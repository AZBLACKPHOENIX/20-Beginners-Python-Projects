import random as ran

game_count=0
com_win=0
user_win=0
while True:
    rps = ["Rock", "Paper", "Scissors"]
    comp_num = ran.randint(0,2)
    comp_choice = rps[comp_num]
    user_number = int(input("Enter 0:Rock 1:Paper 2:Scissors ::"))
    user_choice = rps[user_number]
    if user_number == comp_num:
        print("computer:", comp_choice)
        print("Draw")
    elif (user_number == 0 and comp_num == 1) or (user_number == 2 and comp_num == 0) or (user_number == 1 and comp_num == 2):
        print("computer:", comp_choice)
        print("Computer Win")
        com_win += 1
    else:
        print("computer", comp_choice)
        print("You Win")
        user_win += 1
    game_count += 1
    if game_count == 5:
        if com_win < user_win:
            print("Com Score:", com_win, "\nYour Score:", user_win)
            print("You Won")
        else:
            print("Com Score:", com_win, "\nYour Score:", user_win)
            print("Computer Win")
        break