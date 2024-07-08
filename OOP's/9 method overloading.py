class method_overloading:

    # def method1(self):        Shows Error as overloading
    #     print("hello")
    def method1(self):  #upper method is overridden
        print("hii",b)

    def method1(self,x=None):
        print("hello",x)

obj=method_overloading()
obj.method1(5)
obj.method1()