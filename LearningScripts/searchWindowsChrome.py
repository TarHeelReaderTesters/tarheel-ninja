from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time

MAX_WAIT_TIME=30

class Searcher:
	def __init__(self):
		chromedriver = "/home/dallara/SeleniumDrivers/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self._browser = webdriver.Chrome(chromedriver)
		self.run_test()

	def run_test(self):
		"""Runs the book searching test for Tar Heel Reader
		"""

		#Load home page of Tar Heel Reader
		self._browser.get("http://tarheelreader.org")
		assert "Tar Heel Reader" in self._browser.title

		#Click on find book button
		try:
    			findButton=self._browser.find_element_by_xpath("//a[contains(@href,'/find/')]")
    			findButton.click()
		except NoSuchElementException:
    			assert 0, "can't find find book button"

		#Narrow down search options
		self._browser.implicitly_wait(MAX_WAIT_TIME)
		self.select_option("//select[contains(@name, 'category')]", "People and Places", "can't find category selection element")
		self.select_option("//select[contains(@name, 'reviewed')]", "Include unreviewed", "can't find review status selection field")
		self.select_option("//select[contains(@name, 'audience')]", "Any rating", "can't find rating selection field")
		self.select_option("//select[contains(@name, 'language')]", "English", "can't find language selection field")

		#input a value into the search field
		try:
			searchField=self._browser.find_element_by_xpath("//input[contains(@placeholder, 'Enter text to search')]")
			searchField.send_keys("lake"+Keys.RETURN)
		except NoSuchElementException:
			assert 0, "can't find search field"

		#Close browser
		time.sleep(3.0)
		self._browser.close()
	
	def select_option(self, xpath, textToFind, exceptionString):
		"""Selects from an arbitrary select element on the search page.

		xpath--the select element HTML description that will help the
		       browser find that select element

		textToFind--the text which the browser is trying to find an
                            option for within the select element

		exceptionString--the text to display if the select element
				 being searched for is not found
		"""	
		try:
			selectionElement=self._browser.find_element_by_xpath(xpath)
			options=selectionElement.find_elements_by_tag_name("option")
			optionStrings=[]
			
			for option in options:
				optionStrings.append(str(option.text))
			options[optionStrings.index(textToFind)].click()
		
		except NoSuchElementException:
			assert 0, exceptionString
def main():
	searcher=Searcher()
	sys.exit(0)

if __name__=='__main__':
	main()
