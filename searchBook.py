from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30

class searchBook(unittest.TestCase):
    
    def setUp(self):
        if len(param) == 4:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})
            
    def test_searchBook(self):
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
            
    def tearDown(self):
        """Closes the browser when the program exits
            exit_code--what value the program is exiting with
            (depends on whether or not an error occurred)
            """
        time.sleep(5.0)
        print 'Ran ' + param[0]
        print 'Platform: ' + param[1]
        print 'Browser: ' + param[2]
        self._browser.close()
        
if __name__ == '__main__':
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