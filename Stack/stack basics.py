# Stack is a linear data structure.
# It follows LIFO(Last In /First Out) Principle.
# In Python Stack is implemented using List
l=[]
print(l)
while True:
    c=int(input('''
        1 Push Elements
        2 Pop Elements
        3 Peek Element
        4 Display Stack
        5 Exit
    '''))
    #Push Element
    if(c==1):
        num=int(input("Enter the value:"))
        l.append(num)
        print(l)
    #Pop Element
    elif(c==2):
        if(len(l)==0):
            print("Empty Stack")
        else:
            x=l.pop()
            print("Popped Element",x)
            print("After pop stack is:",l)
    #Peek Element
    elif(c==3):
        if (len(l) == 0):
            print("Empty Stack")
        else:
            print("Peek value of Stack is:",l[-1])
            print(l)
    #Display Elements of Stack
    elif(c==4):
        print("Stack is ", l)
    elif(c==5):
        break;
    else:
        print("Please enter valid operation.")