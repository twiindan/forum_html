from selenium import webdriver
from page_object import Homepage
from nose.tools import assert_equals
import requests


class create_user_test():

    def setUp(self):
        self.browser = webdriver.Firefox()
        requests.get('http://localhost:8081/v1.0/reset')


    def create_user_test(self):

        #Define the table data
        table_data = [u'First Message with Page Object', u"Yes! I'm using Page Objects!"]

        #Initialize PageObject (HomePage)


        #Navigate to the Home Page


        #Click on New Forum Message Link


        #Fill all the data


        #Assert the forum list messages

    def tearDown(self):
        self.browser.close()
