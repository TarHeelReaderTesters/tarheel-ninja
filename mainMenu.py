from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import unittest
import time
import sys
import os

MAX_WAIT_TIME=30
usingChrome=False

#testing Main Menu
class MainMenu(unittest.TestCase):
    def setUp(self):
    #Figure out what browser we are going to use

        if len(param) == 4:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})
                
    def test_main_menu(self):
        driver = self._browser
        driver.get("http://www.tarheelreader.org")
        self.assertIn("Tar Heel Reader", driver.title)
                
        menuNames = ['Home', 'Find a book', 'Collections', 'Favorites', 'Write a book', 'Log in', 'Help', 'Your books', 'Announcements', 'Photo credits']
        for menuName in menuNames:
            print 'Current name :', menuName
            try:
                while True:
                    try:
                        WebDriverWait(driver, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//img[contains(@src,'/themeV1/images/well.png')]").is_displayed())
                        break
                    except StaleElementReferenceException:
                        time.sleep(1.0)
                            
                well = driver.find_element_by_xpath("//img[contains(@src,'/themeV1/images/well.png')]")
                well.click()
                WebDriverWait(driver, MAX_WAIT_TIME).until(lambda s: s.find_element_by_class_name("navigationMenu").is_displayed())
            except NoSuchElementException:
                assert 0, "Cannot find main menu"

            try:
                WebDriverWait(driver, MAX_WAIT_TIME).until(lambda s: s.find_element_by_link_text(menuName))
                homePage = driver.find_element_by_link_text(menuName)
                homePage.click()
                time.sleep(3.0)
                if(menuName!="Home"):
                    driver.back()
            except NoSuchElementException:
                assert 0, "Cannot find " + menuName + " button"
                            
    def tearDown(self):
		time.sleep(5.0)
        if len(param) == 4:
            print '\nTest: ' + param[0]
            print 'Platform: ' + param[3]
            print 'Browser: ' + param[4]
            print 'Version: ' + param[5]
        else:
            print len(param)
            print '\nTest: ' + param[0]
            print 'Platform: ' + param[3]
            print 'Browser: ' + param[4]
        self._browser.quit()
             
if __name__ == "__main__":
	#Do we have right number of parameters?
    param = []
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
