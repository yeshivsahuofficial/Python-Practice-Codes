#Checking For Palindrome String
def is_palindrome(str1):
    rev=str1[::-1]
    if(rev==str1):
        print(f"{str1} is Palindrome.")
    else:
        print(f"{str1} is NOT Palindrome.")

is_palindrome("Yeshiv")
is_palindrome("BABA")
is_palindrome("Mom")
is_palindrome("MOM")
is_palindrome([1,2,1])
is_palindrome((1,2,3,3,2,1))