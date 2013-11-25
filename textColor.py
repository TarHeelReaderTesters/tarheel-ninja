from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://tarheelreader.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        # open | /2013/10/22/pandas-can-eat/ | 
        driver.get(self.base_url + "/2013/10/22/pandas-can-eat/")
        # click | css=img[alt="Settings"] | 
        driver.find_element_by_css_selector("img[alt=\"Settings\"]").click()
        # click | css=span.colors | 
        driver.find_element_by_css_selector("span.colors").click()
        # click | css=li.textColors > span | 
        driver.find_element_by_css_selector("li.textColors > span").click()
        # click | //li[2]/ul/li[7]/span | 
        driver.find_element_by_xpath("//li[2]/ul/li[7]/span").click()

        rgb = driver.find_element_by_xpath("//div[contains(@class,'thr-book-page')]").value_of_css_property('color')
           
        print rgb
        if rgb == "rgba(255, 255, 255, 1)":
                print "text color values are equal"

        else:
            print "text color values are not equal"
    
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
    unittest.main()
