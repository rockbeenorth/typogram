import config as c

def size_generator() -> dict:
    """
    - For each scheme (REM.desktop & REM.mobile) generate different sizes
    - For each tag generate S sizes
    """

    result = {}

    for name, values in c.TAGS.items():
        result[name] = {}
        for size, s in c.SIZE.items():

            scaled_size = s * values['scale']

            # print(name, size, scaled_size, f'{int(round(scaled_size*16, 0))}px')
            print(name, size, scaled_size, f'{scaled_size*16}px')

            result[name][size] = scaled_size
    #         # result.get(tag, tag)

    #         # result[tag][s] = s * tag['scale']

    print(result)


if __name__ == "__main__":
    size_generator()

    # x = 1.392
    # print( x % x > 0 )