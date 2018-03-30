
"""
Some func problems
~~~~~~~~~~~~~~~~~~

Provide your solutions and run this module.
"""

import math


def add(a, b):
    """Returns sum of two numbers."""
    return a + b


def cube(n):
    """Returns cube (n^3) of the given number."""
    # return n * n * n
    # return n**3
    return math.pow(n, 3)


def is_odd(n):
    """Return True if given number is odd, False otherwise."""
    return n % 2 == 1


def print_nums(num):
    """Prints all natural numbers less than given `num`."""
    for i in range(num):
        print(i)


def print_even(num):
    """Prints all even nums less than a given `num`."""
    for i in range(num):
        if not is_odd(i):
            print(i)


def cube_lst(lst):
    """Returns a list of cubes based on input list."""
    # lst_1 = []
    #
    # for i in lst:
    #     lst_1.append(cube(i))
    #
    # return lst_1

    return [cube(i) for i in lst]

# === Don't modify below ===

def test():
    assert add(3, 2) == 5
    assert add(8, -1) == 7
    assert cube(3) == 27
    assert cube(-1) == -1
    assert is_odd(3)
    assert is_odd(5)
    assert is_odd(11)
    assert not is_odd(2)
    assert cube_lst([1, 2, 5]) == [1, 8, 125]


def main():
    try:
        test()
    except AssertionError:
        print("=== Tests FAILED ===")
    else:
        print("=== Success! ===")


if __name__ == '__main__':
    main()
