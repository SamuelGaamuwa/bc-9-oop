class Attendance_Records(object):
	attended = []
	attendance = {}
	def attendance_list(attendance_dict):
		for key in attendance_dict.keys():
			if key in Attendance_Records.attendance.keys() and Attendance_Records.attendance[key] is not None:
				(Attendance_Records.attendance[key]).append(attendance_dict[key])
			else:
				Attendance_Records.attendance[key] = (Attendance_Records.attended.append(attendance_dict[key]))
		return Attendance_Records.attendance 
	def return_attendees(date):
			return Attendance_Records.attendance[date]

