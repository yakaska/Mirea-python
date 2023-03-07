import sys
from collections.abc import Sequence

print()


def myprint(*args, sep=' ', end='\n'):
    for arg in args:
        if arg == args[-1]:
            sep = ''
        if is_iterable(arg):
            left_bracket, right_bracket = '[', ']'
            if type(arg) == list:
                left_bracket, right_bracket = '[', ']'
            elif type(arg) == tuple:
                left_bracket, right_bracket = '(', ')'
            elif type(arg) == set:
                left_bracket, right_bracket = '{', '}'
            print_container(arg, [left_bracket, right_bracket])
            sys.stdout.write(sep)
        elif type(arg) == dict:
            left_bracket, right_bracket = '{', '}'
            sys.stdout.write(left_bracket)
            counter = 0
            for i in arg.items():
                sys.stdout.write(f'\'{str(i[0])}\': {str(i[1])}')
                if counter != len((arg.items())) - 1:
                    sys.stdout.write(', ')
                counter += 1
            sys.stdout.write(right_bracket + sep)
        else:
            sys.stdout.write(str(arg) + sep)
    sys.stdout.write(end)


def is_iterable(obj):
    return isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray))


def print_container(container, brackets):
    left_bracket, right_bracket = brackets[0], brackets[1]
    container = list(container)
    sys.stdout.write(left_bracket)
    for i in container:
        sys.stdout.write(str(i))
        if i != container[-1]:
            sys.stdout.write(', ')
    sys.stdout.write(right_bracket)


dict1 = {'qwe': 1, 'qe': 2, 'q': 3}
list1 = [1, 2, 3]
tuple1 = ("Fred", 13, [5, 7, 4])
string1 = "Hello World!"
boolean = True
myprint(dict1, list1, sep='\\', end='\n\n')
myprint(True, False, True)
myprint(1.12)
myprint({1, 2, 3})
