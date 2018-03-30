import math


def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def main():
    lst = [1, 15, 123, 1000, 88]
    for num in lst:
        # tmpl = "{} -- {}"
        # print("{} -- {}".format(num, square(num)))
        print(num, " -- ", cube(num))

main()
