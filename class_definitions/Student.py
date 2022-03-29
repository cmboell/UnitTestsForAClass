"""
Assignment name: Unit Tests for a Class Assignment
Program: student.py
Author: Colby Boell
Last date modified: 03/28/2022

The purpose of this program is to use a class to make students and then use unit testing to test
the class to ensure that it is properly functioning.
"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        if isinstance(gpa, float) and gpa <= 4.0:
            self.gpa = gpa
        else:
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


if __name__ == '__main__':
    student1 = Student("Boell", "Colby", "Programming", 3.8)
    student2 = Student("Kellihan", "Lisa", "Science", 3.95)
    print(student1)
    print(student2)
