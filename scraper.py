from urllib.request import Request, urlopen
import urllib.error
from html.parser import HTMLParser
from courseClass import Course
from mainCourseClass import MainCourse
import re
from flask import flask
app = Flask(__name__)

@app.route("/courseread")
def CourseReader(Dept: str, CourseNum: str):# -> [MainCourse]
	mainCourseList = []
	link = "https://www.reg.uci.edu/perl/WebSoc?YearTerm=2018-03&ShowFinals=1&ShowComments=0&Dept={}&CourseNum={}".format(Dept, CourseNum)
	WebSocHTML = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	with urlopen(WebSocHTML) as file:
		for line in file:
			decodedLine = line.decode()
			if 'Bookstore' in decodedLine:
				courseCode = units = 0
				courseType = courseType = courseSection = instructor = time = place = ""

				match = re.search('\d\d\d\d\d', decodedLine)
				if match:
					courseNumber = match.group()

				match = re.search('Lec|Dis|Lab', decodedLine)
				if match:
					courseType = match.group()
				print(courseNumber + "  " + courseType)


if __name__ == '__main__':
	CourseReader('CSE', '31L')
