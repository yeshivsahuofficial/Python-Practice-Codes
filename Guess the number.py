import random

rNumber=random.randint(1,101)
guess=None

while(rNumber!=guess):
    guess=int(input("Enter any number from 1 to 100:"))
    if(guess==rNumber):
        print("Congrats You guesssed the right one!.")
    elif(guess>rNumber):
        print("Your number is too high choose smaller.")
    elif(guess<rNumber):
        print("Your number is too low choose bigger.")
    print()