class MealyAutomat:
    def __init__(self):
        self.state = 'A'

    def fade(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'E'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 7
        raise MealyError('fade')

    def race(self):
        if self.state == 'B':
            self.state = 'B'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'A'
            return 6
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'G':
            self.state = 'C'
            return 9
        raise MealyError('race')


class MealyError(Exception):
    pass


def main():
    return MealyAutomat()


def test():
    o = main()
    raises(lambda: o.race(), MealyError)
    assert o.fade() == 0
    assert o.race() == 2
    assert o.fade() == 1
    assert o.race() == 3
    assert o.fade() == 5
    assert o.fade() == 7
    assert o.race() == 8
    with raises(lambda: o.fade(), MealyError):
        print('ass')
    assert o.race() == 9
    o = main()
    assert o.fade() == 0
    assert o.race() == 2
    assert o.fade() == 1
    assert o.race() == 3
    assert o.race() == 6
    o = main()
    assert o.fade() == 0
    assert o.race() == 2
    assert o.fade() == 1
    assert o.fade() == 4


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as ex:
        assert type(ex) == error
    assert output is None
