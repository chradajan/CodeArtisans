"""
Scheduler stores 

class Scheduler:
	def __init__(self, badTimes: dict):
		self.schedules = dict() #Schedule in format {Day: []}
		self._fillInBadTimes()

	def schedule(self, allCourses: dict):
		"""
		format of allCourses: {CourseTitle: [MainCourse objects]}
		format of badTimes: {Day: [(start, end)]}
		"""

	def _fillInBadTimes(self, badTimes: dict)
