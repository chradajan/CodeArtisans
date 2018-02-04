from urllib.request import request, urlopen
import urllib.error
from html.parser import HTMLParser

def CourseReader(Dept: str, CourseNum: str)
	link = "https://www.reg.uci.edu/perl/WebSoc?YearTerm=2018-03&ShowFinals=1&ShowComments=0&Dept={}&CourseNum={}".format(Dept, CourseNum)
	WebSocHTML = request(link, headers={'User-Agent': 'Mozilla/5.0'})
	with urlopen(WebSocHTML) as file:
		for line in file:
			if 'Bookstore' in line:
				