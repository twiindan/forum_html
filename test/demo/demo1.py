__author__ = 'arobres'


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from nose.tools import assert_equals


#DEFINE DATA
user_data = ['vlctesting', 'vlctesting', 'QA', 'vlctesting', 'vlctesting@vlctesting.es', ]
table_headers = ['username', 'password', 'role', 'name', 'email']

#INIT THE FIREFOX WEBDRIVER
driver = webdriver.Firefox()

#SET IMPLICIT WAIT TO 10 SECONDS
driver.implicitly_wait(10)

#GET THE MAIN PAGE
driver.get("http://localhost:8081/v1.0")

#ASSERT THE MAIN PAGE IS OPENED
header = driver.find_element_by_id('header_first_time')
assert_equals(header.text, 'Welcome to VLC Testing Python Forum')

#LOCATE AND CLICK IN THE FIRST LINK
new_user_link = driver.find_element_by_link_text('Create a new user')
new_user_link.click()

#LOCATE ALL THE ELEMENTS
name = driver.find_element_by_id('name')
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
email = driver.find_element_by_id('email')
role = Select(driver.find_element_by_id('role'))
button = driver.find_element_by_id('save')


#FILL ALL THE FORM AND CLICK ON BUTTON
username.send_keys(user_data[0])
password.send_keys(user_data[1])
role.select_by_visible_text(user_data[2])
name.send_keys(user_data[3])
email.send_keys(user_data[4])
button.click()

#LOCATE THE TABLE
user_table = driver.find_element_by_xpath(".//*[@id='user_table']/tbody")

#LOCATE THE ROWS AND HEADERS
rows = user_table.find_elements_by_tag_name('tr')
header_columns = rows[0].find_elements_by_tag_name('th')

#ASSERT THE HEADERS
for x in range(len(header_columns)):
    assert_equals(header_columns[x].text, table_headers[x])

#ASSERT THE ROWS
for x in range(1, len(rows)):
    columns = rows[x].find_elements_by_tag_name('td')

    for i in range(len(columns)):
        assert_equals(columns[i].text, user_data[i])

#CLOSE THE WINDOW
driver.close()