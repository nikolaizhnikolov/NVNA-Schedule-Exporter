import unittest
import regex as re

class LectureTypes:
    LECTURE = 'l'
    PRACTICE = 'p'
    EXAM = 'e'


class GroupTypes:
    CADET = 0
    BACHELORS = 1
    BACHELORS_REMOTE = 2
    MASTERS = 3


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
    group_type = GroupTypes.BACHELORS
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
        self.group_type = GroupTypes.BACHELORS
        self.occurences = 0
        self.student_count = 0


    def __str__(self) -> str:
        return  'Name: ' + self.name + '\n' + \
                'Number: ' + self.name_number + '\n' + \
                'Groups: ' + str(self.groups) + '\n' + \
                'Type: '   + self.type + '\n' + \
                'Occurences: ' + str(self.occurences) + '\n'

    def __key(self):
        return (self.name, self.name_number, tuple(self.groups), self.type)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, LectureDataForExport):
            return self.__key() == other.__key()
        return NotImplemented        
