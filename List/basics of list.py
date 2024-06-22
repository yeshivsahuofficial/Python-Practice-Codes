# List is a collection of items, which can be of different types (including other lists).
# Lists are ordered, mutable (modifiable), and allow duplicate elements.

# Creating an empty list
empty_list = []

# Creating a list with elements of different types
my_list = [1, 2, 'apple', 'banana', True, [3.14, 'orange']]
print(my_list[2:5])
print(my_list[0::2])

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ['apple', 'banana', 'cherry']

# Creating a list of boolean values
booleans = [True, False, True, False]

# Creating a list of lists (nested lists)
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[:])
print(nested_list[1])
print(nested_list[1][0])

list_num=[1,2,3,4,5,6,7,8,9]
print(list_num[:])
print(list_num[-1::-1])
print(list_num[-1::-2])
