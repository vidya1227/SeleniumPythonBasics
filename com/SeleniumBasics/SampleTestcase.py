import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("http://demoaut.katalon.com/")
driver.maximize_window()
print(driver.title) # Title of the page

# ---------->>Home page Click on make appointment button , it ll navigate to login page
print('Navigate to the login page')
ele_Btn_MakeAppointment = driver.find_element_by_xpath('//*[@id="btn-make-appointment"]').click()
print('Navigation is successfull')

#Login to the website ------>>> Login page --->> LOgin with username and password
print('Login as User to the application')
ele_Txt_Username = driver.find_element_by_xpath('//*[@id="txt-username"]').send_keys('John Doe')
ele_Txt_Password = driver.find_element_by_xpath('//*[@id="txt-password"]').send_keys('ThisIsNotAPassword')
ele_Btn_Login = driver.find_element_by_xpath('//*[@id="btn-login"]').click()
print('Login is successfull!')

#----Make Appointment page----->>>>>> Add details--------------------------------------------------------------
print('Add details to make appointment page')
ele_Pop_Facility = driver.find_element_by_xpath('//*[@id="combo_facility"]')
#Dropdown Selection in python selenium
dropDown = Select(ele_Pop_Facility)
#Select by visible text
#dropDown.select_by_visible_text('Tokyo CURA Healthcare Center')
#select by index
#dropDown.select_by_index(2)
#Select by using value
dropDown.select_by_value('Seoul CURA Healthcare Center')

# Checkbox 'Apply for hospital readmission'
ele_Chk_HospitalReadmission = driver.find_element_by_xpath('//*[@id="chk_hospotal_readmission"]').click()

# Radio Button
ele_RBtn_HealthcareProgram = driver.find_element_by_xpath('//*[@id="appointment"]/div/div/form/div[3]/div/label[2]').click()

#Date Window box
ele_VisitDate = driver.find_element_by_xpath('//*[@id="appointment"]/div/div/form/div[4]/div/div').click()
ele_Date = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[5]/td[2]').click()

# Comment Text field
ele_Txt_Comment = driver.find_element_by_xpath('//*[@id="txt_comment"]').send_keys('I want appointment for meadicare details')

# Book Appointment Button to book appointment
ele_Btn_BookAppointment = driver.find_element_by_xpath('//*[@id="btn-book-appointment"]').click()

time.sleep(3) # sleep in python
print('Details are added successfully to make appointment page')

#------------>>>Apointment confirmation page-----------------------------------------------------
print('confirmation page is displayed, and clicking on "Go To Home Page" button')
# Book Appointment Button to book appointment
ele_Btn_GoToHomePage = driver.find_element_by_xpath('//*[@id="summary"]/div/div/div[7]/p/a').click()
print('Home page is displayed')

#----------Home Page-----------------------------------------------------------------------------
print('Logout from application')
#Menu in home page
ele_Btn_Menu = driver.find_element_by_xpath('//*[@id="menu-toggle"]/i').click()

#---------------------------User logout----------------------------------------------------------
# logout Option in Menu list
ele_Btn_Logout = driver.find_element_by_xpath('//*[@id="sidebar-wrapper"]/ul/li[5]/a').click()
print('Logout is successfull')

#----------------Quit browser-----------------------------------------------------------------------
print(driver.title)
driver.close() # Close the  cureently  focused browser
driver.quit() # closes all the browser

print('Test completed Successfully')