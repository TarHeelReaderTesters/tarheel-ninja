from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time

MAX_WAIT_TIME=30

class Searcher:
	def __init__(self):
		usingChrome=False

                #Too many input arguments?
                if(len(sys.argv)>2):
                        print "Incorrect number of parameters!"
                        print "Format is: %s [-c]" % (sys.argv[0],)
                        sys.exit(1)
                elif(len(sys.argv)==2 and sys.argv[1]=="-c"):
                        usingChrome=True

                #Figure out what browser we are going to use
                if(usingChrome):
                        chromedriver = "/home/dallara/SeleniumDrivers/chromedriver"
                        os.environ["webdriver.chrome.driver"] = chromedriver
                        self._browser = webdriver.Chrome(chromedriver)
                else:
                        self._browser=webdriver.Firefox()

		self.run_search_test()

	def run_search_test(self):
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

		#click on first book that is found
		try:
			#Make sure original body div goes invisible before searching in new one that will appear after searching
			self._browser.find_element_by_xpath("//div[contains(@class, 'find-page') and (contains(@style, 'display:none') or contains(@style, 'display: none') or contains(@style, 'visibility:hidden') or contains(@style, 'visibility: hidden'))]")

			visibleBody=self._browser.find_element_by_xpath("//div[contains(@class, 'find-page') and not(contains(@style, 'display:none')) and not(contains(@style, 'display: none')) and not(contains(@style, 'visibility:hidden')) and not(contains(@style, 'visibility: hidden'))]")
			bookLink=visibleBody.find_element_by_xpath(".//a[contains(@data-type, 'book')]")
			bookLink.click()
		except NoSuchElementException:
			assert 0, "can't find book to read"

		self.run_read_test()

	def run_read_test(self):
		"""Runs the book reading test for Tar Heel Reader
		   PRE: Already at title page of book being read
		   POST: Entire book has been read, on page where
			 user chooses what he/she wants to do next
		"""

		#Tell the browser to only wait 3 additional seconds so can tell faster when finished reading
		self._browser.implicitly_wait(3.0)

		#Read one page at a time of current book
		while(True):
			try:
				readAgainElements=self._browser.find_elements_by_xpath("//li[contains(@data-speech, 'again')]")

				if(len(readAgainElements)>0):
					print "finished reading book"
					break

				nextPageLink=self._browser.find_element_by_link_text("Next")
				nextPageLink.click()

			except NoSuchElementException:
				print "error reading book"
				break

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
