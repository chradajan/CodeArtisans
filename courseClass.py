class course:
	def __init__(self, courseCode: int, classType: str, units: int, instructor: str, time: str, final: str):
		self.courseCode = courseCode
		self.classType = classType
		self.units = units
		self.instructor = instructor
		self.time = getTimes(time)
		self.final = final

	def splitTimes(timeList: list):
		'''Takes a list with [startTime, endTime] and breaks it into a list of 20 minute intervals between those times'''
		startTime = timeList[0]
		if 'p' in timeList[1]:
			endTime = timeList[1].replace('p', '')
			endPM = True
			startPM = True
			if int(timeList[0].split(':')[0]) < 12:
				startPM = False
		else:
			endTime = timeList[1]
			endPM = False
			startPM = False

		timeIntervals = []
		
		while startTime != endTime:
			tempMinutes = startTime.split(':')[1]
			if tempMinutes == '00':
				
			timeIntervals.append()



	def getTimes(timeString: str) -> dict:
		timeDict = {}
		daysString = timeString.split()[0]
		timeList = ''.join(testTime.split()[1:]).split('-')
		if 'M' in timeString.split():
			pass



testTime = "TuTh   8:00- 9:20"

testTimeValues = ''.join(testTime.split()[1:]).split('-')
print(testTimeValues)