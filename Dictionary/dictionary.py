# Dictionary represents a collection of key-value pairs.
# Dictionaries are unordered, iterable, and mutable,
# It allows us to store and retrieve values based on keys rather than numerical indexes.
info={"f_Name":"Yeshiv","l_Name":"Sahu","Age":23,"Salary":4500}
print(info)

#Accesing elements
print(info["f_Name"],end="  ")
print(info["l_Name"],end="  ")
print(info["Age"],end="  ")
print(info["Salary"])

#iterating values by for loop
for v in info:
    print(info[v],end="  ")
print()
#updating value using keys
info["Age"]=30
print(info)