from enum import Enum, unique

@unique
class QueryTypes(Enum):
    GROUP = 'Group'
    LECTURER = 'Lecturer'
    WEEK = 'Week'