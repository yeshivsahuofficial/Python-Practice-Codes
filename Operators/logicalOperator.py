# In Python, logical operators are used to combine conditional statements.
# There are three main logical operators: 'and', 'or', and 'not'.

# 1.'and':
# returns 'True' if both operands are 'True', otherwise it returns 'False'.
x = 5
print(f"{x} > 0 and {x} < 10 is", x > 0 and x < 10)  # True, because both conditions are true
print(f"{x} > 0 and {x} < 10 is", x > 0 and x > 10)  # False, because the second condition is false

# 'or':
# returns 'True' if at least one of the operands is 'True'. If both are 'False', it returns 'False'.
y = 5
print(f"{y} > 0 or {y} > 10", y > 0 or y > 10)  # True, because the first condition is true
print(f"{y} < 0 or {y} > 10", y < 0 or y > 10)  # False, because both conditions are false

# not: The not operator is used to negate the boolean value of a statement.
z = 5
print(not z > 0)  # False, because x > 0 is true, and not False is False
print(not z < 0)  # True, because x < 0 is false, and not True is False
