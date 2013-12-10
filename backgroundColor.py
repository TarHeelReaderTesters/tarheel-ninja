import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time, re, sys

MAX_WAIT_TIME = 5

#testing background colors
class testBackgroundColor(unittest.TestCase):
        def setUp(self):
        
		#check How many arguments were passed in (OS Browser Version) or (OS Browser)
		self._url = str(param[1])
		if len(param) == 5:
                	self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3], "version": param[4]})
            	else:
                	self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3]})
                
                if self._url == "http://gbserver3.cs.unc.edu":
                    
                    self.base_url  = "http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/"
                else:
                    self.base_url  = "http://tarheelreader.org/2013/11/18/tarheelreadertestbook/"


        def test_background_color(self):
            browser = self._browser
            browser.get(self.base_url)
            try:
                settings = browser.find_element_by_xpath("//img[contains(@src,'images/settings.png')]")# Find the settings menu
                WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//img[contains(@src,'images/settings.png')]").is_displayed())
                settings.click()
                if "gbserver3" in self._url:
                    settings.click()
                
                WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//img[contains(@src,'images/settings.png')]").is_displayed())
               
                colors = browser.find_element_by_xpath("//span[contains(@class,'colors')]")# Find the Colors menu
                WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//span[contains(@class,'colors')]").is_displayed())
                colors.click()
                
                pageColor = browser.find_element_by_xpath("//span[contains(text(),'Page Color')]")# Find the Page Color menu
                WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//span[contains(text(),'Page Color')]").is_displayed())
                
                pageColor.click()
                
                colorSelect = browser.find_element_by_xpath("//span[contains(@class,'magenta')]")# choose a color
                WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//span[contains(@class,'magenta')]").is_displayed())
                
                colorSelect.click()


                rgb = browser.find_element_by_xpath("//div[contains(@class,'thr-book-page')]").value_of_css_property('background-color')
                if rgb == "rgba(255, 0, 255, 1)" or "#f0f":
                        print "background color values are equal"

                else:
                    print "background color values are not equal"
            except:
                assert 0, "Could not change background color"
                

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


if __name__ == "__main__":
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

