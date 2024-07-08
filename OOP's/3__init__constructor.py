class Student:
    college_name="AVC college"              #Class Attribute
    
    #Attribute that is common in class..
    # Doesn't occupy memory as many times is called..
   
    def __init__(self,name,marks):
        self.name=name  #Object Attribute
        self.marks=marks
        print("Adding new student in database:")
    
    def welcome(self):
        print("Hello welcome",self.name)


s1=Student("Aman",65)
print(s1.name,s1.marks,s1.college_name) 

s2=Student("Raj",87)
print(s2.name,s2.marks,Student.college_name)

s1.welcome()