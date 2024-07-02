'''(JavaScript Object Notation) is a data format used for exchanging info. b/n applications and
storing data in a human-readable and machine-processible way.
It's based on key-value pairs and nested structures,
making it versatile for representing various data types.'''

import json

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Check the type of 'data' (it's a dictionary)
print(type(data))

# Convert dictionary to JSON string with indentation for readability
json_string = json.dumps(data, indent=4)
print(json_string)

# Check the type of 'json_string' (it's a string)
print(type(json_string))



#Convertin json file to python obj
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Check the type of 'data' (it's a dictionary)
print(type(data))

# Convert dictionary to JSON string with indentation for readability
json_string = json.dumps(data, indent=4)
print(json_string)