class Course:
	def __init__(self, courseCode: int, courseType: str, instructor: str, time: str, place: str):
		self.courseCode = courseCode
		self.courseType = courseType
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

if __name__ == "__main__":
	a = Course(1,"Cse", "hey", "MWF   3:00- 3:50p	", "x")
	print(a.getTimes())
