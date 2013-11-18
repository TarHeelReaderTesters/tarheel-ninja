import unittest
from PIL import ImageChops
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

#testing screenshots

def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None


'''browser = webdriver.Firefox()
browser.get('http://www.google.com/')
browser.implicitly_wait(2)
browser.save_screenshot('C:\Users\estradr\Desktop\screenTests\screenie.png')
browser.quit()'''

old = Image.open('C:\Users\estradr\Desktop\screenTests\screenieRef.png')
new = Image.open('C:\Users\estradr\Desktop\screenTests\screenieWrong.png')

if equal(old,new):
        print "the same"
else:
        print "NOT the same"