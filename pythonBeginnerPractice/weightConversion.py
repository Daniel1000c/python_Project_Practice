# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

# Create if statement to check if unit is K or L

if unit == "K":
    weight = round(weight * 2.205,2)
    unit = "lbs."
    print(f"Your weight is: {weight} {unit}")
elif unit == "L":
    weight = round(weight / 2.205,2)
    unit = "Kgs."
    print(f"Your weight is: {weight} {unit}")
else:
    print(f"{unit} is not a valid conversion!!")
    