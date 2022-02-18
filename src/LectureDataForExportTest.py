import unittest
from LectureDataForExport import LectureTypes, find_group_type

class TestFindGroupTypes(unittest.TestCase):        
    def test_find_group_type_for_lecture(self):
        self.assertEqual(LectureTypes.LECTURE, find_group_type('Курсов проект - лекция'))
    def test_find_group_type_for_practice(self):
        self.assertEqual(LectureTypes.PRACTICE, find_group_type('Курсов проект - пз'))   
        self.assertEqual(LectureTypes.PRACTICE, find_group_type('Курсов проект - практика'))     
        self.assertEqual(LectureTypes.PRACTICE, find_group_type('Курсов проект - практическо занятие'))          
    def test_find_group_type_for_exam(self):
        self.assertEqual(LectureTypes.EXAM, find_group_type('Курсов проект - изпит'))
        
test = TestFindGroupTypes()
test.test_find_group_type_for_lecture()
test.test_find_group_type_for_practice()
test.test_find_group_type_for_exam()