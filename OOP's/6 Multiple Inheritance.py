class A:
    def methodA(self):
        print("Welcome to class A.")
class B:
    def methodB(self):
        print("Welcome to class B.")
class C(A,B):
    def methodC(self):
        print("Welcome to class C.")


obj=C()
obj.methodA()
obj.methodB()
obj.methodC()