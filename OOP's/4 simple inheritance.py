# INHERITANCE ---Inherits the properties and behaviors(methods and attributes)
# of another class(called a superclass or base class ).

class A:
    def methodA(self):
        print("Welcome to class A.")
class B(A):
    def methodB(self):
        print("Welcome to class B.")

obj=B()
obj.methodB()
obj.methodA()

