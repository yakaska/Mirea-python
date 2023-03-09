import re

test_string1 = r'[ <data> set @"arerre_209" =-4948 </data><data>set @"zaen" = -5816 </data> ]'
test_string2 = r'[<data>set @"este_583" = 5840 </data> <data> set @"usbear" = -2370</data> <data>set @"arso_10" = ' \
               r'-1480 </data><data>set @"vesobi"= 2526</data> ]'


def main(string):
    exp = r'@"(\w+)"\s*=\s*(-*\d+)'
    matches = re.findall(exp, string)
    dictionary = {}
    for match in matches:
        key = match[0]
        value = match[1]
        dictionary[key] = value
    return list(dictionary.items())


print(main(test_string1))
print(main(test_string2))
