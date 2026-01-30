"""
Tracing Engine - Core tracing logic, validation, and rendering
"""
import pygame
import math
import numpy as np
import config


class TracingEngine:
    """Handles character tracing, validation, and visual feedback"""
    
    def __init__(self, screen, character_data):
        """
        Initialize tracing engine
        character_data: dict with 'strokes' (list of paths), 'name', 'pronunciation'
        """
        self.screen = screen
        self.character_data = character_data
        self.user_path = []  # List of (x, y) tuples from user drawing
        self.scaled_guide_paths = []
        self.scale_factor = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.completion_percentage = 0.0
        self.is_complete = False
        
        # Calculate display area (center of screen, leaving space for UI)
        screen_width, screen_height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        self.display_area_size = config.CHARACTER_DISPLAY_SIZE
        self.display_x = (screen_width - self.display_area_size) // 2
        # Adjust Y position for smaller screen (account for title and buttons)
        self.display_y = 50  # Start below title/pronunciation
        
        self._prepare_guide_paths()
    
    def _prepare_guide_paths(self):
        """Scale and position guide paths for display"""
        if not self.character_data or 'strokes' not in self.character_data:
            return
        
        # Find bounding box of character (assuming normalized 0-100 coordinates)
        all_points = []
        for stroke in self.character_data['strokes']:
            all_points.extend(stroke)
        
        if not all_points:
            return
        
        min_x = min(p[0] for p in all_points)
        max_x = max(p[0] for p in all_points)
        min_y = min(p[1] for p in all_points)
        max_y = max(p[1] for p in all_points)
        
        # Calculate scale to fit in display area with padding
        padding = 10
        char_width = max_x - min_x
        char_height = max_y - min_y
        
        scale_x = (self.display_area_size - 2 * padding) / max(char_width, 1)
        scale_y = (self.display_area_size - 2 * padding) / max(char_height, 1)
        self.scale_factor = min(scale_x, scale_y)
        
        # Center the character
        scaled_width = char_width * self.scale_factor
        scaled_height = char_height * self.scale_factor
        
        self.offset_x = self.display_x + (self.display_area_size - scaled_width) // 2 - min_x * self.scale_factor
        self.offset_y = self.display_y + (self.display_area_size - scaled_height) // 2 - min_y * self.scale_factor
        
        # Scale all guide paths
        self.scaled_guide_paths = []
        for stroke in self.character_data['strokes']:
            scaled_stroke = [
                (x * self.scale_factor + self.offset_x, y * self.scale_factor + self.offset_y)
                for x, y in stroke
            ]
            self.scaled_guide_paths.append(scaled_stroke)
    
    def add_user_point(self, x, y):
        """Add a point to the user's drawing path"""
        self.user_path.append((x, y))
        self._validate_path()
    
    def set_user_path(self, path):
        """Set the entire user path"""
        self.user_path = path.copy() if path else []
        self._validate_path()
    
    def clear_user_path(self):
        """Clear the user's drawing"""
        self.user_path = []
        self.completion_percentage = 0.0
        self.is_complete = False
    
    def _validate_path(self):
        """Validate user path against guide paths and calculate completion"""
        if not self.user_path or not self.scaled_guide_paths:
            self.completion_percentage = 0.0
            self.is_complete = False
            return
        
        # Flatten all guide points
        all_guide_points = []
        for stroke in self.scaled_guide_paths:
            all_guide_points.extend(stroke)
        
        if not all_guide_points:
            return
        
        # For each user point, find closest guide point
        correct_points = 0
        total_guide_points = len(all_guide_points)
        
        for ux, uy in self.user_path:
            min_distance = float('inf')
            for gx, gy in all_guide_points:
                distance = math.sqrt((ux - gx)**2 + (uy - gy)**2)
                min_distance = min(min_distance, distance)
            
            if min_distance <= config.TRACING_TOLERANCE:
                correct_points += 1
        
        # Calculate percentage (user points that are close to guide)
        if len(self.user_path) > 0:
            accuracy = correct_points / len(self.user_path)
        else:
            accuracy = 0
        
        # Also check coverage of guide points
        covered_guide_points = 0
        for gx, gy in all_guide_points:
            min_distance = float('inf')
            for ux, uy in self.user_path:
                distance = math.sqrt((ux - gx)**2 + (uy - gy)**2)
                min_distance = min(min_distance, distance)
            
            if min_distance <= config.TRACING_TOLERANCE:
                covered_guide_points += 1
        
        coverage = covered_guide_points / total_guide_points if total_guide_points > 0 else 0
        
        # Combined score
        self.completion_percentage = (accuracy * 0.5 + coverage * 0.5)
        self.is_complete = self.completion_percentage >= config.TRACING_COMPLETION_THRESHOLD
    
    def _draw_dashed_line(self, surface, color, start_pos, end_pos, dash_length, gap_length):
        """Draw a dashed line"""
        x1, y1 = start_pos
        x2, y2 = end_pos
        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if distance == 0:
            return
        
        # Unit vector
        dx = (x2 - x1) / distance
        dy = (y2 - y1) / distance
        
        current_distance = 0
        draw_dash = True
        
        while current_distance < distance:
            if draw_dash:
                end_dash = min(current_distance + dash_length, distance)
                start_x = x1 + dx * current_distance
                start_y = y1 + dy * current_distance
                end_x = x1 + dx * end_dash
                end_y = y1 + dy * end_dash
                pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), config.GUIDE_LINE_WIDTH)
            
            current_distance += dash_length + gap_length if draw_dash else gap_length
            draw_dash = not draw_dash
    
    def render(self):
        """Render the tracing interface"""
        # Draw guide lines (dashed)
        for stroke in self.scaled_guide_paths:
            if len(stroke) < 2:
                continue
            
            for i in range(len(stroke) - 1):
                self._draw_dashed_line(
                    self.screen,
                    config.COLOR_GUIDE_LINE,
                    stroke[i],
                    stroke[i + 1],
                    config.DASH_LENGTH,
                    config.DASH_GAP
                )
        
        # Draw user path with color feedback
        if len(self.user_path) > 1:
            for i in range(len(self.user_path) - 1):
                x1, y1 = self.user_path[i]
                x2, y2 = self.user_path[i + 1]
                
                # Determine color based on proximity to guide
                color = config.COLOR_USER_DRAWING
                if self.scaled_guide_paths:
                    # Check if this segment is close to any guide point
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2
                    
                    min_distance = float('inf')
                    for stroke in self.scaled_guide_paths:
                        for gx, gy in stroke:
                            distance = math.sqrt((mid_x - gx)**2 + (mid_y - gy)**2)
                            min_distance = min(min_distance, distance)
                    
                    if min_distance <= config.TRACING_TOLERANCE:
                        color = config.COLOR_CORRECT
                    elif min_distance <= config.TRACING_TOLERANCE * 2:
                        color = config.COLOR_USER_DRAWING
                    else:
                        color = config.COLOR_INCORRECT
                
                pygame.draw.line(self.screen, color, (x1, y1), (x2, y2), config.USER_LINE_WIDTH)
        
        # Draw completion indicator
        if self.completion_percentage > 0:
            # Progress bar at bottom (smaller for 3.5" screen)
            bar_width = 150
            bar_height = 12
            bar_x = (config.SCREEN_WIDTH - bar_width) // 2
            bar_y = config.SCREEN_HEIGHT - 50
            
            # Background
            pygame.draw.rect(self.screen, (200, 200, 200), (bar_x, bar_y, bar_width, bar_height))
            
            # Progress fill
            fill_width = int(bar_width * self.completion_percentage)
            progress_color = config.COLOR_SUCCESS if self.is_complete else config.COLOR_PRIMARY
            pygame.draw.rect(self.screen, progress_color, (bar_x, bar_y, fill_width, bar_height))
            
            # Border
            pygame.draw.rect(self.screen, config.COLOR_TEXT, (bar_x, bar_y, bar_width, bar_height), 2)
    
    def get_completion(self):
        """Get completion percentage and status"""
        return self.completion_percentage, self.is_complete
