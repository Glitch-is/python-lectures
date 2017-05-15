#!/usr/bin/python


# A. extract
# On a graduation diploma, the grades for a given subject are given as the table below shows.
#
# Námsgrein	Áfangar	Einkunnir	Einingar
# …	…	…	…
# Efnafræði	EFN 1036 2036 3036 4036 4136  	M 10 8 7 S    	18
# …	…	…	…
# Suppose you are given a text files that contain the result of passing diplomas through an OCR engine. OCR engines take an image, containing text, and try to convert it to a text document. This process can be inaccurate. E.g., it is can be hard for OCR engines to recognize the difference between 1 and l, O and 0, and so forth.
#
# In this problem, we assume we have been able to extract the part of each line that contains the grades. The only grades that can appear on a diploma are the integers from 4 to 10 (inclusive) and the letters S and M. The grade string you obtain, however, is not necessarily properly formatted. Spaces may have been removed or added, 0 could have been read as O, 1 as l and S as s. Furhtermore, the string could contain ‘noise’, such as hyphens, dots and commas.
#
# Write a function extract that takes a string of grades, from an OCR engine, and returns a list of strings containing the grades of the string. However, if the string contains illegal characters, or it is impossible to split the string up into grades (with the noise removed, and all misread characters corrected), the function should return None.
def extract(s):
    # +++your code here+++
    return

# B. count_names
# Statistics Iceland (Hagstofa Íslands) provides data on how many Icelandic citizens have a given first and middle name (see https://hagstofa.is/talnaefni/ibuar/faeddir-og-danir/nofn/).
# 
# The complete data is provided as a JSON file, nofn.json. The data are represented with a list of objects, one object for each name. Each object contains three keys, Nafn, Fjoldi1 and Fjoldi2. The key Nafn provides the name that object represents, Fjoldi1 gives the number of citizens that have the specified name as a first name, and Fjoldi2 the number that have that name as a middle name.
# [
#   ...
#   {
#     "Nafn": "Linddís",
#     "Fjoldi1": 1,
#     "Fjoldi2": 1
#   },
#   {
#     "Nafn": "Damjan",
#     "Fjoldi1": 5,
#     "Fjoldi2": 0
#   },
#   {
#     "Nafn": "Bjarki",
#     "Fjoldi1": 915,
#     "Fjoldi2": 475
#   },
#   {
#     "Nafn": "Þórhildur",
#     "Fjoldi1": 374,
#     "Fjoldi2": 38
#   },
#   ...
# ]
# Write a function function count_names that takes one string, start as a parameter. The function returns a tuple (a, b) where a and b are the numbers of citizens that have a first and middle name that starts with the string start, respectively.
def count_names(start):
    # +++your code here+++
    return


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('extract')
    test(extract('10s M8'), [ '10', 'S', 'M', '8' ])
    test(extract('1 0894l0'), [ '10', '8', '9', '4', '10' ])
    test(extract('5.4-9'), [ '5', '4', '9' ])
    test(extract('398 4'), None)

    print()
    print('count_names')
    test(count_names('Bja'), (3267, 1494))
    test(count_names('Wat'), (8, 2))
    test(count_names('Snati'), (0, 0))


if __name__ == '__main__':
    main()
