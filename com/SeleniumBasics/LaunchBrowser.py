from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")


#driver = webdriver.Firefox(executable_path="E:\geckodriver.exe")

driver = webdriver.Ie(executable_path="E:\IEDriverServer.exe")

driver.get("https://zeenyx.com/")

print(driver.title) # Title of the page

print(driver.current_url)

#print(driver.page_source) # gives the HTML source code

driver.close() # Close the browser
