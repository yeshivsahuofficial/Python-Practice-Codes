# There are two Identity Operators : 'is' , 'is not'
# It is a comparison operator in Python, used to determine whether two variables refer to the same object in memory.

#'is' Operator
str1 = "Yeshiv"
str2 = "Yeshiv"
str3 = "yeshiv"

print(str1 is str2)
print(str2 is str3)

#'is not'
print(str1 is not str2)
print(str2 is not str3)