from student import Student 
from attendance_records import Attendance_Records

student1 = Student('Samuel', 'Gaamuwa', 'UG')
student2 = Student('Rebecca', 'Oyenene',)
student3 = Student('Derrick', 'Kiboko', 'TZ')
student4 = Student('Martha', 'Kyozira', 'UG')
student5 = Student('Joshua', 'Mazune')
student6 = Student('Mary', 'Nansubuga' 'UG')
student7 = Student('Marvin', 'Kato', 'TZ')
student8 = Student('Jazmine', 'Babirye')

student1.attend_class()
student2.attend_class()
student3.attend_class()
student4.attend_class()
student5.attend_class()

def present_students(self, date):
    #pass the date to the return attendees function in Attendance records and return students present that day
    return Attendance_Records.return_attendees(date)

