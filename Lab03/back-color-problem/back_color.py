from random import *

shapes = [ # list of dict
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text_list = []
    color_list = []
    for i in shapes:
        text_list.append(i['text'])
        color_list.append(i['color'])
    text = choice(text_list)
    color = choice(color_list)
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]


def mouse_press(x, y, text, color, quiz_type):
    def is_inside(a, b):
        return b[0] < a[0] < b[0] + b[2] and b[1] < a[1] < b[1] + b[3]
    for i in shapes:
        if quiz_type == 0:
            if i['text'] == text:
                return is_inside([x, y], i['rect'])
        else:
            if i['color'] == color:
                return is_inside([x, y], i['rect'])
