import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os


fn = os.path.join(os.path.abspath(os.pardir), 'Screenshots')

print(fn)
driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("http://demoaut.katalon.com/")
driver.maximize_window()
print(driver.title) # Title of the page
#driver.save_screenshot('E:\\VidyaWorkspace\\PythonWorkspace\\PythonProjects\\SeleniumPythonBasics\\Screenshos\\Snap1.png')

driver.save_screenshot(fn+'\snap3.png')
#
#
# fileName = str(round(time.time() * 1000)) + "Snap9.png"
# screenshotDirectory = "Screenshots/"
# relativeFileName = screenshotDirectory + fileName
# currentDirectory = os.path.dirname(__file__)
# destinationFile = os.path.join(currentDirectory, relativeFileName)
# destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
# print(destinationFile)
# driver.save_screenshot(destinationFile)


#driver.get_screenshot_as_png()
#driver.get_screenshot_as_file('E:\\VidyaWorkspace\\PythonWorkspace\\PythonProjects\\SeleniumPythonBasics\\Screenshos\\Snap1.jpeg')

driver.close()