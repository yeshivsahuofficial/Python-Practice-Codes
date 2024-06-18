# Valid VARIABLES
'''
1.Can start with a letter (a-z, A-Z) or underscore (_)
    Ex.=var_name
2.Can contain letters(a - z, A - Z), digits(0 - 9), and underscores(_)
    Ex.=var_1
3.Are case-sensitive
   'myVar' and 'myvar' are treated as different variables.
5.Cannot start with a digit
    Example: 123var is invalid.
6.Can be of any length
    Example: a, my_long_variable_name, _my_variable_name_123

# Invalid Variables
1.Cannot contain special characters
    Examples: var@, var!, var$
2.Cannot start with a digit
    Examples: 123var, 2nd_var
3.Cannot be a reserved word
    Python reserved words(keywords) like if, else, for, etc., cannot be used as variable names.
4.Cannot contain spaces
    Example: my var is invalid; use underscores (my_var) or camelCase (myVar) instead.
5.Cannot be Python built-in functions or modules
    Avoid using names like print,list, str, etc., as variable names, as they are already used by Python.
'''

var_1=10
var_2=50
var_3=10

#Check Memory location of var-1
print(id(var_1))
print(id(var_2))
print(id(var_3))
print("Since the values of Variables var_1 and var_3 are same their Memory location are also same..")
#Since the values of Variables var_1 and var_3 are same their Memory location are also same
