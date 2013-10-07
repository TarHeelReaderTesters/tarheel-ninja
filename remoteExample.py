from selenium import webdriver

driver=webdriver.Remote("http://152.23.20.86:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX)
driver.get('http://www.google.com')
driver.get_screenshot_as_file('/home/dallara/Desktop/google.png')
driver.quit()
