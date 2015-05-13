__author__ = 'arobres'
from selenium.webdriver.support.ui import Select


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)


class Homepage(BasePage):
    url = "http://localhost:8081/v1.0"

    def go_new_user(self):
        self.driver.find_element_by_link_text('Create a new user').click()
        return NewUserPage(self.driver)

    def go_new_forum_message(self):
        self.driver.find_element_by_link_text('Create new forum message').click()

    def go_user_list(self):
        self.driver.find_element_by_link_text('List users').click()

    def go_forum_messages_list(self):
        self.driver.find_element_by_link_text('List forum message').click()

    def get_header(self):
        return self.driver.find_element_by_id('header_first_time')


class NewUserPage(BasePage):
    url = "http://localhost:8081/v1.0/users/new"

    def fill_name(self, name):
        self.driver.find_element_by_id('name').send_keys(name)

    def fill_username(self, username):
        self.driver.find_element_by_id('username').send_keys(username)

    def fill_role(self, role):
        Select(self.driver.find_element_by_id('role')).select_by_visible_text(role)

    def fill_password(self, password):
        self.driver.find_element_by_id('password').send_keys(password)

    def fill_email(self, email):
        self.driver.find_element_by_id('email').send_keys(email)

    def click_button(self):
        self.driver.find_element_by_id('save').click()
        return UserListPage(self.driver)

    def fill_all_form(self, username, password, role, email, name):

        self.fill_username(username)
        self.fill_name(name)
        self.fill_password(password)
        self.fill_role(role)
        self.fill_email(email)
        self.click_button()
        return UserListPage(self.driver)


class UserListPage(BasePage):

    url = "http://localhost:8081/v1.0/users/"

    def get_table_headers(self):
        header_list = []
        user_table = self.driver.find_element_by_xpath(".//*[@id='user_table']/tbody")
        rows = user_table.find_elements_by_tag_name('tr')
        header_columns = rows[0].find_elements_by_tag_name('th')

        for x in range(len(header_columns)):
            header_list.append(header_columns[x].text)

        return header_list

    def get_table_data(self):
        user_data_list = []
        user_table = self.driver.find_element_by_xpath(".//*[@id='user_table']/tbody")
        rows = user_table.find_elements_by_tag_name('tr')

        for x in range(1, len(rows)):
            row_list = []
            columns = rows[x].find_elements_by_tag_name('td')

            for i in range(len(columns)):
                row_list.append(columns[i].text)

            user_data_list.append(row_list)
        return user_data_list