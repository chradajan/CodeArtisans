from courseClass import Course

class MainCourse(Course):
	def __init__(self, courseCode: int, courseType: str, courseSection: str, instructor: str, time: str, place: str, coCourse: list):
		super().__init__(courseCode, courseType, courseSection, instructor, time, place)
		self.coCourse = coCourse