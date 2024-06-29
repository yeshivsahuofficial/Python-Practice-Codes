#
def fibo(n):
    a,b=0,1
    if(n==1):
        return 0
    fibonacci_series=[a,b]
    for i in range(2, n + 1):
        a, b = b, a + b
        fibonacci_series.append(b)
    return fibonacci_series

n=int(input("Enter any number: "))
series=fibo(n)
print(f"Fibonacci Series of {n} is : {series}")