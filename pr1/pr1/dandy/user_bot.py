def script(check, x, y):
    if check("gold", x, y) != 0:
        return "take"

    if check("level") == 1:
        if check("wall", x + 2, y):
            return 'down'
        return "right"

    if check("level") == 2:
        if check('wall', x-1, y):
            return 'right'
        if check('wall', x, y-1) == 0 and check('wall', x, y-1) == 0:
            return 'up'
        if check('wall', x, y-1) == 1 and check('wall', x+2, y) == 0:
            return 'right'
        if check('gold', x, y + 1):
            return 'down'
        if check('gold', x, y - 1):
            return 'up'

    return "pass"
