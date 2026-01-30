"""
Menu Screen - Language and character selection
"""
import pygame
import config
from src.ui.ui_components import Button, CharacterButton, GridLayout


class MenuScreen:
    """Main menu screen for language and character selection"""
    
    def __init__(self, screen):
        self.screen = screen
        self.current_language = None
        self.characters = []
        self.character_buttons = []
        self.language_buttons = []
        self.selected_character = None
        self._setup_language_buttons()
    
    def _setup_language_buttons(self):
        """Create language selection buttons"""
        button_width = 180
        button_height = config.BUTTON_HEIGHT
        spacing = 20
        start_y = 100
        
        languages = [
            ('English', 'english'),
            ('Numbers', 'numbers'),
            ('Korean', 'korean'),
            ('Chinese', 'chinese'),
        ]
        
        total_width = len(languages) * button_width + (len(languages) - 1) * spacing
        start_x = (config.SCREEN_WIDTH - total_width) // 2
        
        self.language_buttons = []
        for i, (label, lang_id) in enumerate(languages):
            x = start_x + i * (button_width + spacing)
            btn = Button(
                x, start_y, button_width, button_height,
                label, config.FONT_SIZE_SMALL,
                callback=lambda l=lang_id: self._select_language(l)
            )
            self.language_buttons.append(btn)
    
    def _select_language(self, language_id):
        """Load characters for selected language"""
        self.current_language = language_id
        
        # Import language module
        if language_id == 'english':
            from src.languages import english as lang_module
        elif language_id == 'numbers':
            from src.languages import numbers as lang_module
        elif language_id == 'korean':
            from src.languages import korean as lang_module
        elif language_id == 'chinese':
            from src.languages import chinese as lang_module
        else:
            return
        
        # Get characters
        self.characters = lang_module.get_all_characters()
        self._setup_character_buttons()
    
    def _setup_character_buttons(self):
        """Create character selection buttons in grid"""
        self.character_buttons = []
        
        if not self.characters:
            return
        
        # Calculate grid layout
        cols = 6  # 6 columns
        button_size = 80
        spacing = 15
        start_y = 200
        
        positions = GridLayout.calculate_grid(
            self.characters, cols, config.SCREEN_WIDTH,
            start_y, button_size, button_size, spacing
        )
        
        for i, char in enumerate(self.characters):
            x, y = positions[i]
            btn = CharacterButton(
                x, y, button_size, char, config.FONT_SIZE_LARGE,
                callback=lambda c=char: self._select_character(c)
            )
            self.character_buttons.append(btn)
    
    def _select_character(self, character):
        """Select a character to practice"""
        self.selected_character = character
    
    def handle_event(self, event):
        """Handle input events"""
        # Handle language buttons
        for btn in self.language_buttons:
            if btn.handle_event(event):
                return None
        
        # Handle character buttons
        for btn in self.character_buttons:
            if btn.handle_event(event):
                if self.selected_character:
                    return {
                        'action': 'start_tracing',
                        'language': self.current_language,
                        'character': self.selected_character
                    }
        
        return None
    
    def update(self):
        """Update screen state"""
        pass
    
    def render(self):
        """Render the menu screen"""
        # Clear screen
        self.screen.fill(config.COLOR_BACKGROUND)
        
        # Title
        title_font = pygame.font.Font(None, config.FONT_SIZE_LARGE)
        title_text = title_font.render("Learning App", True, config.COLOR_TEXT)
        title_rect = title_text.get_rect(center=(config.SCREEN_WIDTH // 2, 40))
        self.screen.blit(title_text, title_rect)
        
        # Language selection label
        if not self.current_language:
            label_font = pygame.font.Font(None, config.FONT_SIZE_MEDIUM)
            label_text = label_font.render("Select a Language:", True, config.COLOR_TEXT)
            label_rect = label_text.get_rect(center=(config.SCREEN_WIDTH // 2, 60))
            self.screen.blit(label_text, label_rect)
        
        # Draw language buttons
        for btn in self.language_buttons:
            btn.draw(self.screen)
        
        # Draw character buttons
        if self.current_language:
            # Show language label
            lang_label_font = pygame.font.Font(None, config.FONT_SIZE_SMALL)
            lang_names = {
                'english': 'English Alphabet',
                'numbers': 'Numbers',
                'korean': 'Korean (Hangul)',
                'chinese': 'Chinese Characters'
            }
            lang_label = lang_names.get(self.current_language, '')
            lang_text = lang_label_font.render(f"Select a character: {lang_label}", True, config.COLOR_TEXT)
            lang_rect = lang_text.get_rect(center=(config.SCREEN_WIDTH // 2, 170))
            self.screen.blit(lang_text, lang_rect)
            
            for btn in self.character_buttons:
                btn.draw(self.screen)
        
        # Highlight selected language button
        if self.current_language:
            lang_index = ['english', 'numbers', 'korean', 'chinese'].index(self.current_language)
            if 0 <= lang_index < len(self.language_buttons):
                btn = self.language_buttons[lang_index]
                pygame.draw.rect(self.screen, config.COLOR_SUCCESS, btn.rect, 4)
