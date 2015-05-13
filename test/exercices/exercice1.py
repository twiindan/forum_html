__author__ = 'arobres'


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from nose.tools import assert_equals


#DEFINE DATA

subject_data = 'First Message with Selenium!'
message_data = "I'm automating my first test with Python and Selenium!"

#INIT THE FIREFOX WEBDRIVER
driver = webdriver.Firefox()

#SET IMPLICIT WAIT TO 10 SECONDS
driver.implicitly_wait(10)

#GET THE MAIN PAGE
driver.get("http://localhost:8081/v1.0")

#ASSERT THE MAIN PAGE IS OPENED
header = driver.find_element_by_id('header_first_time')
assert_equals(header.text, 'Welcome to ExpoQA Python Forum')

#LOCATE AND CLICK IN THE FIRST LINK USING FIND ELEMENT BY LINK TEXT (Create new forum message) ()


#LOCATE THE THEME ELEMENT (IS A COMBOBOX) THE ID IS 'theme'


#SELECT VALUE (AUTOMANTION)


#LOCATE THE SUBJECT ELEMENT. THE ID IS 'subject'


#SEND KEYS TO THE SUBJECT ELEMENT


#LOCATE THE MESSAGE ELEMENT. THE ID IS 'message'


#SEND KEYS TO THE SUBJECT ELEMENT


#LOCATE THE BUTTON (ID=save) AND CLICK IT


#LOCATE THE TABLE


#LOCATE THE ROWS AND HEADERS


#ASSERT THE HEADERS


#ASSERT THE ROWS


#CLOSE THE WINDOW
driver.close()
