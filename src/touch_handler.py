"""
Touch Handler - Processes touchscreen input events
"""
import pygame
import math
import config


class TouchHandler:
    """Handles touch input from the touchscreen"""
    
    def __init__(self):
        self.is_touching = False
        self.touch_start_pos = None
        self.current_pos = None
        self.touch_path = []  # List of (x, y) tuples
        self.last_touch_pos = None
        
    def handle_event(self, event):
        """
        Process a pygame event and update touch state
        Returns: (event_handled, touch_data)
        """
        touch_data = {
            'is_touching': self.is_touching,
            'position': self.current_pos,
            'path': self.touch_path.copy(),
            'start_pos': self.touch_start_pos
        }
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button (touch)
                self.is_touching = True
                self.touch_start_pos = event.pos
                self.current_pos = event.pos
                self.touch_path = [event.pos]
                self.last_touch_pos = event.pos
                touch_data['is_touching'] = True
                touch_data['position'] = self.current_pos
                touch_data['start_pos'] = self.touch_start_pos
                return True, touch_data
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_touching = False
                touch_data['is_touching'] = False
                # Keep the path for processing
                return True, touch_data
                
        elif event.type == pygame.MOUSEMOTION:
            if self.is_touching:
                current_pos = event.pos
                # Only add point if it's far enough from last point (smooth drawing)
                if self.last_touch_pos is None:
                    self.touch_path.append(current_pos)
                    self.last_touch_pos = current_pos
                else:
                    distance = math.sqrt(
                        (current_pos[0] - self.last_touch_pos[0])**2 +
                        (current_pos[1] - self.last_touch_pos[1])**2
                    )
                    if distance >= config.TOUCH_SENSITIVITY:
                        self.touch_path.append(current_pos)
                        self.last_touch_pos = current_pos
                
                self.current_pos = current_pos
                touch_data['position'] = self.current_pos
                touch_data['path'] = self.touch_path.copy()
                return True, touch_data
        
        return False, touch_data
    
    def clear_path(self):
        """Clear the current touch path"""
        self.touch_path = []
        self.last_touch_pos = None
        self.is_touching = False
        self.touch_start_pos = None
        self.current_pos = None
    
    def get_path(self):
        """Get the current touch path"""
        return self.touch_path.copy()
    
    def is_point_in_rect(self, point, rect):
        """
        Check if a touch point is within a rectangle
        rect: (x, y, width, height)
        """
        x, y = point
        rx, ry, rw, rh = rect
        return rx <= x <= rx + rw and ry <= y <= ry + rh
