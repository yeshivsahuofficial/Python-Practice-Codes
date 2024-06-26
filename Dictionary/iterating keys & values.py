dict={
    'Course':'Python',
    'fee':'8000',
    'experience':'2 months'
}

print(dict)

#Printing Keys  "dict_name.keys()"
print("1.", dict.keys())

print('2. Printing keys of dictionary using for loop:',end="  ")
for x in dict.values():
    print(f"{x}",end="  ")

#Printing values "dict_name.values()"
print()
print("3.", dict.values())

print('4. Printing keys of dictionary using for loop:',end="  ")
for x in dict.keys():
    print(x,end="  ")

print()
print('''5. Using get() method
Price of fee is ''',dict.get('fee'))   #get('key_name')

#Printing keys and values together using items()
print("6. Printing key & values using items() method:")
for x,y in dict.items():
    print(x,y)