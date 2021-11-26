from enum import Enum, unique

@unique
class QueryTypes(Enum):
    GROUP = 'group'
    LECTURER = 'lecturer'
    WEEK = 'week'