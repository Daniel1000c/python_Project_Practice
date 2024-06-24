 # variable  = a reuseable container for storing a value
 #  a variable behaves as if it were the value it contains
 
age = 21
 
print(age)

print("You are " + str(age) + " years old")

print("You are", age, "years old")

print(f"You are {age} years old")


# Integer
age = 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# float
gpa = 3.2
distance = 2.5
price = 10.99

print(f"Your gpa is {gpa}")
print(f"You ran {distance}Km")
print(f"The price is ${price}")

# string
name = "Bro"
food = "pizza"
email = "bro123@gmail.com"

print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# boolean
online = True
for_sale = False
running = True

print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

if running:
    print("The game is running")
else:
    print("The game is over")
    
x = 1
y = 2
z = 3

print(x)
print(y)
print(z)

x,y,z = 1,2,3

