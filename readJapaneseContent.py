from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30
param=[]

class JapaneseContentReader(unittest.TestCase):
        def setUp(self):
                #check How many arguments were passed in (OS Browser Version) or (OS Browser)
                if len(param) == 4:
                        self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
                else:
                        self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})

                self.build_up_page_tests()

        def build_up_page_tests(self):
                try:
                        f=open('japaneseBookLines.txt', 'r')
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

		self._browser.get("http://tarheelreader.org/2013/03/04/%E3%81%AF%E3%81%98%E3%82%81%E3%81%BE%E3%81%97%E3%81%A6/")
       		self._browser.implicitly_wait(MAX_WAIT_TIME)

		line_number=0
		error=False

		#Read one page at a time of current book
		while(line_number<11):
			try:
				time.sleep(3.0)

				#Have we checked the title and author on the first page yet? 
				if(line_number>=2):
					lineToLookFor=self._lines[line_number]
					page_wrap_element=self._browser.find_element_by_xpath("//div[contains(@class, 'page-wrap') and not (contains(@style, 'display:none') or contains(@style, 'display: none') or contains(@style, 'visibility:hidden') or contains(@style, 'visibility: hidden'))]")
					caption_box_element=page_wrap_element.find_element_by_class_name("thr-caption-box")
					text_elements=caption_box_element.find_elements_by_xpath("//p[contains(@class, 'VOSay')]")

					if(len(text_elements)==0):
						error=True
					else:
						text_element=text_elements[0]
						for paragraph in text_elements:
							if(paragraph.text==lineToLookFor):
								text_element=paragraph
								break
						if(text_element.text!=lineToLookFor):
							error=True

					line_number+=1

				#Make sure title and author on first page of story are correct
				else:
					titleToLookFor=self._lines[0]
					authorToLookFor=self._lines[1]

					content_wrap=self._browser.find_element_by_xpath("//div[contains(@class, 'content-wrap') and not (contains(@style, 'display:none') or contains(@style, 'display: none') or contains(@style, 'visibility:hidden') or contains(@style, 'visibility: hidden'))]")
					title_element=content_wrap.find_element_by_class_name("title")
					author_element=content_wrap.find_element_by_class_name("thr-author")

                                        if(title_element.text!=titleToLookFor):
                                                error=True

                                        if(author_element.text!=authorToLookFor):
                                                error=True

					line_number=2

				nextPageLink=self._browser.find_element_by_link_text("Next")
				nextPageLink.click()

			except NoSuchElementException:
				print "Error reading book"
				error=True
				break


		#Has the test failed or not?
		if(error==True):
			assert 0, "Japanese text is incorrect"

	def tearDown(self):
		"""Closes the browser when the program exits
		"""
        #global param
                time.sleep(5.0)

                if len(param) == 4:
                        print '\nTest: ' + param[0]
                        print 'Platform: ' + param[1]
                        print 'Browser: ' + param[2]
                        print 'Version: ' + param[3]
                else:
                        print '\nTest: ' + param[0]
                        print 'Platform: ' + param[1]
                        print 'Browser: ' + param[2]
                self._browser.quit()

if __name__ == '__main__':
    if len(sys.argv) == 4:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        del sys.argv[1:]

    else:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        del sys.argv[1:]

    unittest.main()
