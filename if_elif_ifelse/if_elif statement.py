#Grading based on Students Percentage

percent=int(input("Enter your percentage :"))

if(percent>=60):
    print("You got First Division.")
elif(percent>=48):
    print("You got Second Division.")
elif(percent>=30):
    print("You got Third Division.")
else:
    print("You have Failed..")
