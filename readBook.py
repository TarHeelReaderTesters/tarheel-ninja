from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30

class ReadBook(unittest.TestCase):
    def setUp(self):
        self.url = str(param[1])

        if len(param) == 5:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3], "version": param[4]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3]}) 
            
    def testReadBook(self):
        """Runs the book reading test for Tar Heel Reader
        PRE: Already at title page of book being read
        POST: Entire book has been read, on page where
        user chooses what he/she wants to do next"""
        #Tell the browser to only wait 3 additional seconds so can tell faster when finished reading
        self.getToBook()
        self._browser.implicitly_wait(1.0)
	previousURL=self._browser.current_url
	print previousURL
        #Read one page at a time of current book
        while(True):
            try:
                readAgainElements=self._browser.find_elements_by_xpath("//li[contains(@data-speech, 'again')]")

                if(len(readAgainElements)>0):
                    break

                nextPageLink=self._browser.find_element_by_link_text("Next")
                nextPageLink.click()
		if(previousURL==self._browser.current_url):
			assert 0, "next page button didn't work!"

		previousURL=self._browser.current_url

            except NoSuchElementException:
                assert 0, "error reading book"
                break
                
    def getToBook(self):
        """Goes directly to a test book, which depends on the server being tested
	"""
        if self.url in "http://gbserver3.cs.unc.edu/2011/11/14/the-frog-prince-2/":
            self._browser.get("http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/")
        else:
            self._browser.get("http://tarheelreader.org/2013/11/18/tarheelreadertestbook/")
        
	assert "Tar Heel Reader" in self._browser.title
    
    def tearDown(self):
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
    param = []
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
    
