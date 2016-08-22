from bank_account import BankAccount

class CheckingAccount(BankAccount):
	"""
		Class for a checking account 
		the user must have a minimum amount of money that they can deposit
		a minimum amount of money that they can withdraw
		and a minimum balance that they can have on their account
	"""
	def __init__(self, account_name, account_number, minimum_deposit, minimum_withdraw, minimum_balance):
		#initialising the class with minimum values
		#ensure that only correct data types are passed
		if isinstance(account_name, str):
			self.account_name = account_name
		else:
			return None
		if isinstance(account_number, int):
			self.account_number = account_number
		else:
			return None
		if isinstance(minimum_deposit, int):
			self.minimum_deposit = minimum_deposit
		else:
			return None
		if isinstance(minimum_withdraw, int):
			self.minimum_withdraw = minimum_withdraw
		else:
			return None
		if isinstance(minimum_balance, int):
			self.minimum_balance = minimum_balance
		else:
			return None
		self.account_balance = minimum_balance

	#method to deposit money into the account
	def deposit_money(self, amount):
		if amount > self.minimum_deposit: 
			self.account_balance = self.account_balance + amount
		else:
			return "Figure too little to credit account"

	#method to withdraw money from the account 
	def withdraw_money(self, amount):
		if amount > self.account_balance:
			return "Not enough money for transaction"
		elif (self.account_balance - amount) < self.minimum_balance:
			return "Exceeds minimum balance"
		elif amount < self.minimum_withdraw:
			return "Low withdraw value"
		else:
			self.account_balance = self.account_balance - amount
			return str(amount) + " has been withdrawn"
