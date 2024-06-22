#Updation
l1=[23,454,86,424,75,86,57]
l2=[]
for i in range(len(l1)):
    l2.append(l1[i])
print(f"List l2 is {l2}")

#COMPREHENSION - A concise way to write the code

l3=[x for x in l1]
print(f"List l3 is {l3}")

l4=[i for i in range(2,21,2)]
print(f"List l4 is {l4}")

l5=[i for i in range(2,21,2) if i%2==0]
print(f"List l5 is {l5}")
