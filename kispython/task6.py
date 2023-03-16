def main(args):
    dict1 = {1973: 0, 1990: 1, 1992: 2}
    dict2 = {1961: 3, 2011: 4, 1985: 5}
    dict3 = {1961: 6, 2011: 7, 1985: 8}
    dict4 = {1965: 9, 2009: 10}
    if args[0] == 'SCSS':
        return 12
    elif args[0] == 'EC':
        if args[2] == 1992:
            return 11
        elif args[2] == 1990:
            return dict4.get(args[3])
        else:
            return dict3.get(args[1])
    else:
        if args[3] == 2009:
            return dict2.get(args[1])
        else:
            return dict1.get(args[2])
