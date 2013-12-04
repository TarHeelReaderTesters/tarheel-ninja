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
            if len(param) == 4:
                self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
            else:
                self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})
            self._browser.implicitly_wait(30)
            self.base_url = "http://tarheelreader.org/"


        def test_background_color(self):
            browser = self._browser
            browser.get(self.base_url + "2013/11/18/tarheelreadertestbook/")

            settings = browser.find_element_by_xpath("//img[contains(@src,'/themeV1/images/settings.png')]")# Find the settings menu
            WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//img[contains(@src,'/themeV1/images/settings.png')]").is_displayed())
            settings.click()
           
            colors = browser.find_element_by_xpath("//span[contains(@class,'colors')]")# Find the Colors menu
            WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//span[contains(@class,'colors')]").is_displayed())
            colors.click()
            
            pageColor = browser.find_element_by_xpath("//span[contains(text(),'Page Color')]")# Find the Page Color menu
            WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//span[contains(text(),'Page Color')]").is_displayed())
            #WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//ul[@class='submenu l1 r1 active selected']").is_displayed())
            
            pageColor.click()
            
            colorSelect = browser.find_element_by_xpath("//span[contains(@class,'magenta')]")# choose a color
            WebDriverWait(browser, MAX_WAIT_TIME).until(lambda s: s.find_element_by_xpath("//span[contains(@class,'magenta')]").is_displayed())
            
            colorSelect.click()


            rgb = browser.find_element_by_xpath("//div[contains(@class,'thr-book-page')]").value_of_css_property('background-color')
       
            print rgb
            if rgb == "rgba(255, 0, 255, 1)":
                    print "background color values are equal"

            else:
                print "background color values are not equal"
                

        def tearDown(self):
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



if __name__ == "__main__":
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

