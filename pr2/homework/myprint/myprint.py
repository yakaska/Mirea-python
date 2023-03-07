import sys

print()


def myprint(*args, sep=' ', end='\n'):
    for arg_i in range(len(args)):
        arg = args[arg_i]
        if arg_i == len(args) - 1:
            sep = ''
        if type(arg) == list:
            left_bracket, right_bracket = '[', ']'
            sys.stdout.write(left_bracket)
            for i in arg:
                sys.stdout.write(str(i))
                if i != arg[-1]:
                    sys.stdout.write(', ')
            sys.stdout.write(right_bracket + sep)
        elif type(arg) == tuple:
            left_bracket, right_bracket = '(', ')'
            sys.stdout.write(left_bracket)
            for i in arg:
                sys.stdout.write(str(i))
                if i != arg[-1]:
                    sys.stdout.write(', ')
            sys.stdout.write(right_bracket + sep)
        elif type(arg) == dict:
            left_bracket, right_bracket = '{', '}'
            sys.stdout.write(left_bracket)
            counter = 0
            for i in arg.items():
                sys.stdout.write(chr(39) + str(i[0]) + chr(39) + ': ' + str(i[1]))
                if counter != len((arg.items())) - 1:
                    sys.stdout.write(', ')
                counter += 1
            sys.stdout.write(right_bracket + sep)
        else:
            sys.stdout.write(str(arg) + sep)
    sys.stdout.write(end)


dict1 = {'qwe': 1, 'qe': 2, 'q': 3}
list1 = [1, 2, 3]
tuple1 = ("Fred", 13, [5, 7, 4])
string1 = "Hello World!"
boolean = True
myprint(dict1, list1, sep='\\')
myprint(True, False, True)
myprint(1.12)
