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

    def go_new_forum_message(self):
        self.driver.find_element_by_link_text('Create new forum message').click()
        return NewMessageForumTest(self.driver)

    def go_user_list(self):
        self.driver.find_element_by_link_text('List users').click()

    def go_forum_messages_list(self):
        self.driver.find_element_by_link_text('List forum message').click()

    def get_header(self):
        return self.driver.find_element_by_id('header_first_time')


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
