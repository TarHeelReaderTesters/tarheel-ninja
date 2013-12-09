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
        
        #checks if command contains a browser version
        if len(param) == 6:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3], "version": param[4]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3]})

        self._browser.set_window_size(800,600)
        self._browser.set_window_position(0,0)
                
    def test_screenShot(self):
        """Runs the book searching test for Tar Heel Reader
		"""
        if self.url in "http://gbserver3.cs.unc.edu":
            #make base directories for GBserver with browser version'
            if len(param) == 5:
                if not os.path.exists('images'):
                    os.makedirs('images')
                if not os.path.exists('images/GBserver3/'):
                    os.makedirs('images/GBserver3/')
                if not os.path.exists('images/GBserver3/new/'):
                    os.makedirs('images/GBserver3/new/')
                if not os.path.exists('images/GBserver3/new/' + param[2]):
                    os.makedirs('images/GBserver3/new/' + param[2])
                if not os.path.exists('images/GBserver3/new/' + param[2] +'/' + param[3] + param[4]):
                    os.makedirs('images/GBserver3/new/' + param[2] +'/' + param[3] + param[4])
            else:
                #make base directories for GBserver without browser version'
                if not os.path.exists('images'):
                    os.makedirs('images')
                if not os.path.exists('images/GBserver3/'):
                    os.makedirs('images/GBserver3/')
                if not os.path.exists('images/GBserver3/new/'):
                    os.makedirs('images/GBserver3/new/')
                if not os.path.exists('images/GBserver3/new/' + param[2]):
                    os.makedirs('images/GBserver3/new/' + param[2])
                if not os.path.exists('images/GBserver3/new/' + param[2] +'/' + param[3]):
                    os.makedirs('images/GBserver3/new/' + param[2] +'/' + param[3])
            print self.url
        
        
            url = ['http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/','http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/2/' , 'http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/3/' , 'http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/4/', 'http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/5/', 'http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/6/']
        
        
            screenshot_name = ['title', 'page2', 'page3', 'page4', 'page5', 'page6']
            
            #takes a screenshot for every page in the url array
            for i in range(6):
                name = screenshot_name[i] + '.png'
                self._browser.get(url[i])
                time.sleep(3.0)
                self._browser.save_screenshot('images/GBserver3/new/' + param[2] + '/' + param[3] +'/' + name)
        else:
            #make base directories for tarheelreader with browser version'
            if len(param) == 5:
                if not os.path.exists('images'):
                    os.makedirs('images')
                if not os.path.exists('images/tarheelreader/new/'):
                    os.makedirs('images/tarheelreader/new/')
                if not os.path.exists('images/tarheelreader/new/' + param[2]):
                    os.makedirs('images/tarheelreader/new/' + param[2])
                if not os.path.exists('images/tarheelreader/new/' + param[2] +'/' + param[3] + param[4]):
                    os.makedirs('images/tarheelreader/new/' + param[2] +'/' + param[3] + param[4])
            else:
            #make base directories for tarheelreader without browser version'
                if not os.path.exists('images'):
                    os.makedirs('images')
                if not os.path.exists('images/tarheelreader/new/'):
                    os.makedirs('images/tarheelreader/new/')
                if not os.path.exists('images/tarheelreader/new/' + param[2]):
                    os.makedirs('images/tarheelreader/new/' + param[2])
                if not os.path.exists('images/tarheelreader/new/' + param[2] +'/' + param[3]):
                    os.makedirs('images/tarheelreader/new/' + param[2] +'/' + param[3])
        
            url = ['http://tarheelreader.org/2013/11/18/tarheelreadertestbook/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/2/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/3/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/4/', 'http://tarheelreader.org/2013/11/18/tarheelreadertestbook/5/']
        
            screenshot_name = ['title', 'page2', 'page3', 'page4', 'page5_japanese']
            
            #takes a screenshot for every page in the url array
            for i in range(5):
                name = screenshot_name[i] + '.png'
                self._browser.get(url[i])
                time.sleep(3.0)
                self._browser.save_screenshot('images/tarheelreader/new/' + param[2] + '/' + param[3] +'/' + name)
            
    def tearDown(self):
        time.sleep(5.0)
        #formats output with browser version
        if len(param) == 5:
            print '\nTest: ' + param[0]
            print 'URL: ' + param[1]
            print 'Platform: ' + param[2]
            print 'Browser: ' + param[3]
            print 'Version: ' + param[4]
        
        else:
            #formats output without browser version
            print '\nTest: ' + param[0]
            print 'URL: ' + param[1]
            print 'Platform: ' + param[2]
            print 'Browser: ' + param[3]
        self._browser.quit()
        
if __name__ == '__main__':
    param = []
    #python Unittest requires an empty array.  So save the current paramters, then delete them.
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
    
