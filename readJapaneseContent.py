from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30

class JapaneseContentReader(unittest.TestCase):
	def setUp(self):
		#check How many arguments were passed in (OS Browser Version) or (OS Browser)
		self.url = param[1]
		if len(param) == 5:
                	self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3], "version": param[4]})
            	else:
                	self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3]})
                
                if param[1] == "http://gbserver3.cs.unc.edu":
                    self.build_up_page_tests("sandboxJapaneseBookLines.txt")
                    self._japaneseBook = "http://gbserver3.cs.unc.edu/2011/08/20/japanese-house%E3%80%80%E3%81%AB%E3%81%BB%E3%82%93%E3%80%80%E3%81%AE%E3%80%80%E3%81%84%E3%81%88/"
                else:
                    self.build_up_page_tests("japaneseBookLines.txt")
                    self._japaneseBook = "http://tarheelreader.org/2013/03/04/%E3%81%AF%E3%81%98%E3%82%81%E3%81%BE%E3%81%97%E3%81%A6/"

        def build_up_page_tests(self, textFile):
                try:
                        f=open(textFile, 'r')
                        self._lines=f.readlines()
                        for i in range(0, len(self._lines)):
                                self._lines[i]=self._lines[i].strip().decode('utf-8')
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

		self._browser.get(self._japaneseBook)
       		self._browser.implicitly_wait(MAX_WAIT_TIME)

		line_number=0
		error=""
        	
		previous_url=self._browser.current_url

        	if param[1] == "http://gbserver3.cs.unc.edu":
            		count = 6
        	else:
            		count = 11
        #Read one page at a time of current book
		while(line_number<count):
			try:
				time.sleep(3.0)

				#Have we checked the title and author on the first page yet? 
				if(line_number>=2):
					lineToLookFor=self._lines[line_number]
					page_wrap_element=self._browser.find_element_by_xpath("//div[contains(@class, 'page-wrap') and not (contains(@style, 'display:none') or contains(@style, 'display: none') or contains(@style, 'visibility:hidden') or contains(@style, 'visibility: hidden'))]")
					caption_box_element=page_wrap_element.find_element_by_class_name("thr-caption-box")
					text_elements=caption_box_element.find_elements_by_xpath("//p[contains(@class, 'VOSay')]")

					if(len(text_elements)==0):
						error="No caption element found!"
					else:
						text_element=text_elements[0]
						for paragraph in text_elements:
							if(paragraph.text==lineToLookFor):
								text_element=paragraph
								break
						if(text_element.text!=lineToLookFor):
							error="Wrong text on page "+str(line_number)+" of book!" 

					line_number+=1

				#Make sure title and author on first page of story are correct
				else:
					titleToLookFor=self._lines[0]
					authorToLookFor=self._lines[1]

					content_wrap=self._browser.find_element_by_xpath("//div[contains(@class, 'content-wrap') and not (contains(@style, 'display:none') or contains(@style, 'display: none') or contains(@style, 'visibility:hidden') or contains(@style, 'visibility: hidden'))]")
					title_elements=content_wrap.find_elements_by_class_name("title")
					author_elements=content_wrap.find_elements_by_class_name("thr-author")

					if(len(title_elements)==0):
						error="No title text element found!"
                                        elif(title_elements[0].text!=titleToLookFor):
                                                error="Wrong title found!"

					if(len(author_elements)==0):
						error="No author text element found!"
                                        elif(author_elements[0].text!=authorToLookFor):
                                                error="Wrong author found!"

					line_number=2

				nextPageLink=self._browser.find_element_by_link_text("Next")
				nextPageLink.click()

				if(previous_url==self._browser.current_url):
					error="Next button did not work!"
					break

				previous_url=self._browser.current_url

			except NoSuchElementException:
				error="Error reading book"
				break


		#Has the test failed or not?
		if(error!=""):
			assert 0, error

	def tearDown(self):
		"""Closes the browser when the program exits
		"""
        	time.sleep(5.0)
		if len(param) == 5:
			print '\nTest: ' + param[0]
			print 'URL: ' + param[1]
			print 'Platform: ' + param[2]
			print 'Browser: ' + param[3]
			print 'Version: ' + param[4]
		else:
			print '\nTest: ' + param[0]
			print 'URL: ' + param[1]
			print 'Platform: ' + param[2]
			print 'Browser: ' + param[3]
		self._browser.quit()

if __name__ == '__main__':
    	param=[]
	if len(sys.argv) == 5:
        	param.append(sys.argv[0])
        	param.append(sys.argv[1])
        	param.append(sys.argv[2])
        	param.append(sys.argv[3])
        	param.append(sys.argv[4])
        	del sys.argv[1:]
	else:
		param.append(sys.argv[0])
		param.append(sys.argv[1])
		param.append(sys.argv[2])
		param.append(sys.argv[3])
		del sys.argv[1:]
	unittest.main()
