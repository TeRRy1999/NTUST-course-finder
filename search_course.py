from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox) # linux only

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome('./chromedriver')

# driver = webdriver.Chrome(options=chrome_options, executable_path=r"./chromedriver")

driver.set_window_size(1400,1000)

def course(coursename, num):
	driver.get("https://querycourse.ntust.edu.tw/querycourse/")#put here the adress of your page
	driver.refresh()
	course_name = driver.find_element_by_xpath("//input[@aria-label='課程名稱']")
	time.sleep(2)
	search = driver.find_element_by_xpath("//div[button/@class='v-btn v-btn--block v-btn--round theme--light']")
	course_name.send_keys(coursename)
	search.click()
	time.sleep(2)

	allcourse = driver.find_elements_by_tag_name('tbody')
	# print (allcourse[0].text.split(' ')[7].split('(')[0])
	if int(allcourse[0].text.split(' ')[7].split('(')[0]) < num:
		print ('{} here have {} seats for you: '.format(allcourse[0].text.split(' ')[1], num - int(allcourse[0].text.split(' ')[7].split('(')[0])))
		meg = '{} here have {} seats for you'.format(allcourse[0].text.split(' ')[1], num - int(allcourse[0].text.split(' ')[7].split('(')[0]))
		os.system('echo \"{}\" | mail -s \"Test email\" 1332771977@qq.com'.format(meg))
	else:
		print('--- {} No seats: {}'.format(allcourse[0].text.split(' ')[1], int(allcourse[0].text.split(' ')[7].split('(')[0])))

while True:
	driver.refresh()
	# course("張益賓", 55)
	course("禪心情趣－茶禪、香禪、花禪", 54)
	# course("吳傳嘉", 55)
	# course("林保宏", 56)
	# course("沈中安", 20)
	time.sleep(100)

