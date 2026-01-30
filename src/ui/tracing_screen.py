"""
Tracing Screen - Character tracing interface
"""
import pygame
import config
from src.tracing_engine import TracingEngine
from src.ui.ui_components import Button


class TracingScreen:
    """Screen for tracing characters"""
    
    def __init__(self, screen, language, character):
        self.screen = screen
        self.language = language
        self.character = character
        self.character_data = None
        self.tracing_engine = None
        self.buttons = []
        self.completion_animation_time = 0
        self.show_completion = False
        self.pending_action = None
        
        self._load_character_data()
        self._setup_buttons()
    
    def _load_character_data(self):
        """Load character data from language module"""
        # Import language module
        if self.language == 'english':
            from src.languages import english as lang_module
        elif self.language == 'numbers':
            from src.languages import numbers as lang_module
        elif self.language == 'korean':
            from src.languages import korean as lang_module
        elif self.language == 'chinese':
            from src.languages import chinese as lang_module
        else:
            return
        
        # Get character data
        self.character_data = lang_module.get_character(self.character)
        
        if self.character_data:
            self.tracing_engine = TracingEngine(self.screen, self.character_data)
    
    def _setup_buttons(self):
        """Create navigation and control buttons"""
        button_width = 120
        button_height = config.BUTTON_HEIGHT
        button_y = config.SCREEN_HEIGHT - 50
        
        # Back button
        back_x = 20
        self.back_button = Button(
            back_x, button_y, button_width, button_height,
            "Back", config.FONT_SIZE_SMALL,
            callback=lambda: self._on_back()
        )
        
        # Clear button
        clear_x = config.SCREEN_WIDTH // 2 - button_width // 2
        self.clear_button = Button(
            clear_x, button_y, button_width, button_height,
            "Clear", config.FONT_SIZE_SMALL,
            callback=lambda: self._on_clear()
        )
        
        # Next button
        next_x = config.SCREEN_WIDTH - button_width - 20
        self.next_button = Button(
            next_x, button_y, button_width, button_height,
            "Next", config.FONT_SIZE_SMALL,
            callback=lambda: self._on_next()
        )
        
        self.buttons = [self.back_button, self.clear_button, self.next_button]
    
    def _on_back(self):
        """Return to menu"""
        self.pending_action = 'back_to_menu'
    
    def _on_clear(self):
        """Clear current drawing"""
        if self.tracing_engine:
            self.tracing_engine.clear_user_path()
    
    def _on_next(self):
        """Go to next character (for now, just go back to menu)"""
        self.pending_action = 'back_to_menu'
    
    def handle_touch(self, touch_data):
        """Handle touch input for drawing"""
        if not self.tracing_engine:
            return
        
        if touch_data['is_touching']:
            if touch_data['position']:
                # Check if touch is in drawing area (not on buttons)
                touch_x, touch_y = touch_data['position']
                
                # Check if touching a button
                touching_button = False
                for btn in self.buttons:
                    if btn.is_clicked((touch_x, touch_y)):
                        touching_button = True
                        break
                
                if not touching_button:
                    # Add point to tracing engine
                    self.tracing_engine.add_user_point(touch_x, touch_y)
        else:
            # Touch released - validate final path
            if touch_data['path']:
                self.tracing_engine.set_user_path(touch_data['path'])
                
                # Check if completed
                completion, is_complete = self.tracing_engine.get_completion()
                if is_complete and not self.show_completion:
                    self.show_completion = True
                    self.completion_animation_time = 0
    
    def handle_event(self, event):
        """Handle pygame events"""
        # Handle button clicks
        for btn in self.buttons:
            if btn.handle_event(event):
                if self.pending_action:
                    action = self.pending_action
                    self.pending_action = None
                    return action
        
        return None
    
    def update(self, dt):
        """Update screen state"""
        if self.show_completion:
            self.completion_animation_time += dt
            if self.completion_animation_time >= config.CELEBRATION_DURATION:
                self.show_completion = False
                self.completion_animation_time = 0
    
    def render(self):
        """Render the tracing screen"""
        # Clear screen
        self.screen.fill(config.COLOR_BACKGROUND)
        
        if not self.tracing_engine:
            # Error state
            error_font = pygame.font.Font(None, config.FONT_SIZE_MEDIUM)
            error_text = error_font.render("Character not found", True, config.COLOR_ERROR)
            error_rect = error_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
            self.screen.blit(error_text, error_rect)
            return
        
        # Draw character name at top
        name_font = pygame.font.Font(None, config.FONT_SIZE_LARGE)
        name_text = name_font.render(self.character, True, config.COLOR_TEXT)
        name_rect = name_text.get_rect(center=(config.SCREEN_WIDTH // 2, 30))
        self.screen.blit(name_text, name_rect)
        
        # Draw pronunciation hint
        if self.character_data and 'pronunciation' in self.character_data:
            pron_font = pygame.font.Font(None, config.FONT_SIZE_SMALL)
            pron_text = pron_font.render(f"({self.character_data['pronunciation']})", True, config.COLOR_TEXT)
            pron_rect = pron_text.get_rect(center=(config.SCREEN_WIDTH // 2, 60))
            self.screen.blit(pron_text, pron_rect)
        
        # Render tracing engine (guide lines and user drawing)
        self.tracing_engine.render()
        
        # Draw completion celebration
        if self.show_completion:
            # Fade effect (start at full opacity, fade out)
            progress = min(self.completion_animation_time / config.CELEBRATION_DURATION, 1.0)
            alpha = int(255 * (1 - progress))
            
            # Celebration text with fade
            celebration_font = pygame.font.Font(None, 96)
            celebration_text = celebration_font.render("Great Job!", True, config.COLOR_SUCCESS)
            celebration_rect = celebration_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
            
            # Apply alpha to the text surface
            celebration_text.set_alpha(alpha)
            self.screen.blit(celebration_text, celebration_rect)
        
        # Draw buttons
        for btn in self.buttons:
            btn.draw(self.screen)
        
        # Draw instructions
        if not self.tracing_engine.user_path:
            inst_font = pygame.font.Font(None, config.FONT_SIZE_SMALL)
            inst_text = inst_font.render("Trace the character with your finger", True, config.COLOR_TEXT)
            inst_rect = inst_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT - 100))
            self.screen.blit(inst_text, inst_rect)
