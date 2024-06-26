dict={
    'Course':'Python',
    'fee':8000,
    'experience':'2 months',
    'timing':'4 hours',
    'shift':'night'
}

print("key values of dictionary are:")
for x,y in dict.items():
    print(x,y)

#Deleting using del keyword
del dict['shift']
print("After deleting 'shift' item Dictionary is ",dict)

#Deleting using pop() function
print("Deleting 'timing' item in dictionary using pop().")
x=dict.pop('timing')
print("Popped item of dictionary is :",x)
print(dict)

#Updating
print("After changing fee to 10000 dict is :")
dict['fee']=10000
print(dict)