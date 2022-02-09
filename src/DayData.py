class Lecture:
    number  = str('')
    length  = str('')
    lecture_name    = str('')
    lecturer = str('')
    sequence_number = str('')
    group = str('')
    room = str('')

    def __init__(self, number, length, lecture_name, lecturer='', sequence_number='', group='', room=''):
        self.number=number
        self.length=length
        self.lecture_name=lecture_name
        self.lecturer=lecturer
        self.sequence_number=sequence_number
        self.group=group
        self.room=room


    def __str__(self) -> str:
        data = 'Lecture: ' + self.lecture_name + '\n' \
                ' Number: ' + self.number + \
                ' from-to: ' + self.length + '\n'
        if not (self.lecturer.__eq__('')):
            data = data + \
                ' Lecturer: ' + self.lecturer + \
                ' Seq No: ' + self.sequence_number
        if not (self.room.__eq__('')):
            data = data + ' Room: ' + self.room                
        if not (self.group.__eq__('')):
            data = data + ' Group: ' + self.group
        return data

    
    def info(self) -> str:
        # data =  self.number + ' ' + \
        data =  self.length + ' ' + \
                self.lecture_name + '\n'
        if not (self.lecturer.__eq__('')):
            data = data + \
                self.lecturer + ' ' # + \
                # self.sequence_number + ' '               
        if not (self.group.__eq__('')):
            data = data + self.group + ' ' 
        if not (self.room.__eq__('')):
            data = data + self.room + ' '
        return data

    
    def get_optionals(self):
        if(self.lecturer == ''):
            return [self.group, self.room]
        elif(self.group ==''):
            return [self.lecturer, self.room]
        else:
            return [self.group, self.lecturer]


class Day:
    weekday = str('')
    date = str('')
    lectures = []

    def __init__(self, weekday, date, lectures = []):
        self.weekday=weekday
        self.date=date
        self.lectures=lectures

    def __str__(self) -> str:
        data = self.weekday +  ' ' + self.date + '\n'
        for lecture in self.lectures:
            data = data + lecture.__str__() + '\n'
        return data

    def info(self) -> str:
        if self.lectures.__len__() == 0:
            return None
            
        data = self.weekday + ':\n'
        for lecture in self.lectures:
            data = data + lecture.info() + '\n'
        return data