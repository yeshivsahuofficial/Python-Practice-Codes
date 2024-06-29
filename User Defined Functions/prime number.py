#   Prime number is a number which has exactly 2 divisors i.e., 1 and itselff.
#   If n is less than or equal to 1, it is not prime.
#   If n is 2, it is prime (since 2 is the smallest and only even prime number).
#   Even numbers are not prime(except for 2 itself).
def is_prime(n):
    if(n<=1):
        return print(f"{n} is NOT a Prime number")
    elif(n==2):
        return print(f"{n} is a Prime number")
    elif(n%2==0):
        return print(f"{n} is NOT a Prime number")
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                return print(f"{n} is NOT a prime number.")
                break
        else:
            return print(f"{n} is Prime number.")

n=int(input("Enter any number:"))
is_prime(n)
