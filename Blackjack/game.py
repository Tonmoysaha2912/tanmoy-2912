from setting import *
from word2number import w2n


class PlayGame(BlackJack):

    def __init__(self):
        super().__init__()
        self.computer_total = 0
        self.user_total = 0

    def hit_action(self, player_type="user"):

        self.get_cards(player_type)
        self.display(player_type)
        return

    def check_score(self, player_type):
        temp_total = 0
        card_type = self.user_cards if player_type == "user" else self.computer_cards
        for cards in card_type:
            word_num = (cards.split())[0]
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

    def compare_score(self):

        if self.computer_total > self.user_total:
            return "computer"
        elif self.computer_total < self.user_total:
            return "user"
        else:
            return "draw"
