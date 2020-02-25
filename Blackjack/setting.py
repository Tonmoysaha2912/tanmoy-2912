import random as ran
from os import system
from time import sleep


class BlackJack:

	def __init__(self):
		self.card_type = ['heart', 'spread', 'club', 'diamond']
		self.card_values = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'King', 'Queen', 'Ace']
		self.card_varies = {'heart': self.card_values, 'spread': self.card_values, 'club': self.card_values, 'diamond': self.card_values}
		self.computer_cards = []
		self.user_cards = []

	def start_game(self):
		for i in range(2):
			BlackJack.get_cards(self, "user")
		for i in range(2):
			BlackJack.get_cards(self, "computer")

	def get_cards(self, player_type):

		temp_card_type = ran.choice(self.card_type)
		temp_card = ran.choice(self.card_varies[temp_card_type])
		temp_value = temp_card + " of " + temp_card_type

		if player_type == "computer":
			self.computer_cards.append(temp_value)
		else:
			self.user_cards.append(temp_value)

		(self.card_varies[temp_card_type]).remove(temp_card)

	def display(self, player_type="computer"):
		sleep(3)
		system('cls')
		print("\033[1m" + "Computer Cards are:" + "\033[0m")
		if player_type == "computer":
			for item_comp in self.computer_cards:
				print(item_comp)
		else:
			print(self.computer_cards[0])
			print("Still to be displayed" + "\n")

		print("\033[1m" + "User Cards are:" + "\033[0m")
		for item_user in self.user_cards:
			print(item_user)

		# print(self.card_varies)


class Betting:

	def __init__(self, total_amount):
		self.deal_amount = 0
		self.total_amount = self.remain_bal = total_amount

	def get_amount(self):
		user_ans = 'Y'
		res = None
		amount = None
		while True:
			if user_ans.upper() == 'Y':
				print("Add Bet amount")
				amount = int(input())
				res = Betting.checking_remaining(self, amount)

			if res > 0:
				self.deal_amount += amount if user_ans.upper() == 'Y' else 0
				print("Do you want to Deal: Y for Yes , N for No")
				user_ans = input().upper()
				if user_ans.upper() == 'Y':
					continue
				elif user_ans.upper() == 'N':
					break
				else:
					print("Please choose the valid option")
					continue

			elif res == 0:
				self.deal_amount += amount
				print("You have reached to your max limit")
				break

			else:
				print("You are exceeding your max limit")
				break

	def checking_remaining(self, amount):
		self.remain_bal = self.remain_bal - amount
		return self.remain_bal



