import time


class Bank_Account():
	def __init__(self,username,profession,income,balance=0):
		self.username = username
		self.profession = profession
		self.income = income
		self.balance = balance
		self.history = []

def display_info(self):
	print('WELCOME TO GENERAL FINANCING!')
	print('Displaying information...please wait!')
	time.sleep(5)
	print(f'USERNAME: {self.username}',
		 f'PROFESSION: {self.profession}',
		  f'INCOME: {self.income}',
		  f'BALANCE: {self.balance}')

def deposit(self,amount):
	question = int(input('Enter the amount to deposit: '))
	self.amount = question
	if self.amount >=0:
		print(f'Added {self.amount}')
		self.balance.append(self.amount)
		self.history.append(self.amount)
	else:
		print('Enter a valid amount!')

client1 = Bank_Account()
client1.display_info()
client1.deposit()
