# Bitwise operators are used to perform operations on integers at the binary level
"""
1.Bitwise AND (&):
    Sets each bit to 1 if both bits are 1.
2.Bitwise OR (|):
    Sets each bit to 1 if at least one of the corresponding bits of either operand is 1.
3.Bitwise XOR (^):
    Sets each bit to 1 if only one of the corresponding bits of its operands is 1.
4.Bitwise NOT (~):
    Inverts all the bits.
5.Left Shift (<<):(x<<2) Shifts two times left
    Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
6.Right Shift (>>):
    Shifts the bits of the left operand to the right by the number of positions specified by the right operand.
"""
x=10
y=8

print(f"Binary of {x} is ",bin(x))
print(f"Binary of {y} is ",bin(y))

#Bitwise '&'(and) Operator
print("Value of x&y is",bin(x&y),x&y)

#Bitwise '|'(or) Operator
print("Value of x|y is",bin(x|y),x|y)

#Bitwise '^'(XOR) Operator
print("Value of x^y is",bin(x^y),x^y)

#Bitwise '~'(NOT) Operator
print("Value of ~y is",bin(~y),~y)

#Bitwise '<<'(Left Shift) Operator
print("Value of x<<1",bin(x<<1),x<<1)

#Bitwise '>>'(Right Shift) Operator
print("Value of x>>1",bin(x>>1),x>>1)

#To Left or Right shift a Negative Number(ex-(-5)) Steps are:
    # 1. First take binary of 5 - 0101
    # 2. Take one's complement -   1010(Flip 1 to 0 and 0 t0 1)
    # 3. Add 1 to one's complement - 1011(This is binary of '-5''
    # 4.  Now left shift above binary we get answer

y=-5
print(f"Binary of {-5} is",bin(-5))

print(f"Value of y<<1",bin(y<<1),y<<1)