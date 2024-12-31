from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    mobile_no_locator = (
        By.XPATH, "//input[@placeholder='Please enter your Phone Number or Email']")
    password_locator = (
        By.XPATH, "//input[@placeholder='Please enter your password']")
    modal_login_button = (By.XPATH, "//button[contains(@class,'iweb-button')]")

    def enter_login_details(self, mobile_no, password):
        self.driver.find_element(*self.mobile_no_locator).send_keys(mobile_no)
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.modal_login_button).click()
