import unittest
import regex as re

class LectureTypes:
    LECTURE = 'l'
    PRACTICE = 'p'
    EXAM = 'e'


# Курсанти - 0
# Редовно Бакалавър - 1
# Задочно Бакалавър - 2
# Редовно Магистър - 3


def find_group_type(lecture_name):
    flags = re.UNICODE | re.MULTILINE
    r_practical = re.compile('пз|практика|практическо занятие', flags=flags)
    r_exam = re.compile('изпит', flags=flags)

    if(re.search(pattern=r_practical, string=lecture_name) is not None):
        return LectureTypes.PRACTICE
    elif(re.search(pattern=r_exam, string=lecture_name) is not None):
        return LectureTypes.EXAM
    else:
        return LectureTypes.LECTURE


class LectureDataForExport:
    name = str('')
    name_number = str('')
    groups = []
    type = LectureTypes.LECTURE
    group_type = 0
    student_count = 0
    occurences = 0

    
    def get_as_list(self):
        return [self.name,
                self.name_number,
                self.groups.__str__(),
                self.type,
                self.group_type,
                self.student_count,
                self.occurences]


    def __init__(self, lecture):
        self.name = lecture.lecture_name
        self.name_number = str('')
        self.groups = re.findall(re.compile('\d+'), lecture.group)
        self.type = find_group_type(lecture.lecture_name)
        self.group_type = 0
        self.occurences = 0
        self.student_count = 0


    def __str__(self) -> str:
        return  'Name: ' + self.name + '\n' + \
                'Number: ' + self.name_number + '\n' + \
                'Groups: ' + str(self.groups) + '\n' + \
                'Type: '   + self.type + '\n' + \
                'Occurences: ' + str(self.occurences) + '\n'
        

    def __eq__(self, __o: object) -> bool:
        if  (self.name == __o.name) & \
            (self.name_number == __o.name_number) & \
            (self.groups == __o.groups) & \
            (self.type == __o.group_type):
            return True
        else:
            return False


    def __hash__(self) -> int:
        hash =  1
        hash *= (1 + self.name.__hash__()) * \
                (1 + self.name_number.__hash__()) * \
                (1 + self.type.__hash__())
        for group in self.groups:
            hash *= (1 + group.__hash__())
        return hash