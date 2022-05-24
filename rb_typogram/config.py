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
    'zero': 1,
}

SCALE = {
    'xxl': 4,
    'xl': 2,
    'l': 1.5,
    # 'xxl': 3,
    # 'xl': 1.75,
    # 'l': 1.25,
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
        'type': 'tag',
        'font-weight': 'thin',
        'scale': SCALE['xxl'],
        'line-height': LINE_HEIGHT['compact']
    },
    'h2': {
        'type': 'tag',
        'font-weight': 'bold',
        'scale': SCALE['xl'],
        'line-height': LINE_HEIGHT['regular']
    },
    'h3': {
        'type': 'tag',
        'font-weight': 'bold',
        'scale': SCALE['l'],
        'line-height': LINE_HEIGHT['regular']
    },
    'h4': {
        'type': 'tag',
        'font-weight': 'bold',
        'scale': SCALE['m'],
        'line-height': LINE_HEIGHT['regular']
    },
    'h5': {
        'type': 'tag',
        'font-weight': 'regular',
        'scale': SCALE['s'],
        'line-height': LINE_HEIGHT['regular']
    },
    'p': {
        'type': 'tag',
        'font-weight': 'regular',
        'scale': SCALE['m'],
        'line-height': LINE_HEIGHT['loose']
    },
    'small': {
        'type': 'class',
        'font-weight': 'regular',
        'scale': SCALE['s'],
        'line-height': LINE_HEIGHT['loose']
    },
    'x-small': {
        'type': 'class',
        'font-weight': 'regular',
        'scale': SCALE['xs'],
        'line-height': LINE_HEIGHT['loose']
    },
    'xx-small': {
        'type': 'class',
        'font-weight': 'regular',
        'scale': SCALE['xxs'],
        'line-height': LINE_HEIGHT['loose']
    },
}