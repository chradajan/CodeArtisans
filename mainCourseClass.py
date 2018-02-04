from courseClass import Course

class MainCourse(Course):
	def __init__(self, courseCode: int, courseType: str, courseSection: str, instructor: str, time: str, place: str):
		super().__init__(courseCode, courseType, courseSection, instructor, time, place)
		self.coCourse = []

	def addCoCourse(newCoCourse: Course):
		self.coCourse.append(newCoCourse)

	def getCoCourses(self):
		return self.coCourse
