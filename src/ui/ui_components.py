"""
Reusable UI Components
"""
import pygame
import config


class Button:
    """Simple button component"""
    
    def __init__(self, x, y, width, height, text, font_size=None, callback=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.is_hovered = False
        self.font_size = font_size or config.FONT_SIZE_MEDIUM
        self.font = pygame.font.Font(None, self.font_size)
        
    def handle_event(self, event):
        """Handle mouse/touch events"""
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False
    
    def draw(self, screen):
        """Draw the button"""
        # Button color based on hover state
        color = config.COLOR_BUTTON_HOVER if self.is_hovered else config.COLOR_BUTTON
        
        # Draw button
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, config.COLOR_TEXT, self.rect, 3)
        
        # Draw text
        text_surface = self.font.render(self.text, True, config.COLOR_TEXT)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, pos):
        """Check if button is clicked at position"""
        return self.rect.collidepoint(pos)


class CharacterButton(Button):
    """Button for character selection"""
    
    def __init__(self, x, y, size, character, font_size=None, callback=None):
        super().__init__(x, y, size, size, character, font_size, callback)
        self.character = character
        self.size = size
        
    def draw(self, screen):
        """Draw character button with larger character display"""
        # Button background
        color = config.COLOR_BUTTON_HOVER if self.is_hovered else config.COLOR_BUTTON
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, config.COLOR_TEXT, self.rect, 2)
        
        # Draw character (larger)
        char_font = pygame.font.Font(None, self.size - 20)
        char_surface = char_font.render(self.character, True, config.COLOR_TEXT)
        char_rect = char_surface.get_rect(center=self.rect.center)
        screen.blit(char_surface, char_rect)


class GridLayout:
    """Helper for grid layouts"""
    
    @staticmethod
    def calculate_grid(items, cols, screen_width, start_y, item_width, item_height, spacing=10):
        """Calculate positions for grid layout"""
        positions = []
        total_width = cols * item_width + (cols - 1) * spacing
        start_x = (screen_width - total_width) // 2
        
        for i, item in enumerate(items):
            row = i // cols
            col = i % cols
            x = start_x + col * (item_width + spacing)
            y = start_y + row * (item_height + spacing)
            positions.append((x, y))
        
        return positions
