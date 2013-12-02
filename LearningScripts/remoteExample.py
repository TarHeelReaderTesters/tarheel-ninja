lsfrom selenium import webdriver
import unittest
import sys

usingChrome=False

class remoteExample(unittest.TestCase):
	def setUp(self):
		if(usingChrome):
			self._driver=webdriver.Remote("http://152.23.23.217:4444/wd/hub", webdriver.DesiredCapabilities.CHROME)
		else:
			self._driver=webdriver.Remote("http://152.23.23.217:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX)

	def test_remote(self):
		self._driver.get('http://tarheelreader.org/2013/10/22/pandas-can-eat/3/')
		self._driver.get_screenshot_as_file('/home/dallara/Desktop/book_page.png')
		
	def tearDown(self):
		self._driver.quit()

if __name__=="__main__":
	if(len(sys.argv)>2):
		print "Incorrect number of parameters!"
    		print "Format is: %s [-c]" % (sys.argv[0],) # '-c' allows for remote chrome browser launch instead of firefox
    		sys.exit(1)
    	elif(len(sys.argv)==2):
			if(sys.argv[1]=="-c"):
        			usingChrome=True
			else:
				print "Error in '%s' parameter!" % (sys.argv[1],)
				print "Format is: %s [-c]" % (sys.argv[0],)
                        	sys.exit(1)

	del sys.argv[1:]
	unittest.main()
