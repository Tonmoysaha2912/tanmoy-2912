import random as ran


class BlackJack:
	# defining all class variable
	card_type = ['heart', 'spread', 'club', 'diamond']
	card_values = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'King', 'Queen', 'Ace']
	computer_cards = []
	user_cards = []
	computer_total = 0
	user_total = 0

	def __init__(self):
		pass

	def start_game(self):
		BlackJack.get_cards(self, "computer")
		BlackJack.get_cards(self, "user")

	def get_cards(self, player_type):

		for i in range(2):
			temp_card_type = ran.choice(self.card_type)
			temp_card_values = ran.choice(self.card_values)
			temp_value = temp_card_values + " of " + temp_card_type
			self.card_type.remove(temp_card_type)
			self.card_values.remove(temp_card_values)
			if player_type == "computer":
				self.computer_cards.append(temp_value)
			else:
				self.user_cards.append(temp_value)

	def primary_display(self):
		print("\033[1m" + "Computer Cards are:" + "\033[0m")
		print(self.computer_cards[0])
		print("Still to be displayed" + "\n")
		print("\033[1m" + "User Cards are:" + "\033[0m")
		for item_user in self.user_cards:
			print(item_user)


class Betting:

	# defining all class variable
	deal_amount = 0

	def __init__(self, total_amount):
		self.total_amount = self.remain_bal = total_amount

	def get_amount(self):
		while True:
			print("Add Bet amount")
			amount = int(input())
			if Betting.checking_remaining(self, amount):
				self.deal_amount += amount
				print("Do you want to Deal: Y for Yes , N for No")
				user_ans = input().upper()
				if user_ans == 'Y':
					continue
				else:
					break
			else:
				print("You exceeding your limit")
				break

	def checking_remaining(self, amount):
		self.remain_bal = self.remain_bal - amount
		return True if self.remain_bal > 0 else False



