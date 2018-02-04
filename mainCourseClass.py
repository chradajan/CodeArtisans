from courseClass import Course

class MainCourse(Course):
	def __init__(self, courseCode: int, courseType: str, instructor: str, time: str, place: str, coCourse: list):
		super().__init__(courseCode, courseType, instructor, time, place)
		self.coCourse = coCourse