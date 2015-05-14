__author__ = 'arobres'
from selenium import webdriver
from page_object import Homepage
from nose.tools import assert_equals


class create_user_test():

    def setUp(self):
        self.browser = webdriver.Firefox()

    def create_user_test(self):

        table_headings = [u'username', u'password', u'role', u'name', u'email']
        table_data = [u'expoqa', u'expoqa', u'QA', u'expoqa', u'expoqa@expoqa.com']
        homepage = Homepage(self.browser)
        homepage.navigate()
        new_user_page = homepage.go_new_user()
        new_user_page.fill_name('expoqa')
        new_user_page.fill_username('expoqa')
        new_user_page.fill_password('expoqa')
        new_user_page.fill_role('QA')
        new_user_page.fill_email('expoqa@expoqa.com')
        user_list_page = new_user_page.click_button()

        assert_equals(user_list_page.get_table_headers(), table_headings)
        assert_equals(user_list_page.get_table_data()[0], table_data)

    def tearDown(self):
        self.browser.close()