import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time, re, sys


#testing background colors
class testBackgroundColor(unittest.TestCase):
       def setUp(self):
        if(param == 3):
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})
            
        self._browser.implicitly_wait(30)
        self.base_url = "http://tarheelreader.org/"
        self.verificationErrors = []
        self.accept_next_alert = True

        def test_Background_color(self): 
            browser = self._browser
            browser.get(self.base_url + "/2013/10/22/pandas-can-eat/")
            settings = browser.find_element_by_xpath("//img[contains(@src,'/themeV1/images/settings.png')]")# Find the settings menu
            settings.click()
            colors = browser.find_element_by_xpath("//span[contains(@class,'colors')]")# Find the Colors menu
            colors.click()
            pageColor = browser.find_element_by_xpath("//span[contains(text(),'Page Color')]")# Find the Page Color menu
            pageColor.click()
            colorSelect = browser.find_element_by_xpath("//span[contains(@class,'magenta')]")# choose a color
            colorSelect.click()


            rgb = browser.find_element_by_xpath("//div[contains(@class,'thr-book-page')]").value_of_css_property('background-color')
            browser.quit()
            print rgb
            if rgb == "rgba(255, 0, 255, 1)":
                    print "background color values are equal"

            else:
                print "background color values are not equal"
                
        def is_element_present(self, how, what):
            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException, e: return False
            return True
        
        def is_alert_present(self):
            try: self.driver.switch_to_alert()
            except NoAlertPresentException, e: return False
            return True
        
        def close_alert_and_get_its_text(self):
            try:
                alert = self.driver.switch_to_alert()
                alert_text = alert.text
                if self.accept_next_alert:
                    alert.accept()
                else:
                    alert.dismiss()
                return alert_text
            finally: self.accept_next_alert = True
        
        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

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

