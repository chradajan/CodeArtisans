from courseClass import Course

class MainCourse(Course):
	def __init__(self, courseCode: int, courseType: str, courseSection: str, instructor: str, time: str, place: str, final: str):
		super().__init__(courseCode, courseType, courseSection, instructor, time, place)
		self.coCourses = []
		self.final = final

	def addCoCourse(self, newCoCourse: Course):
		self.coCourses.append(newCoCourse)

	def getCoCourses(self):
		return self.coCourses

	def __string__(self):
		bigString = 'Course Code: {}\nCourse Type: {}\nCourse Section: {}\nInstructor: {}\nTime: {}\nLocation: {}\nFinal: {}'.format(self.courseCode, self.courseType, self.courseSection, self.instructor.replace('\n\', '  ''), self.time, self.place, self.final)
		bigString += '\nCo-Courses:\n\n'
		for i in self.coCourses:
			bigString += i
			bigString += '\n\n'
		return bigString
