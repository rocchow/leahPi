"""
Numbers Character Data (0-9)
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


# Normalized coordinates (0-100 scale)
CHARACTERS = {
    '0': {
        'strokes': [
            create_circle_points(50, 50, 30, 30),
        ],
        'name': '0',
        'pronunciation': 'zero'
    },
    '1': {
        'strokes': [
            create_line_points(50, 20, 50, 80, 20),
        ],
        'name': '1',
        'pronunciation': 'one'
    },
    '2': {
        'strokes': [
            [(20, 30), (30, 25), (50, 20), (70, 25), (80, 30), (80, 50), (70, 60), (50, 70), (30, 75), (20, 80), (80, 80)],
        ],
        'name': '2',
        'pronunciation': 'two'
    },
    '3': {
        'strokes': [
            [(20, 25), (40, 20), (60, 25), (70, 35), (60, 45), (50, 50), (60, 55), (70, 65), (60, 75), (40, 80), (20, 75)],
        ],
        'name': '3',
        'pronunciation': 'three'
    },
    '4': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 15),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(80, 20, 80, 80, 20),
        ],
        'name': '4',
        'pronunciation': 'four'
    },
    '5': {
        'strokes': [
            create_line_points(20, 20, 70, 20, 10),
            create_line_points(20, 20, 20, 50, 15),
            create_line_points(20, 50, 60, 50, 10),
            create_line_points(60, 50, 70, 60, 10),
            create_line_points(70, 60, 60, 70, 10),
            create_line_points(60, 70, 30, 75, 10),
            create_line_points(30, 75, 20, 80, 10),
        ],
        'name': '5',
        'pronunciation': 'five'
    },
    '6': {
        'strokes': [
            [(70, 30), (60, 25), (40, 20), (20, 30), (20, 50), (30, 60), (50, 65), (70, 60), (80, 50), (80, 70), (70, 75), (50, 80), (30, 75), (20, 70)],
        ],
        'name': '6',
        'pronunciation': 'six'
    },
    '7': {
        'strokes': [
            create_line_points(20, 20, 80, 20, 10),
            create_line_points(80, 20, 50, 80, 20),
        ],
        'name': '7',
        'pronunciation': 'seven'
    },
    '8': {
        'strokes': [
            create_circle_points(50, 35, 20, 20),
            create_circle_points(50, 65, 20, 20),
        ],
        'name': '8',
        'pronunciation': 'eight'
    },
    '9': {
        'strokes': [
            [(30, 30), (50, 25), (70, 30), (80, 40), (80, 60), (70, 70), (50, 75), (30, 70), (20, 60), (20, 40), (30, 30), (30, 50), (50, 55), (70, 50)],
        ],
        'name': '9',
        'pronunciation': 'nine'
    },
}


def get_character(char):
    """Get character data by character"""
    return CHARACTERS.get(char)


def get_all_characters():
    """Get list of all available characters"""
    return sorted(CHARACTERS.keys())
