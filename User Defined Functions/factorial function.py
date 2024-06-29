#Finding Factorial of a number
def fact(n):
    fact=1
    if n==0:
        return 1
    else:
        while(n>=1):
            fact=fact*n
            n-=1
        return fact
n=int(input("Enter any number:"))
answer=fact(n)
print(f"Factorial of {n} is {answer}")
