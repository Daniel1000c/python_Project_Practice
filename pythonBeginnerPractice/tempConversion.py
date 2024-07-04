Unit = input ("Is this temperature in Celsius or Fahrenheit (C/F): ")

temp = float(input("What is the temperature: "))

if Unit == "C":
    temp = round((9 * temp) / 5 + 32,1)
    print(f"The temperature in Fahrenheit is: {temp} F")
elif Unit == "F":
    temp = round((temp - 32) * 5 / 9,1)
    print(f"The temperature in Celsius is: {temp} C")
else: 
    print(f"{Unit} is an invalid unit of measurement")