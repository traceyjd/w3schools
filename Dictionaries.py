Dicionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Dictionary
# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#
# Dictionaries are written with curly brackets, and have keys and values:
#
# Example
# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
#
# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#
# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
#
# Example
# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
#
# Example
# Print the number of items in the dictionary:
print(len(thisdict))


# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
#
# Example
# String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]

}
print(thisdict)


# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
#
# <class 'dict'>
# Example
# Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
#
# Example
# Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
#
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for
# a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.



# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
#
# Example
# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)



# There is also a method called get() that will give you the same result:
#
# Example
# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)


# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


# Get Values
# The values() method will return a list of all the values in the dictionary.
#
# Example
# Get a list of the values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)


# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
#
# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# Example
# Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
#
# Example
# Get a list of the key:value pairs
x = thisdict.items()


# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
#
# Example
# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
#
# Example
# Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#
# Example
# Add a new item to the original dictionary, and see that the items list gets updated as well:car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
#
# Example
# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

Check if Key
Exists
To
determine if a
specified
key is present in a
dictionary
use
the in keyword:

# Example
# Check if "model" is present in the
# dictionary:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
#
# The argument must be a dictionary, or an iterable object with key:value pairs.
#
# Example
# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
#
# Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
#
# The argument must be a dictionary, or an iterable object with key:value pairs.

# Example
# Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


# Removing Items
# There are several methods to remove items from a dictionary:
#
# Example
# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)



# Example
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

Example
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)



# Example
# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


Example
The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.



# Example
# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


