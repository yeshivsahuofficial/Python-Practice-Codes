name="My name is Yeshiv Sahu"

#fing(char) "Returns Index number of Char"
print(name.find("Y"))
print(name.find("z")) #If it does not find the character it returns -1
print(name.find("Y",2))
#'2': This parameter specifies the starting index from where the search should begin.

#index(char) is same as find but if a char is not found it gives error instead of -1.
print(name.index("Y"))
# print(name.index("z"))    ERROR

#isalpha() checks the given input is complete string and returns True
x="yeshiv "
y="yeshiv"
print(x.isalpha())  #whitespace shows error
print(y.isalpha())

#isdigit() checks complete string is numeric
x="yeshiv123"
y="yeshiv "
z="1234"
print(x.isdigit())
print(y.isdigit())
print(z.isdigit())
