"""
Korean (Hangul) Character Data
Basic Hangul characters for learning
"""
import math


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
# Basic Hangul characters (자모 - jamo)
CHARACTERS = {
    'ㄱ': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
        ],
        'name': 'ㄱ',
        'pronunciation': 'giyeok'
    },
    'ㄴ': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 15),
            create_line_points(20, 80, 80, 80, 10),
        ],
        'name': 'ㄴ',
        'pronunciation': 'nieun'
    },
    'ㄷ': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(80, 20, 80, 50, 10),
        ],
        'name': 'ㄷ',
        'pronunciation': 'digeut'
    },
    'ㄹ': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(80, 50, 80, 80, 10),
        ],
        'name': 'ㄹ',
        'pronunciation': 'rieul'
    },
    'ㅁ': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 20),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(80, 20, 80, 80, 20),
            create_line_points(20, 80, 80, 80, 10),
        ],
        'name': 'ㅁ',
        'pronunciation': 'mieum'
    },
    'ㅂ': {
        'strokes': [
            create_line_points(30, 20, 30, 80, 20),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(70, 20, 70, 80, 20),
        ],
        'name': 'ㅂ',
        'pronunciation': 'bieup'
    },
    'ㅅ': {
        'strokes': [
            create_line_points(50, 20, 20, 80, 15),
            create_line_points(50, 20, 80, 80, 15),
        ],
        'name': 'ㅅ',
        'pronunciation': 'siot'
    },
    'ㅇ': {
        'strokes': [
            [(50, 50), (45, 45), (40, 40), (35, 45), (30, 50), (35, 55), (40, 60), (45, 55), (50, 50)],
        ],
        'name': 'ㅇ',
        'pronunciation': 'ieung'
    },
    'ㅈ': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(50, 20, 50, 50, 10),
        ],
        'name': 'ㅈ',
        'pronunciation': 'jieut'
    },
    'ㅊ': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(50, 15, 50, 50, 10),
        ],
        'name': 'ㅊ',
        'pronunciation': 'chieut'
    },
    'ㅋ': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(50, 20, 50, 50, 10),
            create_line_points(50, 20, 70, 15, 5),
        ],
        'name': 'ㅋ',
        'pronunciation': 'kieuk'
    },
    'ㅌ': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(50, 20, 50, 50, 10),
            create_line_points(50, 20, 70, 15, 5),
            create_line_points(50, 20, 70, 25, 5),
        ],
        'name': 'ㅌ',
        'pronunciation': 'tieut'
    },
    'ㅍ': {
        'strokes': [
            create_line_points(30, 20, 30, 80, 20),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(70, 20, 70, 80, 20),
            create_line_points(50, 15, 50, 50, 5),
        ],
        'name': 'ㅍ',
        'pronunciation': 'pieup'
    },
    'ㅎ': {
        'strokes': [
            create_line_points(50, 20, 20, 80, 15),
            create_line_points(50, 20, 80, 80, 15),
            create_line_points(20, 50, 80, 50, 10),
        ],
        'name': 'ㅎ',
        'pronunciation': 'hieut'
    },
    'ㅏ': {
        'strokes': [
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(50, 50, 80, 50, 10),
        ],
        'name': 'ㅏ',
        'pronunciation': 'a'
    },
    'ㅓ': {
        'strokes': [
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(20, 50, 50, 50, 10),
        ],
        'name': 'ㅓ',
        'pronunciation': 'eo'
    },
    'ㅗ': {
        'strokes': [
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(50, 50, 80, 50, 10),
        ],
        'name': 'ㅗ',
        'pronunciation': 'o'
    },
    'ㅜ': {
        'strokes': [
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(50, 50, 80, 50, 10),
        ],
        'name': 'ㅜ',
        'pronunciation': 'u'
    },
    'ㅡ': {
        'strokes': [
            create_line_points(20, 50, 80, 50, 10),
        ],
        'name': 'ㅡ',
        'pronunciation': 'eu'
    },
    'ㅣ': {
        'strokes': [
            create_line_points(50, 20, 50, 80, 20),
        ],
        'name': 'ㅣ',
        'pronunciation': 'i'
    },
    '가': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(50, 50, 80, 50, 10),
        ],
        'name': '가',
        'pronunciation': 'ga'
    },
    '나': {
        'strokes': [
            create_line_points(20, 20, 20, 80, 15),
            create_line_points(20, 80, 80, 80, 10),
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(50, 50, 80, 50, 10),
        ],
        'name': '나',
        'pronunciation': 'na'
    },
    '다': {
        'strokes': [
            create_line_points(20, 20, 20, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(80, 20, 80, 50, 10),
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(50, 50, 80, 50, 10),
        ],
        'name': '다',
        'pronunciation': 'da'
    },
}


def get_character(char):
    """Get character data by character"""
    return CHARACTERS.get(char)


def get_all_characters():
    """Get list of all available characters"""
    return sorted(CHARACTERS.keys())
