def main(x):
    dict1 = {'RUBY': 1, 'QML': 2, 'LFE': 3}
    dict2 = {1980: 6, 2001: 7}
    dict3 = {1980: 8, 2001: 9}
    dict_m = {'QML': dict2, 'LFE': dict3}
    if x[3] == 1989:
        return 10
    if x[3] == 2019:
        return 11
    if x[1] == 1982:
        return 4
    elif x[1] == 1986:
        if x[0] == 1980:
            return 0
        else:
            return dict1.get(x[4])
    else:
        if x[4] == 'RUBY':
            return 5
        else:
            return dict_m[x[4]].get(x[0])


# print(main([1980, 1986, 1992, 1989, 'QML']))
# print(main([2001, 1986, 1976, 2019, 'RUBY']))
# print(main([1980, 1982, 1992, 1980, 'QML']))
# print(main([2001, 1986, 1992, 1980, 'QML']))
# print(main([2001, 2007, 1992, 1980, 'RUBY']))
print(main([1980, 2007, 1976, 1980, 'LFE']))