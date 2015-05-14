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
        return NewMessageForumTest(self.driver)

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


class NewMessageForumTest(BasePage):
    url = "http://localhost:8081/v1.0/forum/new"

    def fill_theme(self, theme):
        Select(self.driver.find_element_by_id('theme')).select_by_visible_text(theme)

    def fill_subject(self, subject):
        self.driver.find_element_by_id('subject').send_keys(subject)

    def fill_message(self, message):
        self.driver.find_element_by_id('message').send_keys(message)

    def click_button(self):
        self.driver.find_element_by_id('save').click()
        return MessageListPage(self.driver)

    def fill_all_form(self, theme, subject, message):

        self.fill_theme(theme)
        self.fill_subject(subject)
        self.fill_message(message)
        self.click_button()
        return MessageListPage(self.driver)


class MessageListPage(BasePage):

    url = "http://localhost:8081/v1.0/users/"

    def get_table_data(self):

        forum_data_list = []
        forum_table = self.driver.find_element_by_xpath(".//*[@id='forum_table']/tbody")
        rows = forum_table.find_elements_by_tag_name('tr')

        forum_data_list.append(rows[0].find_elements_by_tag_name('th')[0].text)
        forum_data_list.append(rows[1].find_elements_by_tag_name('td')[0].text)
        return forum_data_list
