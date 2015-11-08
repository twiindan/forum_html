from selenium import webdriver
from page_object import Homepage
from nose.tools import assert_equals
import requests


class create_forum_message_test():

    def setUp(self):
        self.browser = webdriver.Firefox()
        requests.get('http://localhost:8081/v1.0/reset')

    def create_forum_message_test(self):

        #Define the table data
        table_data = [u'First Message with Page Object', u"Yes! I'm using Page Objects!"]

        #Initialize PageObject (HomePage)
        homepage = Homepage(self.browser)

        #Navigate to the Home Page
        homepage.navigate()

        #Click on New Forum Message Link
        new_forum_message = homepage.go_new_forum_message()

        #Fill all the data
        new_forum_message.fill_theme('Automation')
        new_forum_message.fill_subject(table_data[0])
        new_forum_message.fill_message(table_data[1])
        forum_list = new_forum_message.click_button()
        
        #Assert the forum list messages
        assert_equals(forum_list.get_table_data(), table_data)

    def tearDown(self):
        self.browser.close()
