# Tuples are immutable
# Elements in a tuple are accessed using indexing
x=(2)
print(type(x))  #Single element is not considered as Tuple
students=("Yeshiv sahu","Shubham verma","Avinash kashyap")
print(students)
print(type(students))
print(students[1])
print(students[0])

print("Iterating tuple elements:")
#Iteration
for x in students:
    print(x)

print("Using range function:")
for x in range(len(students)):
    print(students[x])