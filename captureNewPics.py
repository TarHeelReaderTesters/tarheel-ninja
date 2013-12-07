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
        self.url = param[1]

        if len(param) == 5:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3], "version": param[4]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3]})

        self._browser.set_window_size(800,600)
        self._browser.set_window_position(0,0)
                
    def test_screenShot(self):
        """Runs the book searching test for Tar Heel Reader
		"""
        if self.url in "http://gbserver3.cs.unc.edu":
        #make a directory named 'images'
            if len(param) == 6:
                if not os.path.exists('images'):
                    os.makedirs('images')
                if not os.path.exists('images/new/'):
                    os.makedirs('images/new/')
                if not os.path.exists('images/new/' + param[1]):
                    os.makedirs('images/new/' + param[2])
                if not os.path.exists('images/new/' + param[1] +'/' + param[3] + param[4]):
                    os.makedirs('images/new/' + param[2] +'/' + param[3] + param[4])
            else:
                if not os.path.exists('images'):
                    os.makedirs('images')
                if not os.path.exists('images/new/'):
                    os.makedirs('images/new/')
                if not os.path.exists('images/new/' + param[2]):
                    os.makedirs('images/new/' + param[2])
                if not os.path.exists('images/new/' + param[2] +'/' + param[3]):
                    os.makedirs('images/new/' + param[2] +'/' + param[3])
            print self.url
        
            url = ['http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/','http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/2/' , 'http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/3/' , 'http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/4/', 'http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/5/', 'http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/6/']
        
            screenshot_name = ['title', 'page1', 'page2', 'page3', 'page4', 'page5', 'page6']
            for i in range(5):
                name = screenshot_name[i] + '.png'
                self._browser.get(url[i])
                time.sleep(3.0)
                self._browser.save_screenshot('images/new/' + param[2] + '/' + param[3] +'/' + name)
        else:
        if len(param) == 6:
            if not os.path.exists('images'):
                os.makedirs('images')
            if not os.path.exists('images/new/'):
                os.makedirs('images/new/')
            if not os.path.exists('images/new/' + param[1]):
                os.makedirs('images/new/' + param[2])
            if not os.path.exists('images/new/' + param[1] +'/' + param[3] + param[4]):
                os.makedirs('images/new/' + param[2] +'/' + param[3] + param[4])
        else:
            if not os.path.exists('images'):
                os.makedirs('images')
            if not os.path.exists('images/new/'):
                os.makedirs('images/new/')
            if not os.path.exists('images/new/' + param[2]):
                os.makedirs('images/new/' + param[2])
            if not os.path.exists('images/new/' + param[2] +'/' + param[3]):
                os.makedirs('images/new/' + param[2] +'/' + param[3])
        print self.url
        
            url = ['http://tarheelreader.org/2013/11/18/tarheelreadertestbook/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/2/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/3/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/4/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/5/']
        
            screenshot_name = ['title', 'page2', 'page3', 'page4', 'page5_japanese']
            for i in range(5):
                name = screenshot_name[i] + '.png'
                self._browser.get(url[i])
                time.sleep(3.0)
                self._browser.save_screenshot('images/new/' + param[2] + '/' + param[3] +'/' + name)


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
        if len(param) == 5:
            print '\nTest: ' + param[0]
            print 'URL: ' + param[1]
            print 'Platform: ' + param[2]
            print 'Browser: ' + param[3]
            print 'Version: ' + param[4]
        
        else:
            print '\nTest: ' + param[0]
            print 'URL: ' + param[1]
            print 'Platform: ' + param[2]
            print 'Browser: ' + param[3]
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
    else:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        del sys.argv[1:]
    unittest.main()
    
