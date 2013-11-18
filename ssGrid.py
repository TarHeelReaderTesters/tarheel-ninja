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
        if(param == 3):
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})
                
    def test_screenShot(self):
        """Runs the book searching test for Tar Heel Reader
		"""
        self._browser.set_window_size(800,600)
        self._browser.set_window_position(0,0)
        #make a directory named 'images'
        if not os.path.exists('images'):
            os.makedirs('images')
        
        num = 0
        name = 'images/ss_' + param[1] + '_' + param[2] + '_00.png'


        while(os.path.exists(name)):
            num = num + 1
            if num < 10:
                name = 'images/ss_' + param[1] + '_' + param[2] + '_0' + str(num) + '.png'
            else:
                name = 'images/ss_' + param[1] + '_' + param[2] + '_' + str(num) + '.png'
        

		#Load home page of Tar Heel Reader
        self._browser.get(param[3])
        self._browser.implicitly_wait(10)
        #time.sleep(10.0)
        self._browser.save_screenshot(name)
        #self._browser.get_screenshot_as_file(name)
        assert "Tar Heel Reader" in self._browser.title
            
    def tearDown(self):
        time.sleep(5.0)
        print '\n Ran ' + param[0]
        print 'Platform: ' + param[1]
        print 'Browser: ' + param[2]
        self._browser.quit()
        
if __name__ == '__main__':
    param = []
    if len(sys.argv) == 5:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        param.append(sys.argv[4])
        del sys.argv[1:]
        del sys.argv[2:]
        del sys.argv[3:]
        del sys.argv[4:]
    else:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        del sys.argv[1:]
        del sys.argv[2:]
        del sys.argv[3:]

    unittest.main()
    