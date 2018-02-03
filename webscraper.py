#from selenium import webdriver
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import lxml
import requests
import urllib
import bs4 import BeautifulSoup

URL = "https://www.reg.uci.edu/perl/WebSoc"

def scrape(department, courseCode):
	

# 	# content = urlopen(URL).read()
# 	# soup = BeautifulSoup(content, "lxml")

# 	# for paragraph in soup.head:
# 	# 	print(paragraph)
# 	# 	print('\n')

# 	driver = webdriver.Chrome()

# 	driver.get("https://www.reg.uci.edu/perl/WebSoc")

# 	departmentField = driver.find_element_by_name("Dept")
# 	departmentField.send_keys(department)

# 	courseCodeField = driver.find_element_by_name("CourseNum")
# 	courseCodeField.send_keys(courseCode)

# 	displayResultButton = driver.findElement(By.xpath("//input[@name='Submit' and @value='Display Web Results']"))
# 	displayResultButton.click()

# 	html = driver.page_source

# 	soup = BeautifulSoup(html)

# 	for tag in soup.find_all('title'):
# 		print(tag.text)

if __name__== "__main__":
	scrape("CSE","46") 

