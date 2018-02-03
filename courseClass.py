class course:
	def __init__(self, courseCode: int, classType: str, units: int, instructor: str, time: str):
		self.courseCode = courseCode
		self.classType = classType
		self.units = units
		self.instructor = instructor
		self.time = getTimes(time)

	def getTimes(timeString: str) -> dict:
