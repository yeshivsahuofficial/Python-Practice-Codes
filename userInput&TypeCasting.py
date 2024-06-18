#BY DEFAULT THE INPUT TAKEN BY USER IS 'STRING'
X=input("Enter the value:-")
print(X,type(X))
#String Input
name=str(input("Enter your first name:"))
print(f"Your name is {name}")

#Float input
length=float(input("Enter the length of Rectangle:"))
breadth=float(input("Enter the breadth of Rectangle:"))

Area=length*breadth
print(f"Area of Rectangle is {Area}")

#Integer input
Age=int(input("Enter your Age:"))

print(f"You entered your age as {Age}")

#"eval"
result = eval('3 + 5')
print(result)  # Output: 8

x = 10
result = eval('x + 5')
print(result)  # Output: 15
