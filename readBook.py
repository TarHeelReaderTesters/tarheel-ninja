from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30
usingChrome=False

class Searcher(unittest.TestCase):
	def setUp(self):
		self.build_up_page_tests()

                #Figure out what browser we are going to use
                if(usingChrome):
                        chromedriver = "/home/dallara/SeleniumDrivers/chromedriver"
                        os.environ["webdriver.chrome.driver"] = chromedriver
                        self._browser = webdriver.Chrome(chromedriver)
                else:
                        self._browser=webdriver.Firefox()

	def build_up_page_tests(self):
		try:
			f=open('bookLines.txt', 'r')
			self._lines=f.readlines()
			for i in range(0, len(self._lines)):
				self._lines[i]=self._lines[i].strip()
			f.close()
		except Exception:
			print "Error reading book lines file!"
			try:
				f.close()
			except Exception:
				print "Error closing book lines file!"
			finally:
				sys.exit(1)

	def test_book_reading(self):
		"""Runs the book reading test for Tar Heel Reader
		   PRE: Already at title page of book being read
		   POST: Entire book has been read, on page where
			 user chooses what he/she wants to do next
		"""

		self._browser.get("http://tarheelreader.org/2010/08/26/i-like-sonic-cartoons/")
		self._browser.implicitly_wait(MAX_WAIT_TIME)

		line_number=-1
		error=False

		#Read one page at a time of current book
		while(line_number<8):
			try:
				time.sleep(3.0)

				if(line_number>=0):
					lineToLookFor=self._lines[line_number]
					print "looking for \'"+lineToLookFor+"\'"
					page_wrap_element=self._browser.find_element_by_xpath("//div[contains(@class, 'page-wrap') and not (contains(@style, 'display:none') or contains(@style, 'display: none') or contains(@style, 'visibility:hidden') or contains(@style, 'visibility: hidden'))]")
					caption_box_element=page_wrap_element.find_element_by_class_name("thr-caption-box")
					text_elements=caption_box_element.find_elements_by_xpath("//p[contains(@class, 'VOSay')]")

					if(len(text_elements)==0):
						print "could not find any text on page %d of book" % (line_number+2)
						error=True
					else:
						text_element=text_elements[0]
						for paragraph in text_elements:
							if(paragraph.text==str(lineToLookFor)):
								text_element=paragraph
								print "found!"
								break
						if(text_element.text!=lineToLookFor):
							print "wrong text on page %d of book" % (line_number+2)
							error=True

				nextPageLink=self._browser.find_element_by_link_text("Next")
				nextPageLink.click()
				line_number+=1

			except NoSuchElementException:
				print "error reading book"
				error=True
				break

		print "finished reading book"

		#Has the test failed or not?
		if(error==True):
			sys.exit(1)

	def tearDown(self):
		"""Closes the browser when the program exits
		"""
		time.sleep(5.0)
		self._browser.quit()

if __name__=='__main__':
	if(len(sys.argv)>2): #Too many or incorrect input arguments?
        	print "Incorrect number of parameters!"
                print "Format is: %s [-c]" % (sys.argv[0],)
		sys.exit(1)
        elif(len(sys.argv)==2):
                if(sys.argv[1]=="-c"):
                	usingChrome=True
                else:
                        print "Error in '%s' parameter!" % (sys.argv[1],)
                        print "Format is: %s [-c]" % (sys.argv[0],)
			sys.exit(1)

	del sys.argv[1:]
	unittest.main()
