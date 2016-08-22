import unittest
from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

class Bank_Account_Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_is_type_of_bank_account(self):
		obj = BankAccount('name', 11)
		self.assertEqual(True, type(obj) is BankAccount)

	def test_is_type_of_savings_account(self):
		obj = SavingsAccount('name', 11, 1000)
		self.assertEqual(True, type(obj) is SavingsAccount)

	def test_is_type_of_checking_account(self):
		obj = CheckingAccount('name', 11, 2000, 1000, 5000)
		self.assertEqual(True, type(obj) is CheckingAccount)

	def test_is_instance_bank_account(self):
		obj = BankAccount('name', 11)
		self.assertIsInstance(obj, BankAccount)

	def test_is_instance_savings_account(self):
		obj = SavingsAccount('name', 11, 1000)
		self.assertIsInstance(obj, SavingsAccount)

	def test_is_instance_bank_account(self):
		obj = CheckingAccount('name', 11, 2000, 1000, 5000)
		self.assertIsInstance(obj, CheckingAccount)

	def test_get_account_name(self):
		obj = BankAccount('name', 11)
		self.assertEqual(obj.get_account_name(), 'name')

	def test_get_account_number(self):
		obj = BankAccount('name', 11)
		self.assertEqual(obj.get_account_number(), 11)

	def test_get_balance(self):
		obj = BankAccount('name', 11)
		self.assertEqual(obj.get_account_balance(), 0)

	def test_deposit_money(self):
		obj = BankAccount('name', 11)
		obj.deposit_money(3000)
		self.assertEqual(obj.get_account_balance(), 3000)

	def test_withdraw_money(self):
		obj = BankAccount('name', 11)
		obj.deposit_money(3000)
		obj.withdraw_money(1000)
		self.assertEqual(obj.get_account_balance(), 2000)

	def test_withdraw_excess(self):
		obj = BankAccount('name', 11)
		obj.deposit_money(3000)
		self.assertEqual(obj.withdraw_money(4000), "Not enough money for transaction")

	def test_desposit_savings(self):
		obj = SavingsAccount('name', 11, 1000)
		obj.deposit_money(3000)
		self.assertEqual(obj.get_account_balance(), 3000)

	def test_withdraw_savings(self):
		obj = SavingsAccount('name', 11, 1000)
		obj.deposit_money(3000)
		obj.withdraw_money(800)
		self.assertEqual(obj.get_account_balance(), 2200)

	def test_withdraw_out_of_bounds(self):
		obj = SavingsAccount('name', 11, 1000)
		obj.deposit_money(3000)
		self.assertEqual(obj.withdraw_money(2000), "Withdraw amount beyond limit")

	def test_withdraw_excess_savings(self):
		obj = SavingsAccount('name', 11, 1000)
		obj.deposit_money(3000)
		self.assertEqual(obj.withdraw_money(4000), "Not enough to complete transaction")

	def test_withdraw_excess_in_bounds(self):
		obj = SavingsAccount('name', 11, 1000)
		obj.deposit_money(500)
		self.assertEqual(obj.withdraw_money(800), "Not enough to complete transaction")

	def test_deposit_checking(self):
		obj = CheckingAccount('name', 11, 2000, 1000, 5000)
		obj.deposit_money(3000)
		self.assertEqual(obj.get_account_balance(), 8000)

	def test_insufficient_deposit(self):
		obj = CheckingAccount('name', 11, 2000, 1000, 5000)
		self.assertEqual(obj.deposit_money(1000), "Figure too little to credit account")

	def test_withdraw_checking(self):
		obj = CheckingAccount('name', 11, 2000, 1000, 5000)
		obj.deposit_money(3000)
		obj.withdraw_money(2000)
		self.assertEqual(obj.get_account_balance(), 6000) 

	def test_small_withdraw(self):
		obj = CheckingAccount('name', 11, 2000, 1000, 5000)
		obj.deposit_money(3000)
		self.assertEqual(obj.withdraw_money(500), "Low withdraw value") 

	def test_withdraw_excess_checking(self):
		obj = CheckingAccount('name', 11, 2000, 1000, 5000)
		obj.deposit_money(3000)
		self.assertEqual(obj.withdraw_money(9000), "Not enough money for transaction") 

if __name__ == '__main__':
	unittest.main()