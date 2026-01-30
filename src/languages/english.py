"""
English Alphabet Character Data
Each character has stroke paths defined as coordinate lists
"""
import math


def create_circle_points(center_x, center_y, radius, num_points=20):
    """Helper to create points along a circle"""
    points = []
    for i in range(num_points + 1):
        angle = 2 * math.pi * i / num_points
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    return points


def create_line_points(x1, y1, x2, y2, num_points=10):
    """Helper to create points along a line"""
    points = []
    for i in range(num_points + 1):
        t = i / num_points
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        points.append((x, y))
    return points


# Normalized coordinates (0-100 scale, will be scaled to screen)
# Characters are designed to fit in a 100x100 box
CHARACTERS = {
    'A': {
        'strokes': [
            create_line_points(20, 80, 50, 20, 15),  # Left diagonal
            create_line_points(50, 20, 80, 80, 15),  # Right diagonal
            create_line_points(30, 50, 70, 50, 10),  # Horizontal bar
        ],
        'name': 'A',
        'pronunciation': 'ay'
    },
    'B': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Vertical line
            create_line_points(20, 20, 60, 20, 10),  # Top curve start
            create_line_points(20, 50, 60, 50, 10),  # Middle line
            create_line_points(20, 50, 60, 50, 10),  # Bottom curve start
            create_line_points(20, 80, 60, 80, 10),  # Bottom line
        ],
        'name': 'B',
        'pronunciation': 'bee'
    },
    'C': {
        'strokes': [
            [(70, 30), (60, 25), (50, 20), (40, 20), (30, 25), (25, 30), (20, 40), (20, 50), (20, 60), (25, 70), (30, 75), (40, 80), (50, 80), (60, 75), (70, 70)],
        ],
        'name': 'C',
        'pronunciation': 'see'
    },
    'D': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Vertical line
            [(20, 20), (40, 20), (50, 25), (60, 35), (65, 50), (60, 65), (50, 75), (40, 80), (20, 80)],  # Curve
        ],
        'name': 'D',
        'pronunciation': 'dee'
    },
    'E': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Vertical line
            create_line_points(20, 20, 70, 20, 10),  # Top horizontal
            create_line_points(20, 50, 60, 50, 10),  # Middle horizontal
            create_line_points(20, 80, 70, 80, 10),  # Bottom horizontal
        ],
        'name': 'E',
        'pronunciation': 'ee'
    },
    'F': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Vertical line
            create_line_points(20, 20, 70, 20, 10),  # Top horizontal
            create_line_points(20, 50, 60, 50, 10),  # Middle horizontal
        ],
        'name': 'F',
        'pronunciation': 'ef'
    },
    'G': {
        'strokes': [
            [(70, 30), (60, 25), (50, 20), (40, 20), (30, 25), (25, 30), (20, 40), (20, 50), (20, 60), (25, 70), (30, 75), (40, 80), (50, 80), (60, 75), (70, 70), (70, 50), (50, 50)],
        ],
        'name': 'G',
        'pronunciation': 'jee'
    },
    'H': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Left vertical
            create_line_points(20, 50, 80, 50, 10),  # Horizontal bar
            create_line_points(80, 20, 80, 80, 20),  # Right vertical
        ],
        'name': 'H',
        'pronunciation': 'aych'
    },
    'I': {
        'strokes': [
            create_line_points(20, 20, 80, 20, 10),  # Top horizontal
            create_line_points(50, 20, 50, 80, 20),  # Vertical line
            create_line_points(20, 80, 80, 80, 10),  # Bottom horizontal
        ],
        'name': 'I',
        'pronunciation': 'eye'
    },
    'J': {
        'strokes': [
            create_line_points(20, 20, 80, 20, 10),  # Top horizontal
            create_line_points(50, 20, 50, 70, 20),  # Vertical line
            [(50, 70), (40, 75), (30, 75), (25, 70)],  # Bottom curve
        ],
        'name': 'J',
        'pronunciation': 'jay'
    },
    'K': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Vertical line
            create_line_points(20, 50, 80, 20, 15),  # Top diagonal
            create_line_points(20, 50, 80, 80, 15),  # Bottom diagonal
        ],
        'name': 'K',
        'pronunciation': 'kay'
    },
    'L': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Vertical line
            create_line_points(20, 80, 70, 80, 10),  # Horizontal line
        ],
        'name': 'L',
        'pronunciation': 'el'
    },
    'M': {
        'strokes': [
            create_line_points(20, 80, 20, 20, 20),  # Left vertical
            create_line_points(20, 20, 50, 50, 15),  # Left diagonal
            create_line_points(50, 50, 80, 20, 15),  # Right diagonal
            create_line_points(80, 20, 80, 80, 20),  # Right vertical
        ],
        'name': 'M',
        'pronunciation': 'em'
    },
    'N': {
        'strokes': [
            create_line_points(20, 80, 20, 20, 20),  # Left vertical
            create_line_points(20, 20, 80, 80, 20),  # Diagonal
            create_line_points(80, 80, 80, 20, 20),  # Right vertical
        ],
        'name': 'N',
        'pronunciation': 'en'
    },
    'O': {
        'strokes': [
            create_circle_points(50, 50, 30, 30),
        ],
        'name': 'O',
        'pronunciation': 'oh'
    },
    'P': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Vertical line
            create_line_points(20, 20, 60, 20, 10),  # Top horizontal
            create_line_points(60, 20, 60, 50, 10),  # Right vertical
            create_line_points(20, 50, 60, 50, 10),  # Middle horizontal
        ],
        'name': 'P',
        'pronunciation': 'pee'
    },
    'Q': {
        'strokes': [
            create_circle_points(50, 50, 30, 30),  # Circle
            create_line_points(60, 60, 80, 80, 10),  # Tail
        ],
        'name': 'Q',
        'pronunciation': 'kyoo'
    },
    'R': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Vertical line
            create_line_points(20, 20, 60, 20, 10),  # Top horizontal
            create_line_points(60, 20, 60, 50, 10),  # Right vertical top
            create_line_points(20, 50, 60, 50, 10),  # Middle horizontal
            create_line_points(60, 50, 80, 80, 15),  # Bottom diagonal
        ],
        'name': 'R',
        'pronunciation': 'ar'
    },
    'S': {
        'strokes': [
            [(70, 25), (60, 20), (40, 20), (30, 25), (30, 40), (50, 50), (50, 60), (30, 70), (40, 80), (60, 80), (70, 75)],
        ],
        'name': 'S',
        'pronunciation': 'ess'
    },
    'T': {
        'strokes': [
            create_line_points(20, 20, 80, 20, 10),  # Top horizontal
            create_line_points(50, 20, 50, 80, 20),  # Vertical line
        ],
        'name': 'T',
        'pronunciation': 'tee'
    },
    'U': {
        'strokes': [
            create_line_points(20, 20, 20, 60, 20),  # Left vertical
            [(20, 60), (30, 70), (50, 75), (70, 70), (80, 60)],  # Bottom curve
            create_line_points(80, 60, 80, 20, 20),  # Right vertical
        ],
        'name': 'U',
        'pronunciation': 'yoo'
    },
    'V': {
        'strokes': [
            create_line_points(20, 20, 50, 80, 20),  # Left diagonal
            create_line_points(50, 80, 80, 20, 20),  # Right diagonal
        ],
        'name': 'V',
        'pronunciation': 'vee'
    },
    'W': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),  # Left vertical
            create_line_points(20, 80, 40, 40, 15),  # Left-middle diagonal
            create_line_points(40, 40, 60, 80, 15),  # Right-middle diagonal
            create_line_points(60, 80, 80, 20, 20),  # Right vertical
        ],
        'name': 'W',
        'pronunciation': 'double-yoo'
    },
    'X': {
        'strokes': [
            create_line_points(20, 20, 80, 80, 20),  # Top-left to bottom-right
            create_line_points(80, 20, 20, 80, 20),  # Top-right to bottom-left
        ],
        'name': 'X',
        'pronunciation': 'eks'
    },
    'Y': {
        'strokes': [
            create_line_points(20, 20, 50, 50, 15),  # Top-left diagonal
            create_line_points(80, 20, 50, 50, 15),  # Top-right diagonal
            create_line_points(50, 50, 50, 80, 15),  # Bottom vertical
        ],
        'name': 'Y',
        'pronunciation': 'why'
    },
    'Z': {
        'strokes': [
            create_line_points(20, 20, 80, 20, 10),  # Top horizontal
            create_line_points(80, 20, 20, 80, 20),  # Diagonal
            create_line_points(20, 80, 80, 80, 10),  # Bottom horizontal
        ],
        'name': 'Z',
        'pronunciation': 'zed'
    },
}


def get_character(char):
    """Get character data by character"""
    return CHARACTERS.get(char.upper())


def get_all_characters():
    """Get list of all available characters"""
    return sorted(CHARACTERS.keys())
