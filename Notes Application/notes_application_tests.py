import unittest

from notes_application import NotesApplication

class Test_Notes_Application(unittest.TestCase):
	def setUp(self):
		pass

	def test_object_type(self):
		obj = NotesApplication('author')
		self.assertEqual(True, type(obj) is NotesApplication)

	def test_object_instance(self):
		obj = NotesApplication()
		self.assertNotIsInstance(obj, NotesApplication)

	def test_object_instance_with_argument(self):
		obj = NotesApplication('author')
		self.assertIsInstance(obj, NotesApplication)

	def test_is_argument_set(self):
		obj = NotesApplication('author')
		self.assertEqual(obj.author, 'author')

	def test_if_note_created(self):
		obj = NotesApplication('author')
		obj.create('This is a trial')
		self.assertIn({'author': 'This is a trial'}, obj.notes)

	def test_if_can_search(self):
		obj = NotesApplication('author')
		obj.create('My man oxidionious is a guy')
		self.assertEqual(obj.search('oxidionious'), 'My man oxidionious is a guy')

	def test_if_can_delete(self):
		obj = NotesApplication('author')
		obj.create('to be deleted')
		obj.delete(0)
		self.assertNotIn({'author': 'to be deleted'}, obj.notes)

	def test_if_delete_out_of_bounds(self):
		obj = NotesApplication('author')
		obj.create('bow chica wow wow')
		self.assertEqual(obj.delete(3), 'Note does not exist')

	def test_for_list(self):
		obj = NotesApplication('author')
		obj.create('this is the first note')
		obj.create('this is the second note')
		obj.create('this is the third note')
		obj.create('this is the fourth note')
		self.assertEqual(obj.list(), 4)

	def test_if_can_edit(self):
		obj = NotesApplication('author')
		obj.create('to be edited')
		self.assertIn({'author': 'to be edited'}, obj.notes)
		obj.edit(0,'this is the edit')
		self.assertNotIn({'author': 'to be edited'}, obj.notes)
		self.assertIn({'author': 'this is the edit'}, obj.notes)



if __name__ == '__main__':
	unittest.main()	