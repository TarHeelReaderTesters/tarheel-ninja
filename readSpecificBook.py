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

class readBook(unittest.TestCase):
    def setUp(self):
        if(param == 3):
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})
    
            
    def test_readBook(self):
        """Runs the book reading test for Tar Heel Reader
        PRE: Already at title page of book being read
        POST: Entire book has been read, on page where
        user chooses what he/she wants to do next"""
        #Tell the browser to only wait 3 additional seconds so can tell faster when finished reading
        self.searchBook()
        self._browser.implicitly_wait(3.0)

        #Read one page at a time of current book
        while(True):
            try:
                readAgainElements=self._browser.find_elements_by_xpath("//li[contains(@data-speech, 'again')]")

                if(len(readAgainElements)>0):
                    break

                nextPageLink=self._browser.find_element_by_link_text("Next")
                nextPageLink.click()

            except NoSuchElementException:
                assert 0, "error reading book"
#                print "error reading book"
#                break
                
    def searchBook(self):
        """Runs the book searching test for Tar Heel Reader
		"""

		#Load home page of Tar Heel Reader
        self._browser.get("http://tarheelreader.org")
        assert "Tar Heel Reader" in self._browser.title

        #Click on find book button
        try:
            findButton=self._browser.find_element_by_xpath("//a[contains(@href,'/find/')]")
            findButton.click()
        except NoSuchElementException:
            assert 0, "can't find find book button"

        #Narrow down search options
        self._browser.implicitly_wait(MAX_WAIT_TIME)
        self.select_option("//select[contains(@name, 'category')]", "People and Places", "can't find category selection element")
        self.select_option("//select[contains(@name, 'reviewed')]", "Include unreviewed", "can't find review status selection field")
        self.select_option("//select[contains(@name, 'audience')]", "Any rating", "can't find rating selection field")
        self.select_option("//select[contains(@name, 'language')]", "English", "can't find language selection field")

        #input a value into the search field
        try:
            searchField=self._browser.find_element_by_xpath("//input[contains(@placeholder, 'Enter text to search')]")
            searchField.send_keys("lake"+Keys.RETURN)
        except NoSuchElementException:
            assert 0, "can't find search field"

        #click on first book that is found
        try:
            #Make sure original body div goes invisible before searching in new one that will appear after searching
            self._browser.find_element_by_xpath("//div[contains(@class, 'find-page') and (contains(@style, 'display:none') or contains(@style, 'display: none') or contains(@style, 'visibility:hidden') or contains(@style, 'visibility: hidden'))]")

            visibleBody=self._browser.find_element_by_xpath("//div[contains(@class, 'find-page') and not(contains(@style, 'display:none')) and not(contains(@style, 'display: none')) and not(contains(@style, 'visibility:hidden')) and not(contains(@style, 'visibility: hidden'))]")
            bookLink=visibleBody.find_element_by_xpath(".//a[contains(@data-type, 'book')]")
            bookLink.click()
        except NoSuchElementException:
            assert 0, "can't find book to read"
                
    def select_option(self, xpath, textToFind, exceptionString):
        """Selects from an arbitrary select element on the search page.

        xpath--the select element HTML description that will help the
            browser find that select element

        textToFind--the text which the browser is trying to find an
                            option for within the select element

        exceptionString--the text to display if the select element
                being searched for is not found
        """	
        try:
            selectionElement=self._browser.find_element_by_xpath(xpath)
            options=selectionElement.find_elements_by_tag_name("option")
            optionStrings=[]
        
            for option in options:
                optionStrings.append(str(option.text))
            options[optionStrings.index(textToFind)].click()
        
        except NoSuchElementException:
            assert 0, exceptionString
            
    def tearDown(self):
        time.sleep(5.0)
        print '\n Ran ' + param[0]
        print 'Platform: ' + param[1]
        print 'Browser: ' + param[2]
        self._browser.close()
        
if __name__ == '__main__':
    param = []
    if len(sys.argv) == 4:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        del sys.argv[1:]
        del sys.argv[2:]
        del sys.argv[3:]
    else:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        del sys.argv[1:]
        del sys.argv[2:]

    unittest.main()
    
>>>>>>> 5a7a7caf2a98f588bf175ec03bcbf4fca5b247c3
