#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.


# A. mod_sum
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Implement the function mod_sum(n) that takes an integer as parameters
# and returns the sum of all multiples of 3 or 5 below n.
# So mod_sum(10) returns 23.
def mod_sum(n):
    # +++your code here+++
    return


# B. remove_empty
# Implement the function remove_empty that takes a list of strings and
# returns the same list, where empty strings have been removed.
# So remove_empty(['python', '', 'is', 'awesome', '']) returns
# ['python', 'is', 'awesome']
def remove_empty(l):
    # +++your code here+++
    return


# C. reverse_words
# Implement the function reverse_words(words) that takes a string as a
# parameter. The string contains a single line (i.e. the string contains no \n).
# The function returns the string s, where the order of the words
# in the string have been reversed. The words are separated by single space.
# So reverse_words('in theory there is no difference between theory and practice')
# returns 'practice and theory between difference no is there theory in'
def reverse_words(words):
    # +++your code here+++
    return


# D. duplicates
# Implement the function duplicates(s) that takes a list of numbers or
# strings and returns a list containing all the elements that
# appear more than once in the list (duplicates).
# So duplicates([1337, 42, 5318008, 1337, 5318008, 5885522])
# returns [1337, 5318008]
def duplicates(s):
    # +++your code here+++
    return


# E. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    # +++your code here+++
    return


# F. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
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
    print('mod_sum')
    test(mod_sum(10), 23)
    test(mod_sum(20), 78)
    test(mod_sum(50), 543)

    print()
    print('remove_empty')
    test(
         remove_empty(['python', '', 'is', 'awesome', '']),
         ['python', 'is', 'awesome'])
    test(
         remove_empty(['', 'hello', 'world']),
         ['hello', 'world'])
    test(
         remove_empty(['learning', 'is', '', '', 'fun']),
         ['learning', 'is', 'fun'])

    print()
    print('reverse_words')
    test(
        reverse_words('hello world'),
        'world hello')
    test(
        reverse_words('python is so awesome'),
        'awesome so is python')
    test(
        reverse_words('in theory there is no difference between theory and practice'),
        'practice and theory between difference no is there theory in')

    print()
    print('duplicates')
    test(duplicates([1, 1]), [1])
    test(duplicates([1, 2, 3]), [])
    test(
         duplicates([1337, 42, 5318008, 1337, 5318008, 5885522]),
         [1337, 5318008])

    print()
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(
        front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(
        front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(
        front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


if __name__ == '__main__':
    main()
