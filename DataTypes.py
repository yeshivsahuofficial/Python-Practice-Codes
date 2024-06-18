# Numeric Types:    1.int   2.float:
x=54        #int
y=534.45    #float
print(f"Value of x is {x}")
print(f"Value of y is {y}")

# Boolean Type:     1.bool: Represents truth values, True or False.
                            # Example 1: Assigning boolean values to variables
is_raining = True
is_sunny = False
print(is_raining)  # Output: True
print(is_sunny)    # Output: False
                            # Example 2: Using boolean operators
x = 10
y = 5
is_greater = x > y            # True, because 10 is greater than 5
is_equal = x == y             # False, because 10 is not equal to 5
is_less_or_equal = x <= y     # False, because 10 is not less than or equal to 5

print(x>y)          # Output: True
print(x==y)         # Output: False
print(x<=y)         # Output: False

# Sequence Types(Indexed):     1.str   2.list    3.tuple
fruits_list = ["apple", "banana", "cherry", "date"]     # List
numbers_tuple = (1, 2, 3, 4, 5)     #Tuple
greeting_string = "Hello, Python!"  #String
print(fruits_list[0])       # Output: apple
print(numbers_tuple[2])     # Output: 3
print(greeting_string[7:])  # Output: Python!

# Mapping Type:     1.dict (Key Value Pair)
person_dict = {             #Dictionary
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person_dict["name"])    # Output: Alice
print(person_dict["age"])     # Output: 30
print(person_dict.get("city", "Unknown"))  # Output: New York

# Set Types:     1.set    2.frozenset
fruits_set = {"apple", "banana", "cherry", "date"}      #Set
print("banana" in fruits_set)   # Output: True
print("orange" in fruits_set)   # Output: False

immutable_set = frozenset([1, 2, 3, 4, 5])

print(immutable_set)  # Output: frozenset({1, 2, 3, 4, 5})
# Attempting to modify a frozenset (immutable)
# immutable_set.add(6)  # This will raise an AttributeError

# None Type:     1.NoneType
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")
greet("Alice")    # Output: Hello, Alice!
greet(None)       # Output: Hello, stranger!
