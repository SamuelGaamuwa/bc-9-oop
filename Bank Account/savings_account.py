from bank_account import BankAccount

class SavingsAccount(BankAccount):
	"""
		Class for savings account, it mimicks a savings account in that 
		there has to be a maximum amount of money one can withdraw
	"""
	#initialising the savings account with the maximum withdraw value
	 def __init__(self, account_name, account_number, maximum_withdraw):

	 	if isinstance(account_name, str):
	 		self.account_name = account_name
	 	else:
	 		return None
	 	if isinstance(account_number, int):
	 		self.account_number = account_number
	 	else:
	 		return None

	 	self.account_balance = 0
	
	 	if isinstance(maximum_withdraw, int):
	 		self.maximum_withdraw = maximum_withdraw
	 	else:
	 		return None

	 #method to add interest to the account 
	 def add_interest(self, interest_rate):
	 	self.account_balance = self.account_balance + (self.account_balance * interest_rate)

	 #method to withdraw money with in the confines of the savings account
	 def withdraw_money(self, amount):
	 	if amount > self.account_balance:
	 		return "Not enough to complete transaction"
	 	elif amount > self.maximum_withdraw:
	 		return "Withdraw amount beyond limit"
	 	else:
	 		self.account_balance = self.account_balance - amount
	 	return "Transaction successful"
