l=[23,46,87,35,53,96]

#Count() Checks the number of occurence of an element
print(l.count(46))

#Max()
print(max(l))

#Min()
print(min(l))

#Sort()
print(f"Before sorting list l is {l}")
l.sort()
print(f"After sorting list l is {l}")

#Reverse()
print(l)
l.reverse()
print(f"After using reverse to list l it is f{l}")

#index()
print(l.index(35))