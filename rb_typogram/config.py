REM = {
    'desktop': 16,
    'mobile': 14,
}

FONT_WEIGHT = {
    'bolder': 800,
    'bold': 600,
    'regular': 400,
    'thin': 300,
    'thinner': 200,
}

LINE_HEIGHT = {
    'regular': 1.25,
    'loose': 1.5,
    'compact': 1.15,
}

SCALE = {
    'xxl': 3.25,
    'xl': 1.75,
    'l': 1.25,
    'm': 1,
    's': .875,
    'xs': .75,
    'xxs': .5
}

SIZE = {
    'S': .875,
    'M': 1,
    'L': 1.5,
}

TAGS = {
    'h1': {
        'font-weight': FONT_WEIGHT['thin'],
        'scale': SCALE['xl'],
        'line-height': LINE_HEIGHT['compact']
    },
    'h2': {
        'font-weight': FONT_WEIGHT['bold'],
        'scale': SCALE['l'],
        'line-height': LINE_HEIGHT['regular']
    },
    'h3': {
        'font-weight': FONT_WEIGHT['bold'],
        'scale': SCALE['m'],
        'line-height': LINE_HEIGHT['regular']
    },
    'h4': {
        'font-weight': FONT_WEIGHT['bold'],
        'scale': SCALE['s'],
        'line-height': LINE_HEIGHT['regular']
    },
    'h5': {
        'font-weight': FONT_WEIGHT['regular'],
        'scale': SCALE['s'],
        'line-height': LINE_HEIGHT['regular']
    },
    'p': {
        'font-weight': FONT_WEIGHT['regular'],
        'scale': SCALE['m'],
        'line-height': LINE_HEIGHT['loose']
    }
}