__author__ = 'arobres'


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from nose.tools import assert_equals
import requests
requests.get('http://localhost:8081/v1.0/reset')


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
new_user_link = driver.find_element_by_link_text('Create new forum message')
new_user_link.click()

#LOCATE THE THEME ELEMENT (IS A COMBOBOX) THE ID IS 'theme'
theme = Select(driver.find_element_by_id('theme'))

#SELECT VALUE (AUTOMANTION)
theme.select_by_visible_text('Automation')

#LOCATE THE SUBJECT ELEMENT. THE ID IS 'subject'
subject = driver.find_element_by_id('subject')

#SEND KEYS TO THE SUBJECT ELEMENT
subject.send_keys(subject_data)

#LOCATE THE MESSAGE ELEMENT. THE ID IS 'message'
message = driver.find_element_by_id('message')

#SEND KEYS TO THE SUBJECT ELEMENT
message.send_keys(message_data)

#LOCATE THE BUTTON (ID=save) AND CLICK IT
save_button = driver.find_element_by_id('save')
save_button.click()

#LOCATE THE TABLE
forum_table = driver.find_element_by_xpath(".//*[@id='forum_table']/tbody")

#LOCATE THE ROWS AND HEADERS
rows = forum_table.find_elements_by_tag_name('tr')
header_columns = rows[0].find_elements_by_tag_name('th')

#ASSERT THE HEADERS
for x in range(1):
    assert_equals(header_columns[x].text, subject_data)

#ASSERT THE ROWS
for x in range(1, len(rows)):
    columns = rows[x].find_elements_by_tag_name('td')

    for i in range(len(columns)):
        assert_equals(columns[i].text, message_data)

#CLOSE THE WINDOW
driver.close()
