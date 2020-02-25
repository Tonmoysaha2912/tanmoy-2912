from setting import *
from word2number import w2n


class PlayGame:

    computer_total = 0
    user_total = 0
    bj = BlackJack()

    def __init__(self):
        pass

    def hit_action(self, player_type="user"):

        self.bj.get_cards(player_type)
        self.bj.display(player_type)
        return

    def check_score(self, player_type):
        temp_total = 0
        for user_cards in self.bj.user_cards:
            word_num = (user_cards.split())[0]
            if not(word_num == "King" or word_num == "Queen" or word_num == "Ace" or word_num == "Jack"):
                temp_total = temp_total + w2n.word_to_num(word_num)
            elif word_num == "King" or word_num == "Queen" or word_num == "Jack":
                temp_total = temp_total + 10
            else:
                if temp_total + 11 > 21:
                    temp_total = temp_total + 1
                else:
                    temp_total = temp_total + 11
        if player_type == "user":
            self.user_total = temp_total
        else:
            self.computer_total = temp_total

        return temp_total
