#!/usr/bin/env python3
"""
Raspberry Pi Interactive Learning App
Main entry point
"""
import sys
import pygame
from src.display_manager import DisplayManager
from src.touch_handler import TouchHandler
from src.ui.menu_screen import MenuScreen
from src.ui.tracing_screen import TracingScreen


class LearningApp:
    """Main application class"""
    
    def __init__(self):
        self.display_manager = DisplayManager()
        self.touch_handler = TouchHandler()
        self.screen = None
        self.current_screen = None
        self.running = True
        self.clock = pygame.time.Clock()
        
    def initialize(self):
        """Initialize the application"""
        self.screen = self.display_manager.initialize()
        if not self.screen:
            print("Failed to initialize display")
            return False
        
        # Start with menu screen
        self.current_screen = MenuScreen(self.screen)
        return True
    
    def run(self):
        """Main application loop"""
        if not self.initialize():
            return
        
        last_time = pygame.time.get_ticks()
        
        while self.running:
            # Calculate delta time
            current_time = pygame.time.get_ticks()
            dt = (current_time - last_time) / 1000.0  # Convert to seconds
            last_time = current_time
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                
                # Handle touch events
                handled, touch_data = self.touch_handler.handle_event(event)
                
                # Pass to current screen
                if isinstance(self.current_screen, TracingScreen) and handled:
                    self.current_screen.handle_touch(touch_data)
                
                # Handle other events
                action = self.current_screen.handle_event(event)
                if action:
                    self._handle_action(action)
            
            # Update current screen
            self.current_screen.update(dt)
            
            # Render
            self.current_screen.render()
            self.display_manager.update()
            
            # Limit frame rate
            self.clock.tick(60)
        
        self.cleanup()
    
    def _handle_action(self, action):
        """Handle actions from screens"""
        if action == 'back_to_menu':
            self.current_screen = MenuScreen(self.screen)
        
        elif isinstance(action, dict):
            if action.get('action') == 'start_tracing':
                language = action.get('language')
                character = action.get('character')
                self.current_screen = TracingScreen(self.screen, language, character)
    
    def cleanup(self):
        """Clean up resources"""
        self.display_manager.quit()


def main():
    """Entry point"""
    try:
        app = LearningApp()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        pygame.quit()
        sys.exit(0)


if __name__ == "__main__":
    main()
