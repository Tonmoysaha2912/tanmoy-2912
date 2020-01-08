from bj import *

bold = "\033[1m"

if __name__ == "__main__":
    print(bold + "Welcome to BlackJack Area \nStart the game \nYou have total 3000\n")
    total = 3000
    while True:
        bet = Betting(total)
        bet.get_amount()
        if not(bet.deal_amount == 0):
            bl = BlackJack()
            bl.start_game()
            bl.primary_display()
            break
        else:
            print(bold + "Game is Over" + bold)
            break

