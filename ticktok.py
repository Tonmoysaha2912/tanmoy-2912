import os
import random as ran



def display(temp):
    print("  |   |  ")
    print(temp[7], "|", temp[8], "|", temp[9])
    print("--|---|--")
    print(temp[4], "|", temp[5], "|", temp[6])
    print("--|---|--")
    print(temp[1], "|", temp[2], "|", temp[3])
    print("  |   |  ")


def user_choice(pl1_name):
    print("Enter enter your choice {}, X or O".format(pl1_name))
    user_input = input()
    player1 = user_input.upper()
    if player1 == 'X' or player1 == 'O':
        player2 = 'O' if player1 == 'X' else 'X'
        return player1,player2
    else:
        print("You enter wrong Choice.")
        player1, player2 = user_choice(pl1_name)
        return player1, player2


def first_choice():
    return ran.randint(1,2)


def fetch_input(pval, name):

    res_list = list(set(num_list).intersection(set(temp_list)))
    print(f"{name} : Enter your choice where you marked 1-9")
    val = int(input())

    if val in res_list or val not in (list(range(1,10))):
        print(f"{val} position is not available")
        return False
    else:
        temp_list.append(val)
        list1[val] = pval
        return True


def board_check(board):
    char = ' '
    if char in board[1:]:
        return True
    else:
        return False


def check_player(pl1, pl2, pl1_name, pl2_name):

    p_flag = 1

    while board_check(list1):
        if ticktok_match == 'no':
            if p_flag == 1:
                if fetch_input(pl1, pl1_name):
                    check_ticktac()
                    p_flag = 0
                else:
                    p_flag = 1

            else:
                if fetch_input(pl2, pl2_name):
                    p_flag = 1
                    check_ticktac()
                else:
                    p_flag = 0
        else:
            display(list1)
            print(f"The winner is {pl1_name}") if p_flag == 0 else print(f"The winner is {pl2_name}")
            break

    else:
        display(list1)
        print("Tie Match")


def check_ticktac():

    if check_row() == True or check_col() == True or check_diagonal() == True:
        global ticktok_match
        ticktok_match = 'yes'
    else:
        os.system('cls')
        display(list1)


def check_row():
    for i in range(1, 10, 3):
        if list1[i] == list1[i+1] and list1[i] == list1[i+2] and list1[i] != ' ':
            return True
    else:
        return False


def check_col():
    for i in range(1, 4, 1):
        if list1[i] == list1[i + 3] and list1[i] == list1[i + 6] and list1[i] != ' ':
            return True
    else:
        return False


def check_diagonal():
    if left_diagonal() == True or right_diagonal() == True:
        return True
    else:
        return False


def left_diagonal():
    i = 1
    if list1[i] == list1[i + 4] and list1[i] == list1[i + 8] and list1[i] != ' ':
        return True
    else:
        return False


def right_diagonal():
    i = 3
    if list1[i] == list1[i + 2] and list1[i] == list1[i + 4] and list1[i] != ' ':
        return True
    else:
        return False


print("Welcome to Tik tac toe Game \nThe pattern should be like below")
display(list(range(10)))
print("Enter your name for player 1")
player1_name = input()
print("Enter your name for player 2")
player2_name = input()

while True:

    print("Shall start the game : Yes or no")
    usr_input = input()

    if usr_input == "yes":
        ticktok_match = 'no'
        list1 = [' ']*10
        temp_list = []
        num_list = list(range(1, 10))
        first_player = first_choice()
        if first_player == 1:
            player1 = player1_name
            player2 = player2_name
        else:
            player1 = player2_name
            player2 = player1_name

        player1_choice, player2_choice = user_choice(player1)
        check_player(player1_choice, player2_choice, player1, player2)
        print("Do you want to play again? yes or no")
        user_reply = input()
        if user_reply == 'yes':
            continue
        elif user_reply == 'no':
            break
        else:
            exit("Sorry you enter wrong input")
    else:
        exit("Thank You")

print("Thank you for participating")




