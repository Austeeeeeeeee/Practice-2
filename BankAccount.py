import time
from Users import users

###NOT FINISHED
users = {
'Clemente Loral' : {'PIN':1111, 'Profession':'Doctor','Income': 5000},
'Paco Serrano'   : {'PIN':2222, 'Profession':'Hairdresser','Income': 5000},
'Maria Pacheco'  : {'PIN':3333, 'Profession':'Football player','Income': 5000}
}
def login(users):
	username = input('Enter your username: ').strip()
	pin = int(input('Enter your PIN: '))
	if username in users and users[username] == pin:
		print('Login successful!')
		return username
	if username not in users:
		print('Username does not exit!\n')
		time.sleep(2)
		q = input('Would you like to open an account?')
		if q == 'yes':
			username = input('Enter username: ')
			pin = int(input('Enter a 4-digit PIN: '))
			profession = input('Enter your profession: ')
			income = input('Enter your income: ')
		users[username] = {
			'PIN':pin,
		    'Profession': profession,
		    'Income': income}
		if q == 'no':
			print('Closing session.')


class Bank_Account():
	def __init__(self,username,profession,income,Initial_balance=0):
		self.username = username
		self.profession = profession
		self.income = income
		self.Initial_balance = Initial_balance
		self.history = []

	def login(users):
		username = input('Enter your username: ').strip()
		pin = int(input('Enter your PIN: '))
		if username in users and users[username] == pin:
			print('Login successful!')
			return username
		if username not in users:
			print('Username does not exit!\n')
			time.sleep(2)
			q = input('Would you like to open an account?')
			if q == 'yes':
				username = input('Enter username: ')
				pin = int(input('Enter a 4-digit PIN: '))
				profession = input('Enter your profession: ')
				income = input('Enter your income: ')
			users[username] = {
				'PIN': pin,
				'Profession': profession,
				'Income': income}
			if q == 'no':
				print('Closing session.')

	def display_info(self):
		print('WELCOME TO GENERAL FINANCING!')
		time.sleep(2)
		print(f'USERNAME: {self.username}\n',
			 f'PROFESSION: {self.profession}\n',
		  	 f'INCOME: {self.income}\n',
		  	 f'INITIAL BALANCE: {self.Initial_balance}')


	def operation(self):
		user_input = input("Deposit or withdraw? ")
		user_input = user_input.lower().strip()
		if user_input == "deposit":
			self.deposit()
		elif user_input == "withdraw":
			self.withdraw()

	def deposit(self):
		question = int(input('Amount to deposit: '))
		self.amount = question
		if self.amount >=0:
			print(f'--Added {self.amount}EUR')
			self.Initial_balance += self.amount
			self.updated_balance = self.Initial_balance
			print(f'YOUR CURRENT BALANCE: {self.updated_balance}EUR')
			self.history.append(self.amount)
		else:
			print('Enter a valid amount!')

	def withdraw(self):
		question = int(input("Amount to withdraw: "))
		self.amount_withdraw = question
		self.Initial_balance -= self.amount_withdraw
		self.updated_balance = self.Initial_balance
		if self.amount_withdraw <= self.updated_balance:
			print(f'--Withdrew {self.amount_withdraw}EUR')
			self.history.append(self.amount_withdraw)
			print(f'YOUR CURRENT BALANCE: {self.updated_balance}EUR')
			print()
		elif self.amount_withdraw > self.amount_withdraw:
			print('Not enough funds!')

	def display_history(self):
		question = input('Do you want to see the history of your operations? ')
		if question == 'yes':
			print(self.history)
		elif question == 'no':
			print('Okey! Thanks for choosing us!')

client1 = Bank_Account('Clement Loral','Doctor','5.000',60)
client1.display_info()
print()
client1.login()
