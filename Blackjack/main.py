from game import *
from setting import *

bold = "\033[1m"
flag = 1
if __name__ == "__main__":
    print(bold + "Welcome to BlackJack Area \nStart the game \nYou have total 3000\n")
    total = 3000

    bet = Betting(total)
    bet.get_amount()
    if not(bet.deal_amount == 0):
        print(bold+f"Your bet amount is {bet.deal_amount}"+bold)
        print(bold+"Lets begin\n========================================================"+bold)
        bl = BlackJack()
        bl.start_game()
        bl.display()

    else:
        print(bold + "Game is Over" + bold)

    pg = PlayGame()

    while True:
        print("Do you want to hit or stand?")
        user_input = input()
        if user_input.lower() == "hit":
            pg.hit_action("user")
            if pg.check_score("user") > 21:
                flag = 0
                break
        elif user_input.lower() == "stand":
            break
        else:
            print("Please enter the correct choice within \"hit\"or\"stand\" ")
            continue
    if flag == 0:
        print("Game Blast! you have lost the bet")



