from typing import List

class Lecture:
    number  = str()
    length  = str()
    lecture    = str()
    lecturer = str()
    sequenceNumber = str()
    group = str()
    room = str()

class Day:
    weekday = str('')
    date = str('')
    lectures:List[Lecture] = []
