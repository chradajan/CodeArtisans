import itertools
from mainCourseClass import MainCourse
from courseClass import Course
from collections import defaultdict

"""
Scheduler generates a list of all the possible combinations of class
the user can take
"""
class Scheduler:
	def __init__(self, allCourses: dict, badTimes: dict):
		"""
		format of allCourses: {CourseTitle: [MainCourse objects]}
		format of badTimes: {Day: [(start, end)]}
		"""
		self.scheduleCombinations = []
		self.takenTimes = defaultdict(list)
		self._fillInBadTimes(badTimes)
		self._scheduler(allCourses)

	def getScheduleCombinations(self):
		return self.scheduleCombinations

	def _scheduler(self, allCourses: dict):
		permutationMainAndCoCourses = []
		for sameCourses in allCourses.values():
			if sameCourses[0].getCoCourses() == []:
				permutationMainAndCoCourses.append(sameCourses)
			else:
				temp = []
				for mainCourse in sameCourses:
					temp  += list(itertools.product(*([mainCourse], mainCourse.getCoCourses())))
				permutationMainAndCoCourses.append(temp)
		permutationDiffCourses = list(itertools.product(*permutationMainAndCoCourses))

		for combo in permutationDiffCourses:
			takenTimesPerCombo = self.takenTimes.copy()
			conflict = False
			combined = list(itertools.chain.from_iterable(combo))
			for course in combined:
				courseTimes = course.getTimes()
				for day,time in courseTimes.items():
					startTime = int(time[0])
					endTime = int(time[1])
					for dayList in takenTimesPerCombo[day]:
						for tupl in dayList:
							storedStart = int(tupl[0])
							storedEnd = int(tupl[1])
							if startTime > storedEnd or endTime < storedStart:
								takenTimesPerCombo[day].append((time + (course,)))
							else:
								conflict = True
								break
						else:
							continue
						break
					else:
						continue
					break
				else:
					continue
				break
			if not conflict:
				# self.scheduleCombinations.append(combined)
				# uncomment top and delte this, for testing
				l = []
				for i in combined:
					l.append(i.getCourseCode())
				self.scheduleCombinations.append(l)

		# for combo in permutationDiffCourses:
		# 	takenTimesPerCombo = self.takeTimes.copy()
		# 	conflict = False
		# 	for courses in combo:
		# 		combined = list(itertools.chain.from_iterable(courses))
		# 		for course in combined:
		# 			courseTimes = course.getTimes()
		# 			for day,time in courseTimes.items():
		# 				startTime = int(time[0])
		# 				endTime = int(time[1])
		# 				for dayList in takenTimesPerCombo[day]:
		# 					for tupl in dayList:
		# 						storedStart = int(tupl[0])
		# 						storedEnd = int(tupl[1])
		# 						if startTime > storedEnd or endTime < storedStart:
		# 							takenTimesPerCombo[day].append()
		# 						else:
		# 							conflict = True
		# 							break
		# 					else:
		# 						continue
		# 					break
		# 				else:
		# 					continue
		# 				break
		# 			else:
		# 				continue
		# 			break
		# 		else:
		# 			continue
		# 		break
		# 	else:
		# 		continue
		# 	break
		# 	if !conflict

	def _fillInBadTimes(self, badTimes: dict):
		"""
		Populate the takenTimes dictionary with user specified badTimes
		"""
		for day,times in badTimes.items():
			for time in times:
				self.takenTimes[day].append(times + (0,))


if __name__ == "__main__":
	Lab311 = Course(16041, "Lab", "A1", "HEYDARIGORJI, A.", "M   8:00-10:50", "ELH 110")
	print(Lab311)
	Lab312 = Course(16042, "Lab", "A2", "TAZARV, A.", "Tu   11:00- 1:50p0", "ELH 110")
	lab31list = [Lab311, Lab312]
	Lec31L = MainCourse(16040, "Lec", "A", "DANG, Q.", "Tu   5:00- 6:50p", "SSH 100", lab31list)


	Lab331 = Course(36130, "Lab", "10", "LIU, J.", "TuTh   2:00- 3:50p", "ELH 110")
	Lab332 = Course(36131, "Lab", "10", "LIU, J.", "TuTh   2:00- 3:50p", "ELH 110")
	Lab333 = Course(36133, "Lab", "10", "LIU, J.", "TuTh   2:00- 3:50p", "ELH 110")
	Lab33List = [Lab331, Lab332, Lab333]
	Lec33a = MainCourse(36110, "Lec", "A", "DANG, Q.", "MWF   1:00- 1:50p", "SSH 100", Lab33List)
	Lec33b = MainCourse(36115, "Lec", "B", "DANG, Q.", "MWF   4:00- 4:50p", "SSH 100", Lab33List)
	allCourses = {"CSE 31L": [Lec31L], "ICS 33": [Lec33a, Lec33b]}

	x = Scheduler(allCourses, {})
	print(x.getScheduleCombinations())
