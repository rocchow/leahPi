"""
Configuration settings for the Raspberry Pi Learning App
"""
import os

# Display Settings
# Common resolutions:
# 3.5" screen: 480x320
# 7" screen: 800x480
# 10" screen: 1024x600
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
FULLSCREEN = True  # Set to False for windowed mode (useful for testing on non-Pi systems)

# Colors (RGB)
COLOR_BACKGROUND = (240, 248, 255)  # Alice Blue
COLOR_PRIMARY = (70, 130, 180)  # Steel Blue
COLOR_SECONDARY = (255, 182, 193)  # Light Pink
COLOR_SUCCESS = (144, 238, 144)  # Light Green
COLOR_ERROR = (255, 99, 71)  # Tomato
COLOR_TEXT = (25, 25, 112)  # Midnight Blue
COLOR_BUTTON = (100, 149, 237)  # Cornflower Blue
COLOR_BUTTON_HOVER = (65, 105, 225)  # Royal Blue
COLOR_GUIDE_LINE = (200, 200, 200)  # Light Gray
COLOR_USER_DRAWING = (70, 130, 180)  # Steel Blue
COLOR_CORRECT = (50, 205, 50)  # Lime Green
COLOR_INCORRECT = (255, 69, 0)  # Red Orange

# Touch Settings
TOUCH_SENSITIVITY = 5  # Minimum distance between touch points
TOUCH_DEADZONE = 10  # Ignore touches within this radius of buttons

# Tracing Settings
TRACING_TOLERANCE = 20  # Pixels - how close user needs to be to guide line
TRACING_COMPLETION_THRESHOLD = 0.7  # 70% of path must be traced correctly
GUIDE_LINE_WIDTH = 3
USER_LINE_WIDTH = 4
DASH_LENGTH = 10
DASH_GAP = 5

# UI Settings
BUTTON_HEIGHT = 40  # Reduced for smaller screen
BUTTON_PADDING = 10
FONT_SIZE_LARGE = 48  # Reduced for smaller screen
FONT_SIZE_MEDIUM = 32
FONT_SIZE_SMALL = 24
CHARACTER_DISPLAY_SIZE = 180  # Reduced for 3.5" screen
CHARACTER_GRID_COLS = 2  # 2x2 grid (4 characters visible at once)
CHARACTER_GRID_ROWS = 2
CHARACTER_BUTTON_SIZE = 100  # Size of character buttons in grid

# Animation Settings
ANIMATION_SPEED = 0.1
CELEBRATION_DURATION = 2.0  # seconds

# Paths
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
