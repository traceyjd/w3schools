x = 4 # Set to int
print("The value of x is:", x)

x = "Sally" # set to string
print("The value of x is:", x)

x = "Sally" # set to string
print("The value of x is:", x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal variable names
2myvar = "John"
my-var = "John"
my var = "John"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)
print(y)
print(z)

# The following will assign Orange to x y and z
x = y = z = "Orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#  Print command
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma: