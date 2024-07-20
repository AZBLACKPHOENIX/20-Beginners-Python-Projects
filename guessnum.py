#Import random
import  random as ran
#Declare the value for hidden number
value = ran.randint(0, 10)
#Prompt user
compprompt = input("Would You Like To Play With Me\n Enter Yes To Play With Computer Or No To Play Alone:")

#Use if statement
if compprompt=="Yes":
    #Use while loop to play the game until the user or com gets the correct value
    while (True):
        response = [
            "I lost",
            "I didn't get that",
            "I'll get it next time",
            "Damn! This might be your play",
            "I lost again",
            "Better luck next time for me",
            "Missed it this time",
            "I'll nail it next round",
            "You got this one!",
            "Oops, I lost once more"
        ]

        res_choice = ran.randint(0, 9)
        lost_comp_res = response[res_choice]
        compinput =ran.randint(1, 10)
        if compinput == value:
            comp_turn =1
            print("Computer :I won " + "Hidden Number Is ", value)
            break
        else:
            print("Conmputer:" +lost_comp_res, " My Guess Number Is ", compinput)
            comp_turn = 0
            user = int(input("Ente Your Number:"))
            if user == value:
                print("You won")
                break
            else:
                continue
else:
    while (True):
        user = int(input("Guess The Number:"))
        if (user == value):
            print("You Got It")
            break
        else:
            if user < value:
                print("Try Again The Value Is Greater Than Your Input")
            else:
                print("Try Again The Value Is Less Than Your Input")
            continue

