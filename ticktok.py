import os


def display(temp):
    print(temp[7], "|", temp[8], "|", temp[9])
    print("-|--|-")
    print(temp[4], "|", temp[5], "|", temp[6])
    print("-|--|-")
    print(temp[1], "|", temp[2], "|", temp[3])


def user_choice():
    print("Enter enter your choice X or O")
    user_input = input()
    player1 = user_input.upper()
    player2 = 'O' if player1 == 'X' else 'X'
    return player1, player2


def fetch_input(pval, name):

    res_list = list(set(num_list).intersection(set(temp_list)))
    print(f"{name} : Enter your choice where you marked 1-9")
    val = int(input())
    if val in res_list:
        print(f"{val} position is already taken")
        return False
    else:
        temp_list.append(val)
        list1[val] = pval
        return True


def check_player(pl1, pl2):

    p_flag = 1

    while ticktok_match == 'no':
        if p_flag == 1:
            if fetch_input(pl1, "Player 1"):
                check_ticktok()
                p_flag = 0
            else:
                p_flag = 1

        else:
            if fetch_input(pl2, "Player 2"):
                p_flag = 1
                check_ticktok()
            else:
                p_flag = 0


    else:
        display(list1)
        print(f"The winner is Player 1") if p_flag == 0 else print(f"The winner is Player 2")


def check_ticktok():

    if check_row() == True or check_col() == True or check_diagonal() == True:
        global ticktok_match
        ticktok_match = 'yes'
    else:
        os.system('cls')
        display(list1)


def check_row():
    for i in range(1, 10, 3):
        if list1[i] == list1[i+1] and list1[i] == list1[i+2] and list1[i] != '':
            return True
    else:
        return False


def check_col():
    for i in range(1, 4, 1):
        if list1[i] == list1[i + 3] and list1[i] == list1[i + 6] and list1[i] != '':
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
    if list1[i] == list1[i + 4] and list1[i] == list1[i + 8] and list1[i] != '':
            return True
    else:
        return False


def right_diagonal():
    i = 3
    if list1[i] == list1[i + 2] and list1[i] == list1[i + 4] and list1[i] != '':
        return True
    else:
        return False


print("Welcome to Tiktok Game \nThe pattern should be like below")

display(list(range(10)))
print("Shall start the game : Yes or no")
usr_input = input()

if usr_input == "yes":
    ticktok_match = 'no'
    list1 = ['']*10
    temp_list = []
    num_list = list(range(1, 10))
    player1_choice, player2_choice = user_choice()
    check_player(player1_choice, player2_choice)
    check_ticktok()
else:
    exit("Thank You")





