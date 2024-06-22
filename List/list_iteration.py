list1=[1,22,43,65,75,23,98,94]
length=len(list1)
print(length)
list2=[]
#Simple for loop
for i in list1:
    print(i,end="  ")
print()

#using for loop with range
for i in range(len(list1)):
    print(list1[i],end="  ")
print()

