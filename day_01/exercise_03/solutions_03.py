#!/usr/bin/python


# A. top_3
# Given a dictionary "items" which contain items that can be bought
# in a shop along with their price, can you get the top three most
# expensive items in the shop?
# Give your answer as a list with the names of the most expensive
# items in the order of most expensive first.
# So top_3({'ham': 1, 'eggs': 2, 'milk': 3}) returns ['milk', 'eggs', 'ham']
def top_3(items):
    # +++your code here+++
    products = list(items.items())
    products.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in products][:3]


# B. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    tuples.sort(key=lambda x: x[1])
    return tuples


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
    print('top_3')
    test(top_3(
        {'ham': 13,
         'eggs': 29,
         'milk': 10,
         'bread': 15,
         'butter': 5,
         'steak': 40}),
         ['steak', 'eggs', 'bread'])
    test(top_3(
        {'A': 2,
         'B': 1,
         'C': 4,
         'D': 3}),
         ['C', 'D', 'A'])

    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    test(
        sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3),
                                                         (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
