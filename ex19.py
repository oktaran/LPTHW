def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# ______________________________________________________________________

# def my_sweets(chocolate, apple_pie, candy):
#     print(f"So, today you've had {chocolate} chocolate(s), {apple_pie} piece(s)"
#            " of apple pie and {candy} candy(s).")
#     print("Let's count how many calories you've got!")
#
#
# input("Tell me the truth :)\nHave you eaten chocolate today? > ")
# chocolate = input("How many? > ")
# apple_pie = input("How many apple pies? > ")
# candy = input("Candies (if any)? > ")
#
# my_sweets(chocolate, apple_pie, candy)
#
# chocolate_cal = int(chocolate) * 540
# apple_pie_cal = int(apple_pie) * 150
# candy_cal = int(candy) * 100
#
# total_cal = chocolate_cal + apple_pie_cal + candy_cal
#
# print(f"It's about {total_cal} extra calories!"
#        "You should have a lot of physical training today!")

# _______________________________________________________________________

def hello(greeting, name):
    print(f"{greeting}, {name}!")

# hello("Hola", "Oksana")               # 1

# greeting = "Privet"                   # 2
# name = "Oksana"
# hello(greeting, name)

# greeting = input()                      # 3
# name = input("What's your name? ")
# hello(greeting, name)

# hello(greeting="Yay!", name="Oksa")
