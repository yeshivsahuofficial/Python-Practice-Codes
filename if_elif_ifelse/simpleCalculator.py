x=int(input("Enter number 1:"))
y=int(input("Enter number 2:"))
operand=input("Enter valid operand(+,-,*,/):")

if(operand=='+'):
    print(x+y)
elif(operand=='-'):
    print(x-y)
elif(operand=='*'):
    print(x*y)
elif(operand=='/'):
    print(x/y)
else:
    print("Invalid Operand!")
    print("Please refresh and enter valid Operand")