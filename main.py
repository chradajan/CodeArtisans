import scraper

if __name__ == '__main__':
	course1Dept = input('Enter department: ')
	course1Num = input('Enter number: ')

	testCourse = scraper.CourseReader(course1Dept, course1Num)
	for i in testCourse:
		print(i)