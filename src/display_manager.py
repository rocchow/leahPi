"""
Display Manager - Handles Pygame display initialization for Raspberry Pi LCD
"""
import pygame
import os
import config


class DisplayManager:
    """Manages the Pygame display for Raspberry Pi LCD screen"""
    
    def __init__(self):
        self.screen = None
        self.width = config.SCREEN_WIDTH
        self.height = config.SCREEN_HEIGHT
        self.fullscreen = config.FULLSCREEN
        
    def initialize(self):
        """Initialize Pygame and create the display surface"""
        # Initialize Pygame
        pygame.init()
        
        # Set environment variables for Raspberry Pi (if needed)
        # Some LCD displays require specific framebuffer settings
        if os.name != 'nt':  # Not Windows
            # Try to use framebuffer if available
            os.environ['SDL_FBDEV'] = '/dev/fb0'
            os.environ['SDL_MOUSEDEV'] = '/dev/input/touchscreen'
            os.environ['SDL_MOUSEDRV'] = 'TSLIB'
        
        # Hide mouse cursor for touchscreen
        pygame.mouse.set_visible(False)
        
        # Create display
        if self.fullscreen:
            self.screen = pygame.display.set_mode(
                (self.width, self.height),
                pygame.FULLSCREEN
            )
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
        
        pygame.display.set_caption("Learning App")
        
        # Set up clock for frame rate control
        self.clock = pygame.time.Clock()
        
        return self.screen
    
    def get_screen(self):
        """Get the display surface"""
        return self.screen
    
    def get_size(self):
        """Get screen dimensions"""
        return (self.width, self.height)
    
    def update(self):
        """Update the display"""
        pygame.display.flip()
        self.clock.tick(60)  # Target 60 FPS
    
    def quit(self):
        """Clean up and quit Pygame"""
        pygame.quit()
