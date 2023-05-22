def main(args):
    dict1 = {'PAWN': 1, 'COBOL': 2}
    dict2 = {'PAWN': 4, 'COBOL': 5}
    dict3 = {2007: 8, 2020: 9}
    if args[3] == 1960:
        return 6
    if args[3] == 1985:
        if args[0] == 1995:
            return 7
        if args[1] == 'COBOL':
            return 10
        else:
            return dict3.get(args[2])
    elif args[3] == 1983:
        if args[0] == 1995:
            if args[4] == 2019:
                return 0
            else:
                return dict1.get(args[1])
        else:
            if args[4] == 2019:
                return 3
            else:
                return dict2.get(args[1])
