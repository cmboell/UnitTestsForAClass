"""
Assignment name: Unit Tests for a Class Assignment
Program: student_test.py
Author: Colby Boell
Last date modified: 03/28/2022

The purpose of this program is to use a class to make students and then use unit testing to test
the class to ensure that it is properly functioning.
"""
import unittest
from class_definitions import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student('Boell', 'Colby', 'Programming', 3.8)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Boell')
        self.assertEqual(self.student.first_name, 'Colby')
        self.assertEqual(self.student.major, 'Programming')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Boell')
        self.assertEqual(self.student.first_name, 'Colby')
        self.assertEqual(self.student.major, 'Programming')
        self.assertEqual(self.student.gpa, 3.8)

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Boell, Colby has major Programming with gpa: 3.8')

     # error for last name and first name

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = Student('123', 'Colby', 'Programming', 3.8)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = Student('Boell', '123', 'Programming', 3.8)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = Student('Boell', 'Colby', 'Developer', 'abc')

if __name__ == '__main__':
    unittest.main()
