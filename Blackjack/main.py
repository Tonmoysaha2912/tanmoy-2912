from game import *
from setting import *

bold = "\033[1m"
flag = 1


if __name__ == "__main__":
    print(bold + "Welcome to BlackJack Area \nStart the game \nYou have total 3000\n" + bold)
    total = 3000

    while total > 0:

        bet = Betting(total)
        bet.get_amount()
        pg = PlayGame()

        if not(bet.deal_amount == 0):
            print(bold+f"Your bet amount is {bet.deal_amount}"+bold)
            print(bold+"Lets begin\n========================================================"+bold)
            pg.start_game()
            pg.display("user")

        else:
            exit(bold + "Game is Over" + bold)

        while True:

            print("Do you want to hit or stand?")
            user_input = input()
            if user_input.lower() == "hit":
                pg.hit_action("user")
                user__curr_total = pg.check_score("user")
                if user__curr_total > 21:
                    flag = 0
                    break

            elif user_input.lower() == "stand":
                break
            else:
                print("Please enter the correct choice within \"hit\"or\"stand\" ")
                continue

        if flag == 0:
            pg.display()
            print("Game Blast! you have lost the bet")
            total = total - bet.deal_amount
        else:

            while pg.check_score("computer") < 17:
                if pg.compare_score() == "computer":
                    pg.display()
                    print("Dealer won! you have lost the bet.")
                    total = total - bet.deal_amount
                    break
                else:
                    pg.hit_action("computer")
            else:
                if 17 <= pg.computer_total <= 21:
                    pg.display()
                    winner = pg.compare_score()
                    if winner == "computer":
                        print("Dealer won. You have lost the bet.")
                        total = total - bet.deal_amount
                    elif winner == "user":
                        print("You won the bet.")
                        total = total + bet.deal_amount
                    else:
                        print("Game Tie you have keep the bet.")

                else:
                    print("Game Blast! you have won the bet")
                    total = total + bet.deal_amount

        print(f"Do you continue,Yes or No with balance {total}")
        if input().upper() == "NO":
            print(f"you have {total}")
            break
        else:
            continue

    else:
        print("You don't have balance")
