'''
    range(start,stop,step)
    start (optional): Starting number of the sequence (default is 0).
    stop (required): Generate numbers up to, but not including, this number.
    step (optional): Difference between each number in the sequence (default is 1).
'''

# Using range(stop)
for x in range(6):
    print(x,end="  ")
print()
# Using range(start, stop)
for x in range(1,6):
    print(x,end="  ")
print()
# Using range(start, stop, step)
for x in range(1,11,2):
    print(x,end="  ")
print()