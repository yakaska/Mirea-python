import re

test_string = r"||<sect> data array( @'cebi_815'; @'geso'; @'usla_563' ) to q(dite_207);</sect>;<sect> data array( @'zaatus_229' ; @'ave'; @'enre' )to q(raat); </sect>;||"


def main(string):
    exp = r"array\(\s@'(\w+)'\s*;\s@'(\w+)';\s@'(\w+)'\s\)\s*to\sq\((\w+)"
    matches = re.findall(exp, string)
    dictionary = {}
    for match in matches:
        key = match[3]
        values = match[:3]
        dictionary[key] = values
    return list(dictionary.items())


print(main(test_string))
