from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30

class screenshot(unittest.TestCase):
    def setUp(self):
    
        if len(param) == 4:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})
        
        self._browser.set_window_size(800,600)
        self._browser.set_window_position(0,0)
                
    def test_screenShot(self):
        """Runs the book searching test for Tar Heel Reader
		"""

        #make a directory named 'images'
        if len(param) == 4:
            if not os.path.exists('images'):
                os.makedirs('images')
            if not os.path.exists('images/base/'):
                os.makedirs('images/base/')
            if not os.path.exists('images/base/' + param[1]):
                os.makedirs('images/base/' + param[1])
            if not os.path.exists('images/base/' + param[1] +'/' + param[2] + ' ' + param[3]):
                os.makedirs('images/base/' + param[1] +'/' + param[2] + ' ' + param[3])
        else:
            if not os.path.exists('images'):
                os.makedirs('images')
            if not os.path.exists('images/base/'):
                os.makedirs('images/base/')
            if not os.path.exists('images/base/' + param[1]):
                os.makedirs('images/base/' + param[1])
            if not os.path.exists('images/base/' + param[1] +'/' + param[2]):
                os.makedirs('images/base/' + param[1] +'/' + param[2])
        
        
        url = ['http://tarheelreader.org/2013/11/18/tarheelreadertestbook/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/2/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/3/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/4/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/5/']
        
        screenshot_name = ['title', 'page2', 'page3', 'page4', 'page5_japanese']
        for i in range(5):
            name = screenshot_name[i] + '.png'
            self._browser.get(url[i])
            time.sleep(3.0)
            self._browser.save_screenshot('images/base/' + param[1] + '/' + param[2] +'/' + name)


		#Load home page of Tar Heel Reader
        #self._browser.get(param[3])
        #self._browser.implicitly_wait(10)
        #time.sleep(10.0)
	#Load home page of Tar Heel Reader
    #self._browser.get("http://tarheelreader.org/2013/10/22/pandas-can-eat/")
        #self._browser.save_screenshot(name)
        #self._browser.get_screenshot_as_file(name)
        #assert "Tar Heel Reader" in self._browser.title
            
    def tearDown(self):
        time.sleep(5.0)
        '''if len(param) == 4:
            print '\nTest: ' + param[0]
            print 'Platform: ' + param[1]
            print 'Browser: ' + param[2]
            print 'Version: ' + param[3]
        else:
            print '\nTest: ' + param[0]
            print 'Platform: ' + param[1]
            print 'Browser: ' + param[2]'''
        self._browser.quit()
        
if __name__ == '__main__':
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
        del sys.argv[3:]

    unittest.main()
    
