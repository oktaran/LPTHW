name = 'Zed A. Shaw'
age = 35 # not a lie
height_inch = 74 # inches
height_cm = height_inch * 2.54 # cm
weight_lbs = 180 # lbs
weight_kg = weight_lbs * 0.4536 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_inch} inches (or", round(height_cm), "Centimeters) tall.")
print(f"He's {weight_lbs} punds (or", round(weight_kg), "Kilograms) heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total1 = age + height_inch + weight_lbs
total2 = age + height_cm + weight_kg
print(f"If I add {age} (age), {height_inch} (height in inches),"
       "and {weight_lbs} (weight in pounds) I get this number: {total1}.")
print(f"And if I add {age} (age), {height_cm} (height in Centimeters),"
       "and {weight_kg} (weight in Kilograms) I get another one: {total2}.")
