from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import unittest
import time
import sys
import os
sys.tracebacklimit = 0
MAX_WAIT_TIME=8
usingChrome=False

#testing Main Menu
class MainMenu(unittest.TestCase):
    def setUp(self):
        #checks if command contains a browser version
        self.url = param[1]
        if len(param) == 5:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3], "version": param[4]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3]})
                
    def test_main_menu(self):
        self._browser.get(self.url)
        self.assertIn("Tar Heel Reader", self._browser.title)
                
        menuNames = ['Home', 'Find a book', 'Collections', 'Favorites', 'Write a book', 'Log in', 'Help', 'Your books', 'Announcements', 'Photo credits']
        for menuName in menuNames:
            try:
                while True:
                    try:
                        #ensures that the element has loaded in the browser before interaction
                        WebDriverWait(self._browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//img[contains(@src,'/images/well.png')]").is_displayed())
                        break
                    except StaleElementReferenceException:
                        time.sleep(1.0)
                            
                well = self._browser.find_element_by_xpath("//img[contains(@src,'/images/well.png')]")
                well.click()
                WebDriverWait(self._browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_class_name("navigationMenu").is_displayed())
            except NoSuchElementException:
                assert 0, "Cannot find main menu"


            try:
                WebDriverWait(self._browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_link_text(menuName))
                homePage = self._browser.find_element_by_link_text(menuName)
                homePage.click()
                time.sleep(3.0)
                if(menuName!="Home"):
                    self._browser.get("http://www.tarheelreader.org")
            except:
                assert 0, "Cannot find " + menuName + " button"

                            
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
             
if __name__ == "__main__":
	#Do we have right number of parameters?
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
