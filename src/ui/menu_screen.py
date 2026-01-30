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
        self.current_page = 0  # For pagination
        self._setup_language_buttons()
    
    def _setup_language_buttons(self):
        """Create language selection buttons"""
        button_width = 100  # Reduced for smaller screen
        button_height = config.BUTTON_HEIGHT
        spacing = 8
        start_y = 50  # Moved up for smaller screen
        
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
        
        # Pagination buttons (will be shown when characters are displayed)
        self.prev_button = None
        self.next_button = None
    
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
        """Create character selection buttons in 2x2 grid with pagination"""
        self.character_buttons = []
        self.current_page = 0
        
        if not self.characters:
            return
        
        # Calculate grid layout - 2x2 (4 characters per page)
        cols = config.CHARACTER_GRID_COLS
        rows = config.CHARACTER_GRID_ROWS
        chars_per_page = cols * rows
        button_size = config.CHARACTER_BUTTON_SIZE
        spacing = 10
        start_y = 140  # Adjusted for smaller screen
        
        # Calculate total pages
        total_pages = (len(self.characters) + chars_per_page - 1) // chars_per_page
        
        # Get characters for current page
        start_idx = self.current_page * chars_per_page
        end_idx = min(start_idx + chars_per_page, len(self.characters))
        page_characters = self.characters[start_idx:end_idx]
        
        # Calculate positions for 2x2 grid
        total_width = cols * button_size + (cols - 1) * spacing
        start_x = (config.SCREEN_WIDTH - total_width) // 2
        
        for i, char in enumerate(page_characters):
            row = i // cols
            col = i % cols
            x = start_x + col * (button_size + spacing)
            y = start_y + row * (button_size + spacing)
            
            btn = CharacterButton(
                x, y, button_size, char, config.FONT_SIZE_MEDIUM,
                callback=lambda c=char: self._select_character(c)
            )
            self.character_buttons.append(btn)
        
        # Setup pagination buttons
        self._setup_pagination_buttons()
    
    def _setup_pagination_buttons(self):
        """Create prev/next buttons for pagination"""
        if not self.characters:
            self.prev_button = None
            self.next_button = None
            return
        
        cols = config.CHARACTER_GRID_COLS
        rows = config.CHARACTER_GRID_ROWS
        chars_per_page = cols * rows
        total_pages = (len(self.characters) + chars_per_page - 1) // chars_per_page
        
        button_width = 60
        button_height = 30
        button_y = config.SCREEN_HEIGHT - 40
        
        # Prev button
        if self.current_page > 0:
            self.prev_button = Button(
                20, button_y, button_width, button_height,
                "◀ Prev", config.FONT_SIZE_SMALL,
                callback=lambda: self._prev_page()
            )
        else:
            self.prev_button = None
        
        # Next button
        if self.current_page < total_pages - 1:
            self.next_button = Button(
                config.SCREEN_WIDTH - button_width - 20, button_y, button_width, button_height,
                "Next ▶", config.FONT_SIZE_SMALL,
                callback=lambda: self._next_page()
            )
        else:
            self.next_button = None
    
    def _prev_page(self):
        """Go to previous page"""
        if self.current_page > 0:
            self.current_page -= 1
            self._setup_character_buttons()
    
    def _next_page(self):
        """Go to next page"""
        cols = config.CHARACTER_GRID_COLS
        rows = config.CHARACTER_GRID_ROWS
        chars_per_page = cols * rows
        total_pages = (len(self.characters) + chars_per_page - 1) // chars_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self._setup_character_buttons()
    
    def _select_character(self, character):
        """Select a character to practice"""
        self.selected_character = character
    
    def handle_event(self, event):
        """Handle input events"""
        # Handle language buttons
        for btn in self.language_buttons:
            if btn.handle_event(event):
                return None
        
        # Handle pagination buttons
        if self.prev_button and self.prev_button.handle_event(event):
            return None
        if self.next_button and self.next_button.handle_event(event):
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
    
    def update(self, dt=0):
        """Update screen state"""
        pass
    
    def render(self):
        """Render the menu screen"""
        # Clear screen
        self.screen.fill(config.COLOR_BACKGROUND)
        
        # Title (smaller for 3.5" screen)
        title_font = pygame.font.Font(None, config.FONT_SIZE_MEDIUM)
        title_text = title_font.render("Learning App", True, config.COLOR_TEXT)
        title_rect = title_text.get_rect(center=(config.SCREEN_WIDTH // 2, 20))
        self.screen.blit(title_text, title_rect)
        
        # Language selection label
        if not self.current_language:
            label_font = pygame.font.Font(None, config.FONT_SIZE_SMALL)
            label_text = label_font.render("Select Language:", True, config.COLOR_TEXT)
            label_rect = label_text.get_rect(center=(config.SCREEN_WIDTH // 2, 35))
            self.screen.blit(label_text, label_rect)
        
        # Draw language buttons
        for btn in self.language_buttons:
            btn.draw(self.screen)
        
        # Draw character buttons
        if self.current_language:
            # Show language label (compact)
            lang_label_font = pygame.font.Font(None, config.FONT_SIZE_SMALL)
            lang_names = {
                'english': 'English',
                'numbers': 'Numbers',
                'korean': 'Korean',
                'chinese': 'Chinese'
            }
            lang_label = lang_names.get(self.current_language, '')
            
            # Calculate page info
            cols = config.CHARACTER_GRID_COLS
            rows = config.CHARACTER_GRID_ROWS
            chars_per_page = cols * rows
            total_pages = (len(self.characters) + chars_per_page - 1) // chars_per_page
            page_info = f"{lang_label} ({self.current_page + 1}/{total_pages})"
            
            lang_text = lang_label_font.render(page_info, True, config.COLOR_TEXT)
            lang_rect = lang_text.get_rect(center=(config.SCREEN_WIDTH // 2, 120))
            self.screen.blit(lang_text, lang_rect)
            
            # Draw character buttons
            for btn in self.character_buttons:
                btn.draw(self.screen)
            
            # Draw pagination buttons
            if self.prev_button:
                self.prev_button.draw(self.screen)
            if self.next_button:
                self.next_button.draw(self.screen)
        
        # Highlight selected language button
        if self.current_language:
            lang_index = ['english', 'numbers', 'korean', 'chinese'].index(self.current_language)
            if 0 <= lang_index < len(self.language_buttons):
                btn = self.language_buttons[lang_index]
                pygame.draw.rect(self.screen, config.COLOR_SUCCESS, btn.rect, 3)
