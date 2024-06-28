# user-defined function is a block of organized, reusable code that performs a specific task
def s(argument1, argument2):
    # Function body
    result = argument1 + argument2
    return result   # Return the result

output = s(3, 5)    # Call the function 's' with arguments
print("Result:", output)  # Output: Result: 8

# The def keyword is used to define a function named "s".
# Parameters (argument1 and argument2 in the function s definition)
#     are placeholders for the values that will be passed into the function.
# Arguments (3 and 5 in s(3, 5))
#     are the actual values that are passed into the function when it is called.