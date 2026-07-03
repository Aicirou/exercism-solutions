COLORS_MAP = {
    0: 'black',
    1: 'brown',
    2: 'red',
    3: 'orange',
    4: 'yellow',
    5: 'green',
    6: 'blue',
    7: 'violet',
    8: 'grey',
    9: 'white'
}

def color_code(color):
    for code, c in COLORS_MAP.items():
        if c == color:
            return code
    return None

def colors():
    return list(COLORS_MAP.values())