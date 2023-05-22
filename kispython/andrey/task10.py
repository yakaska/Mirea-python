class MealyAutomat:
    def __init__(self):
        self.state = 'A'

    def shade(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'H'
            return 5
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'G':
            self.state = 'H'
            return 10
        raise MealyError('shade')

    def send(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 3
        raise MealyError('send')

    def mass(self):
        if self.state == 'A':
            self.state = 'H'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'H'
            return 7
        if self.state == 'E':
            self.state = 'F'
            return 8
        if self.state == 'F':
            self.state = 'G'
            return 9
        if self.state == 'G':
            self.state = 'B'
            return 11


class MealyError(Exception):
    pass


def main():
    return MealyAutomat()


def test():
    o = main()
    # Test shade function
    assert o.shade() == 0
    assert o.state == 'B'
    raises(lambda: o.shade(), MealyError)
    assert o.state == 'B'
    o.state = 'C'
    assert o.shade() == 5
    assert o.state == 'H'
    o.state = 'D'
    assert o.shade() == 6
    assert o.state == 'E'
    o.state = 'G'
    assert o.shade() == 10
    assert o.state == 'H'
    raises(lambda: o.shade(), MealyError)
    assert o.state == 'H'

    # Test send function
    o.state = 'A'
    assert o.send() == 1
    assert o.state == 'D'
    raises(lambda: o.send(), MealyError)
    assert o.state == 'D'
    o.state = 'B'
    assert o.send() == 3
    assert o.state == 'C'
    raises(lambda: o.send(), MealyError)
    assert o.state == 'C'

    # Test mass function
    o.state = 'A'
    assert o.mass() == 2
    assert o.state == 'H'
    raises(lambda: o.mass(), MealyError)
    assert o.state == 'H'
    o.state = 'C'
    assert o.mass() == 4
    assert o.state == 'D'
    o.state = 'D'
    assert o.mass() == 7
    assert o.state == 'H'
    o.state = 'E'
    assert o.mass() == 8
    assert o.state == 'F'
    o.state = 'F'
    assert o.mass() == 9
    assert o.state == 'G'
    o.state = 'G'
    assert o.mass() == 11
    assert o.state == 'B'
    raises(lambda: o.mass(), MealyError)
    assert o.state == 'B'


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as ex:
        assert type(ex) == error
    assert output is None
