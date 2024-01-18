#Creating Variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the type
x = 5
y = "Jonh"
print(type(x))
print(type(y))

#Single or Double Quotes
x = "John"
# is the same as
x = 'John'


#Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a

# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y)

x = 5
y = "John"
print(x, y)


# Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#The global Keyword
def myfunc():
  global x 
  x = "fantastic"
myfunc()
print("Python is " + x)