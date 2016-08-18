import unittest

from super_sum import super_sum

class MySuperSumTests(unittest.TestCase):

	def setUp(self):
		pass
	def test_numbers(self):
		self.assertEqual(super_sum(10, 4, 5), 19, msg='cannot add numbers')
	def test_list_numbers(self):
		self.assertEqual(super_sum([10,6], 4, 5), 25, msg='cannot add numbers in a list and numbers outside the list')
	def test_list_list(self):
		self.assertEqual(super_sum([10,4], [5,6]), 25, msg='cannot add numbers in lists')
	def test_lists_numbers(self):
		self.assertEqual(super_sum([10,4], [5,6], 7, 8), 40, msg='cannot add numbers in lists and numbers outside lists')
	def test_non_numbers(self):
		with self.assertRaises(TypeError):
			super_sum('man', '4')

if __name__ == '__main__':
	unittest.main()
