class course:
	def __init__(self, courseCode: int, courseType: str, instructor: str, time: str, place: str, final: str):
		self.courseCode = courseCode
		self.courseType = courseType
		self.instructor = instructor
		self.time = getTimes(time)
		self.place = place
		self.final = final

	def formatTimes(timeList: list) -> tuple:
		'''Takes a list with [startTime, endTime] and converts it to (start, end) in 24 hr format'''
		startTime, endTime = timeList
		if 'p' in endTime:
			endTime = endTime.replace('p', '')
			
			endTimeHour = int(endTime.split(':')[0])
			if endTimeHour != 12:
				endTimeHour += 12
			endTime = str(endTimeHour) + ':' + str(endTime.split(':')[1])
			
			startTimeHour = int(startTime.split(':')[0])
			if startTimeHour < (endTimeHour - 12):
				startTimeHour += 12
			startTime = str(startTimeHour) + ':' + str(startTime.split(':')[1])
		return (startTime, endTime)

	def getTimes(timeString: str) -> dict:
		timeDict = {}
		daysString = timeString.split()[0]
		timeList = ''.join(testTime.split()[1:]).split('-')
		if 'M' in timeString.split():
			pass


testTime = "TuTh   11:00- 1:00p"

testTimeValues = ''.join(testTime.split()[1:]).split('-')
print(formatTimes(testTimeValues))