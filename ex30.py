people = 30
cars = 20
trucks = 50


if cars > people:                       # if Boolean expression is True then -->
    print("We should take the cars.")   # print
elif cars < people:                     # if another Boolean expression is True
    print("We should not take the cars.")
else:                                   # if none from above expression is True
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks or trucks > cars:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
