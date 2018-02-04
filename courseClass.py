class Course:
	def __init__(self, courseCode: int, courseType: str, courseSection: str, instructor: str, time: str, place: str):
		self.courseCode = courseCode
		self.courseType = courseType
		self.courseSection = courseSection
		self.instructor = instructor
		self.time = self._splitTimes(time)
		self.place = place

	def getTimes(self):
		return self.time

	def _formatTimes(self, timeList: list) -> tuple:
		'''Takes a list with [startTime, endTime] and converts it to (start, end) in 24 hr format'''
		startTime, endTime = timeList
		if 'p' in endTime:
			endTime = endTime.replace('p', '')
			
			endTimeHour = int(endTime.split(':')[0])
			if endTimeHour != 12:
				endTimeHour += 12
			endTime = str(endTimeHour) + str(endTime.split(':')[1])
			
			startTimeHour = int(startTime.split(':')[0])
			if startTimeHour < (endTimeHour - 12):
				startTimeHour += 12
			startTime = str(startTimeHour) + str(startTime.split(':')[1])
		startTime = startTime.replace(':', '')
		endTime = endTime.replace(':', '')
		if len(startTime) == 3:
			startTime = "0" + startTime
		if len(endTime) == 3:
			endTime = "0" + endTime
		return (startTime, endTime)

	def _splitTimes(self, timeString: str) -> dict:
		timeDict = {}
		daysString = timeString.split()[0]
		timeTuple = self._formatTimes(''.join(timeString.split()[1:]).split('-'))
		if 'M' in daysString:
			timeDict['M'] = timeTuple
		if 'Tu' in daysString:
			timeDict['Tu'] = timeTuple
		if 'W' in daysString:
			timeDict['W'] = timeTuple
		if 'Th' in daysString:
			timeDict['Th'] = timeTuple
		if 'F' in daysString:
			timeDict['F'] = timeTuple
		return timeDict

	def __str__(self):
		return 'Course Code: {}\nCourse Type: {}\nCourse Section: {}\nInstructor: {}\nTime: {}\nLocation: {}'.format(self.courseCode, self.courseType, self.courseSection, self.instructor.replace('\n\'', '  '), self.time, self.place)