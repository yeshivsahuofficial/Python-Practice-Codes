# The 'for' loop in Python iterates over elements of a sequence or any iterable object.
# Sequence such as  (list, tuple, string, or range)
# SYNTAX:
# for item in iterable:
     # body of the loop
     # do something with item

#Iterating over a list
list1=[2,4,5,6]
for x in list1:
    print(x,end="  ")
print()

#Iterating over a Range of Numbers
for x in range(6):
    print(x,end="  ")
print()

#Iterating over a String
str="Yeshiv Sahu"
for char in str:
    print(char,end="_")
print()

# Here (10,0,2) Becomes Tuple
# for x in (10,0,2):
#     print(x,end="  ")        Prints:10  0  2

#Reverse Iterating
for num in range(10,0,-1):
    print(num,end="  ")
