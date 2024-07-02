import random

l=["Rock","Paper","Scissor"]

while True:
    Ucount=0
    Ccount=0
    Draws=0
    #Select Start or Exit of Game
    gEnter=int(input('''
Game Start
1 Yes
2 No | Exit
    '''))
    #Game Starts for Input 1
    if(gEnter==1):
        #Loop for 5 games
        for a in range(1,6):
            # Selecting User Input
            print()
            userInput=int(input(f'''Round {a} Please choose one of the below:
1 Rock
2 Paper 
3 Scissor
'''))
            print()
            #Storing User input
            if userInput==1:
                Uchoice="Rock"
            elif userInput==2:
                Uchoice="Paper"
            elif userInput==3:
                Uchoice="Scissor"

            #Computers choice
            Cchoice=random.choice(l)

            #Conditions for win
            if Uchoice==Cchoice:
                print(f"Value of User:{Uchoice}")
                print(f"Value of Computer:{Cchoice}")
                print("Match draw")
                Draws+=1
            elif (Uchoice=="Rock" and Cchoice=="Scissor") or (Uchoice=="Paper" and Cchoice=="Stone") or (Uchoice=="Scissor" and Cchoice=="Paper"):
                print(f"Value of User:{Uchoice}")
                print(f"Value of Computer:{Cchoice}")
                print("You won")
                Ucount+=1
            else:
                print(f"Value of User:{Uchoice}")
                print(f"Value of Computer:{Cchoice}")
                print("Computer won!.")
                Ccount += 1
        #Printing the number of wins of User and Computer
        print()
        print(f"Number of Draws:{Draws}")
        print(f"USER won {Ucount} of 5 and COMPUTER won {Ccount} of 5.")
        print()
        # Final Decision
        if (Ucount == Ccount):
            print("The match was Draw!.")
        elif (Ucount > Ccount):
            print('User Won the Final Game.')
            print('Congratulations and Celebrations.')
        else:
            print("Computer Won the Final Game!")
            print("Better LUCK Next Time")
    else:
        break

