s={10,20,30,40}
print(f"Set is :{s}")

#add()
s.add(50)
print(f"After adding 50 set is:{s}")

#pop()
x=s.pop()
print(f"After applying pop() set is:{s}")
print(f"Popped element is {x}")

#remove()
s.remove(50)    #If element is not found It shows error
print(f"After removing 50 set is :{s}")

#discard()
s.discard(30)   #If element is not found It doesn't shows error
print(s)

#clear()
s.clear()
print(s)

s={10,20,30,40}
print(f"Set s is: {s}")
t={10,20,50,60,70}
print(f"Set t is :{t}")
s.update(t)
print(f"After merging/updating set t into set s:{s}")