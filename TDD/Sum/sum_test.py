import unittest

from sum import my_sum

class MySumTests(unittest.TestCase):
	def setUp(self):
		self.numbers = [10,5,7,8,90,60]

	def test_sum_of_digits(self):
		result = my_sum(5,10)
		self.assertEqual(result,15)
		self.assertEqual(my_sum(10,15), 25, msg='did not add the numbers')
	
	def test_non_numbers(self):
		with self.assertRaises(TypeError):
			my_sum('man', '4')
	
if __name__ == '__main__':
	unittest.main()
