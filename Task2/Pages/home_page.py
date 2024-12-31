from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base import Base
from helper.helper import WaitHelper
from Pages.login_page import LoginPage
from Pages.search_results_page import SearchResultsPage


class HomePage(Base):
    def __init__(self, ):
        super().__init__()
        self.wait_helper = WaitHelper(self.driver, 10)

    login_button = (By.XPATH, "//div[@id='anonLogin']/a")
    # logged in details
    username_display = (By.XPATH, "//span[@id='myAccountTrigger']")
    # search
    search_box = (By.ID, "q")

    def get_page_title(self):
        return self.driver.title

    def search_item(self, item):
        search_element = self.driver.find_element(*self.search_box)
        search_element.clear()
        search_element.send_keys(item)
        search_element.send_keys(Keys.ENTER)

    def click_login(self):
        login_element = self.driver.find_element(*self.login_button)
        login_element.click()
        return LoginPage(self.driver)

    def verify_logged_in(self, username):
        self.wait_helper.wait_for_element_visible(self.username_display)
        actual_username = self.driver.find_element(*self.username_display).text
        assert username in actual_username.lower(), "Logged in with different username"

    def search(self, searched_text):
        self.driver.find_element(
            *self.search_box).send_keys(searched_text + Keys.RETURN)
        return SearchResultsPage(self.driver)
