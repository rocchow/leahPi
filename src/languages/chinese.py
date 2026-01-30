"""
Chinese Character Data
Basic Chinese characters for learning
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
# Basic Chinese characters (汉字)
CHARACTERS = {
    '一': {
        'strokes': [
            create_line_points(20, 50, 80, 50, 10),
        ],
        'name': '一',
        'pronunciation': 'yī (one)'
    },
    '二': {
        'strokes': [
            create_line_points(20, 40, 80, 40, 10),
            create_line_points(20, 60, 80, 60, 10),
        ],
        'name': '二',
        'pronunciation': 'èr (two)'
    },
    '三': {
        'strokes': [
            create_line_points(20, 30, 80, 30, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(20, 70, 80, 70, 10),
        ],
        'name': '三',
        'pronunciation': 'sān (three)'
    },
    '人': {
        'strokes': [
            create_line_points(50, 20, 30, 80, 15),
            create_line_points(50, 20, 70, 80, 15),
        ],
        'name': '人',
        'pronunciation': 'rén (person)'
    },
    '大': {
        'strokes': [
            create_line_points(50, 20, 30, 80, 15),
            create_line_points(50, 20, 70, 80, 15),
            create_line_points(20, 50, 80, 50, 10),
        ],
        'name': '大',
        'pronunciation': 'dà (big)'
    },
    '小': {
        'strokes': [
            create_line_points(50, 20, 50, 50, 10),
            create_line_points(30, 60, 50, 50, 10),
            create_line_points(50, 50, 70, 60, 10),
        ],
        'name': '小',
        'pronunciation': 'xiǎo (small)'
    },
    '口': {
        'strokes': [
            create_line_points(30, 30, 70, 30, 10),
            create_line_points(70, 30, 70, 70, 10),
            create_line_points(70, 70, 30, 70, 10),
            create_line_points(30, 70, 30, 30, 10),
        ],
        'name': '口',
        'pronunciation': 'kǒu (mouth)'
    },
    '日': {
        'strokes': [
            create_line_points(30, 30, 70, 30, 10),
            create_line_points(70, 30, 70, 70, 10),
            create_line_points(70, 70, 30, 70, 10),
            create_line_points(30, 70, 30, 30, 10),
            create_line_points(30, 50, 70, 50, 10),
        ],
        'name': '日',
        'pronunciation': 'rì (sun/day)'
    },
    '月': {
        'strokes': [
            create_line_points(35, 25, 65, 25, 10),
            create_line_points(65, 25, 65, 75, 15),
            create_line_points(65, 75, 35, 75, 10),
            create_line_points(35, 75, 35, 25, 15),
            create_line_points(35, 50, 65, 50, 10),
        ],
        'name': '月',
        'pronunciation': 'yuè (moon/month)'
    },
    '水': {
        'strokes': [
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(30, 40, 50, 50, 10),
            create_line_points(50, 50, 70, 40, 10),
            create_line_points(30, 70, 50, 60, 10),
            create_line_points(50, 60, 70, 70, 10),
        ],
        'name': '水',
        'pronunciation': 'shuǐ (water)'
    },
    '火': {
        'strokes': [
            create_line_points(50, 20, 50, 50, 10),
            create_line_points(30, 40, 50, 50, 10),
            create_line_points(50, 50, 70, 40, 10),
            create_line_points(30, 70, 50, 60, 10),
            create_line_points(50, 60, 70, 70, 10),
        ],
        'name': '火',
        'pronunciation': 'huǒ (fire)'
    },
    '木': {
        'strokes': [
            create_line_points(50, 20, 50, 80, 20),
            create_line_points(20, 50, 50, 50, 10),
            create_line_points(50, 50, 80, 50, 10),
            create_line_points(30, 70, 50, 60, 10),
            create_line_points(50, 60, 70, 70, 10),
        ],
        'name': '木',
        'pronunciation': 'mù (tree)'
    },
    '山': {
        'strokes': [
            create_line_points(50, 20, 30, 50, 10),
            create_line_points(50, 20, 70, 50, 10),
            create_line_points(30, 50, 30, 80, 10),
            create_line_points(30, 80, 70, 80, 10),
            create_line_points(70, 80, 70, 50, 10),
        ],
        'name': '山',
        'pronunciation': 'shān (mountain)'
    },
    '田': {
        'strokes': [
            create_line_points(30, 30, 70, 30, 10),
            create_line_points(70, 30, 70, 70, 10),
            create_line_points(70, 70, 30, 70, 10),
            create_line_points(30, 70, 30, 30, 10),
            create_line_points(30, 50, 70, 50, 10),
            create_line_points(50, 30, 50, 70, 10),
        ],
        'name': '田',
        'pronunciation': 'tián (field)'
    },
    '中': {
        'strokes': [
            create_line_points(30, 30, 70, 30, 10),
            create_line_points(70, 30, 70, 70, 10),
            create_line_points(70, 70, 30, 70, 10),
            create_line_points(30, 70, 30, 30, 10),
            create_line_points(50, 30, 50, 70, 10),
        ],
        'name': '中',
        'pronunciation': 'zhōng (middle/China)'
    },
    '上': {
        'strokes': [
            create_line_points(50, 20, 50, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(50, 50, 50, 80, 10),
        ],
        'name': '上',
        'pronunciation': 'shàng (up/above)'
    },
    '下': {
        'strokes': [
            create_line_points(50, 20, 50, 50, 10),
            create_line_points(20, 50, 80, 50, 10),
            create_line_points(50, 50, 50, 80, 10),
            create_line_points(50, 80, 80, 80, 10),
        ],
        'name': '下',
        'pronunciation': 'xià (down/below)'
    },
    '天': {
        'strokes': [
            create_line_points(20, 30, 80, 30, 10),
            create_line_points(50, 30, 30, 80, 20),
            create_line_points(50, 30, 70, 80, 20),
        ],
        'name': '天',
        'pronunciation': 'tiān (sky/heaven)'
    },
    '好': {
        'strokes': [
            # Left part (女)
            create_line_points(25, 25, 25, 75, 15),
            create_line_points(25, 50, 45, 50, 10),
            create_line_points(25, 75, 45, 75, 10),
            # Right part (子)
            create_line_points(55, 30, 55, 50, 10),
            create_line_points(55, 50, 75, 50, 10),
            create_line_points(75, 50, 75, 75, 10),
            create_line_points(55, 75, 75, 75, 10),
        ],
        'name': '好',
        'pronunciation': 'hǎo (good)'
    },
}


def get_character(char):
    """Get character data by character"""
    return CHARACTERS.get(char)


def get_all_characters():
    """Get list of all available characters"""
    return sorted(CHARACTERS.keys())
