import config as c

PIXEL = 16


def check_xceptions(x):

    if .75 < x < .8:
        return .75

    if 1.05 < x < 1.1:
        return 1.125

    if 1.5 < x < 1.6:
        return 1.5

    if 1.3 < x < 1.32:
        return 1.375

    return x


def size_generator() -> dict:
    """
    - For each scheme (REM.desktop & REM.mobile) generate different sizes
    - For each tag generate S sizes
    """

    result = {}

    for name, values in c.TAGS.items():
        result[name] = {}
        if values['type'] == 'tag':
            for size, s in c.SIZE.items():
                scaled_size = check_xceptions(s * values['scale'])
                residual = scaled_size*PIXEL % 2
                pixels = scaled_size * PIXEL
                line_height = values['line-height'] * PIXEL
                print(f'{name}.{size}\t\t{scaled_size}',
                      '\t\t', f'{pixels}px', '\t\t', residual, '\t\t', f'{line_height}px')
                result[name][size] = scaled_size
        if values['type'] == 'class':
            result[name]['M'] = values['scale']

    print(result)

    return result


if __name__ == "__main__":
    size_generator()
