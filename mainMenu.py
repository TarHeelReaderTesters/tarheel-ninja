import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

#testing Main Menu

class MainMenu(unittest.TestCase):

        def setUp(self):
                self.driver = webdriver.Firefox() 

                
        def test_main_menu(self):
                driver = self.driver
                driver.get("http://www.tarheelreader.org")
                self.assertIn("Tar Heel Reader", driver.title)

                
                menuNames = ['Home', 'Find a book', 'Collections', 'Favorites', 'Write a book', 'Log in', 'Help', 'Your books', 'Announcements', 'Photo credits']
                for menuName in menuNames:      
                    print 'Current name :', menuName
                    
                    try:
                            well = driver.find_element_by_xpath("//img[contains(@src,'http://tarheelreader3s.cs.unc.edu/themeV1/images/well.png')]")
                            well.click()
                            WebDriverWait(driver, 10).until(lambda s: s.find_element_by_class_name("navigationMenu").is_displayed())
                    except NoSuchElementException:
                            assert 0, "Cannot find main menu"
                    try:
                            homePage = driver.find_element_by_link_text(menuName)
                            homePage.click()
                            driver.back()
                            
                    except NoSuchElementException:
                        assert 0, "Cannot find " + menuName + " button"

             
                        
        def tearDown(self):
                self.driver.close()
             
if __name__ == "__main__":
        unittest.main()
