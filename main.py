import scraper
from scheduler import Scheduler

if __name__ == '__main__':
	course1 = scraper.CourseReader('CSE', '46')
	course2 = scraper.CourseReader('math', '3d')
	course3 = scraper.CourseReader('cse', '31l')
	course4 = scraper.CourseReader('in4matx', '43')

	for i in course1:
		print(i)

	#allCourses = {'CSE 46': course1, 'MATH 3D': course2, 'CSE 31L': course3, 'IN4MATX 43': course4}

	#print(allCourses)

	#testSchedule = Scheduler(allCourses, {})

	# for i in testSchedule.getScheduleCombinations():
	# 	print(i)