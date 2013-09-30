import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

#testing INVALID Login to TarHeelReader.org

class FirefoxInvalidLogin(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox() # Get local session of firefoxz
		
	def test_firefox_invalid_login(self):
		driver = self.driver
		driver.get("http://www.tarheelreader.org") # Load page
		self.assertIn("Tar Heel Reader", driver.title)
		try:
			well = driver.find_element_by_xpath("//img[contains(@src,'http://tarheelreader3s.cs.unc.edu/themeV1/images/well.png')]")# Find the main menu
			well.click()
			WebDriverWait(driver, 10).until(lambda s: s.find_element_by_class_name("navigationMenu").is_displayed())
		except NoSuchElementException:
			assert 0, "Can not find main menu"
			
		#Find the login link and click, throw error otherwise
		try:
			login = driver.find_element_by_link_text("Log in")
			login.click()
		except NoSuchElementException:
			assert 0, "Can not find login"
		
		#check if the cursor is on the user field of the form
		#type in user name
		try:
			user = driver.find_element_by_name("log")
			user.send_keys("huynhl")
		except NoSuchElementException:
			assert 0, "Can not find user form"
		
		#makes sure the cursor is on the password field
		#types an invalid password
		try:
			pw = driver.find_element_by_name("pwd")
			pw.send_keys("thrt85384")
			pw.send_keys(Keys.RETURN)
		except NoSuchElementException:
			assert 0, "Can not find pwd form"
		
		#if page logins in with an INVALID user/pwd then throw an error
		try:
			text = driver.find_element_by_xpath("//p[@class='message']")
		except NoSuchElementException:
			assert 0, "Invalid pwd test failed"
		
	def tearDown(self):
		self.driver.close()
		
if __name__ == "__main__":
	unittest.main()
