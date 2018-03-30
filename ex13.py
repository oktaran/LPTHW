from sys import argv
# read the WYSS section for how to run this
# _, first_name, last_name, city = argv

# print("The script is called:", script_name)

# print("Your first name is: ", first_name)
# print("Your last name is: ", last_name)
# print("You live in: ", city)
# year_of_birth = input("You were born in: ")

_, n1, n2, n3 = argv

# print(n1)
# print(n2)
# print(n3)

# total = int(n1) + int(n2) + int(n3)
# print("Total: ", total)

num = input("Input your number: ")

print(
    "The sum of typed in number with three numbers above is: ",
    int(n1) + int(n2) + int(n3) + int(num)
)
