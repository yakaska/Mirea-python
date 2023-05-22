import re

test_string1 = r'<sect><sect> make raqu<== q(isorso_759); </sect>. <sect> make tiarus <== q(teorri_934); </sect>. ' \
               r'<sect> make arla_424 <== q(qube); </sect>.</sect>'
test_string2 = r'<sect> <sect> make inan_51 <== q(ququar_617); </sect>. <sect> make engeen_725 <== q(' \
               r'esma_229);</sect>. <sect> make isre <== q(xeaner); </sect>. <sect> make leance <==q(' \
               r'qudice_376);</sect>.</sect>'


def main(string):
    exp = r'make\s*(\w+)\s*<==\s*q\((\w+)'
    matches = re.findall(exp, string)
    dictionary = {}
    for match in matches:
        key = match[0]
        value = match[1]
        dictionary[key] = value
    return list(dictionary.items())


print(main(test_string1))
print(main(test_string2))
