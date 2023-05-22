class MealyAutomat:
    def __init__(self):
        self.state = 'A'

    def herd(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'A'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 8
        raise MealyError('herd')

    def align(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'D'
            return 7
        raise MealyError('align')

    def carve(self):
        if self.state == 'D':
            self.state = 'B'
            return 6
        if self.state == 'B':
            self.state = 'F'
            return 2
        raise MealyError('carve')


class MealyError(Exception):
    pass


def main():
    return MealyAutomat()


def test():
    o = MealyAutomat()

    raises(lambda: o.align(), MealyError)
    raises(lambda: o.align(), MealyError)
    assert o.herd() == 0
    raises(lambda: o.align(), MealyError)
    assert o.herd() == 1
    raises(lambda: o.carve(), MealyError)
    assert o.herd() == 4

    o = MealyAutomat()
    assert o.herd() == 0
    assert o.carve() == 2
    raises(lambda: o.carve(), MealyError)
    raises(lambda: o.align(), MealyError)
    raises(lambda: o.herd(), MealyError)

    o = MealyAutomat()
    assert o.herd() == 0
    assert o.herd() == 1
    assert o.align() == 3
    assert o.align() == 7
    assert o.carve() == 6
    assert o.carve() == 2

    o = MealyAutomat()
    assert o.herd() == 0
    assert o.herd() == 1
    assert o.align() == 3
    assert o.herd() == 5
    raises(lambda: o.carve(), MealyError)
    raises(lambda: o.align(), MealyError)
    assert o.herd() == 8

    o = MealyAutomat()
    assert o.herd() == 0
    assert o.herd() == 1
    assert o.herd() == 4
    assert o.herd() == 0
    assert o.herd() == 1
    assert o.align() == 3
    assert o.align() == 7
    assert o.herd() == 5
    assert o.herd() == 8


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as ex:
        assert type(ex) == error
    assert output is None
