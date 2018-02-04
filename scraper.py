from urllib.request import Request, urlopen
import urllib.error
from html.parser import HTMLParser
from courseClass import Course
from mainCourseClass import MainCourse
import re
#from flask import flask
#app = Flask(__name__)

#@app.route("/courseread")
def CourseReader(Dept: str, CourseNum: str) -> []:
	mainCourseList = []
	link = "https://www.reg.uci.edu/perl/WebSoc?YearTerm=2018-03&ShowFinals=1&ShowComments=0&Dept={}&CourseNum={}".format(Dept, CourseNum)
	WebSocHTML = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	with urlopen(WebSocHTML) as file:
		for line in file:
			decodedLine = line.decode()
			if 'Bookstore' in decodedLine:
				courseCode = units = 0
				courseType = courseType = courseSection = instructor = time = place = final = ""

				#Parse course code
				match = re.search('\d\d\d\d\d', decodedLine)
				if match:
					courseCode = int(match.group())

				#Parse type
				match = re.search('Lec|Dis|Lab|Tap', decodedLine)
				if match:
					courseType = match.group()

				#Parse Section
				match = re.search('>((\w\w?)|(\d\d?))<', decodedLine)
				if match:
					courseSection = match.groups()[0].replace('>', '').replace('<', '')

				#Parse units
				match = re.search('>\d<', decodedLine)
				if match:
					units = int(match.group().replace('>', '').replace('<', ''))

				#Parse instructor
				match = re.findall('>((?:\w+(?: ?\w+)?, \w+.)|(?:STAFF))<', decodedLine)
				if match:
					instructor = '  '.join(match)

				#Parse Time
				match = re.search('\w+[ ]+&nbsp;[ ]+\d+:\d+-[ ]?\d+:\d+p?', decodedLine)
				if match:
					time = match.group().replace(' &nbsp;', '')

				#Parse Place
				match = re.search('>\w+ \d+[A-Z]*<', decodedLine)
				if match:
					place = match.group().replace('>', '').replace('<', '')

				#Parse Final
				match = re.search('\w+, +\w+ +\d+, +\d+:\d+-\d+:\d+p?m?', decodedLine)
				if match:
					final = match.group()
				elif units > 0:
					final = 'TBA'

				print('{:5}  {:3}  {:2}  {:1}  {:20}  {:17}  {:10}  {}'.format(courseCode, courseType, courseSection, units, instructor, time, place, final))

				if units > 0:
					mainCourseList.append(MainCourse(courseCode, courseType, courseSection, instructor, time, place, final))
				elif units == 0:
					mainCourseList[-1].addCoCourse(Course(courseCode, courseType, courseSection, instructor, time, place))
				

		return mainCourseList