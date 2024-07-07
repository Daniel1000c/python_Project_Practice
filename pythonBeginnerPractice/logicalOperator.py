# Logical Operators = Used on conditional statements

#   and = checks two or more conditions if True
#   or = checks if at least one condition is True
#   not = True if condition is False, and vice versa

temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("The Temperature is bad")
else:
    print("The Temperature is good")
    
if sunny:
    print("It is sunny outside")
else:
    print("It is cloudy outside")