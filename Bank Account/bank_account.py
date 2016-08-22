class BankAccount(object):
	"""Bank Account is a class potraying a bank account as it is used 
		in real life
	"""	
	#function to initialise the account with the account name and the account number 
	def __init__(self, account_name, account_number):
		if isinstance(account_name, str):
			self.account_name = account_name
		else:
			return None
		if isinstance(account_number, int):
			self.account_number = account_number
		else:
			return None

		self.account_balance = 0
	
	#method to return the account name
	def get_account_name(self):
		return self.account_name

	#method to return the account number
	def get_account_number(self):
		return self.account_number

	#method to return the account balance
	def get_account_balance(self):
		return self.account_balance

	#method to deposit money into the account
	def deposit_money(self, amount):
		if amount > 0:
			self.account_balance = self.account_balance + amount
			return str(amount)
		else:
			return "Cannot credit account with negative sum"

	#method to withdraw money from the account 
	def withdraw_money(self, amount):
		if amount > self.account_balance:
			return "Not enough money for transaction"
		else:
			self.account_balance = self.account_balance - amount
			return str(amount) + " has been withdrawn"

obj = BankAccount('name', 11)
print(obj.get_account_balance)

