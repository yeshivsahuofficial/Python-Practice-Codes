class parent:

    def show(self):
        print('hii')

#Inheriting

class child(parent):

    def show(self):
        super().show()#Directly prints parent methods statement
        print('hello')

obj=child()
obj.show()  #prints 'hello' as child method dominates parents method

obj=parent()
obj.show()