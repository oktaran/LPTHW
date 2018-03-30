i = 0
numbers = []

# while i < 6:
#     # print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

#
# def loop(number, incr):
#     i = 0
#     num_lst = []
#
#     while i < number:
#         print(f"At the top i is {i}")
#         num_lst.append(i)
#
#         i = i + incr
#         print("Numbers now: ", num_lst)
#         print(f"At the bottom i is {i}")
#
# loop(10, 2)


def for_loop(number, incr):
    for i in range(number, incr):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

for_loop(0, 10)


print("The numbers: ")

for num in numbers:
    print(num)
