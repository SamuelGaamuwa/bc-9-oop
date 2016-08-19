from datetime import datetime
from attendance_records import Attendance_Records
class Student(object):
    country = {'KE':'Kenya', 'UG':'Uganda', 'TZ':'Tanzania'}

    student_id = 0
    attendance_dict = {}

    def __init__(self, first_name, last_name, cc='KE'):
        self.first_name = first_name
        self.last_name = last_name
        self.country = Student.country[cc]
        #auto increment the id with every new object created
        Student.student_id += 1
        

    def attend_class(self, **kwargs):
        #check if the values for loc, teacher and date are passed in kwargs, and if not set defaults
        self.loc = kwargs.get('loc', 'Hogwarts')
        self.teacher = kwargs.get('teacher', 'Alex')
        self.date = kwargs.get('date', str(datetime.date.today()))
        #register the first name of the student in a dictionary with the date as the key value
        Student.attendance_dict[self.date] = self.first_name
        #pass the dictionary to the attendance list in the attendance records class
        return Attendance_Records.attendance_list(attendance_dict)
       
