from courseClass import Course

class MainCourse(Course):
	def __init__(self, courseCode: int, courseType: str, courseSection: str, instructor: str, time: str, place: str, final: str):
		super().__init__(courseCode, courseType, courseSection, instructor, time, place)
		self.coCourses = []
		self.final = final

	def addCoCourse(self, newCoCourse: Course):
		self.coCourses.append(newCoCourse)

	def getCoCourses(self):
		return self.coCourse
