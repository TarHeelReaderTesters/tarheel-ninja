from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import sys

class testTextColor(unittest.TestCase):
    def setUp(self):
        self.url = param[1]

        if len(param) == 5:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3], "version": param[4]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3]})
            
        self._browser.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_text_color(self):
        self._browser.get(self.url + '/' + "2013/11/18/tarheelreadertestbook/")
        self._browser.find_element_by_css_selector("img[alt=\"Settings\"]").click()
        self._browser.find_element_by_css_selector("span.colors").click()
        self._browser.find_element_by_css_selector("li.textColors > span").click()
        self._browser.find_element_by_xpath("//li[2]/ul/li[7]/span").click()

        rgb = self._browser.find_element_by_xpath("//div[contains(@class,'thr-book-page')]").value_of_css_property('color')
           
        print rgb
        if rgb == "rgba(255, 255, 255, 1)":
                print "text color values are equal"

        else:
            print "text color values are not equal"
    

    def tearDown(self):
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
