import time
from selenium.webdriver.common.by import By
from helper.helper import WaitHelper


class ProductPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait_helper = WaitHelper(self.driver, 5)

    cart_btn = (By.XPATH, "//span[contains(text(),'Add to Cart')]")
    close_ship_from_overseas = (By.XPATH, "//span[@class='sfo__close']")
    added_to_cart_success = (
        By.XPATH, "//span[contains(text(),'Added to cart successfully!')]")

    def click_add_to_cart(self):
        try:
            self.wait_helper.wait_for_element_visible(
                self.close_ship_from_overseas)
            self.driver.find_element(*self.close_ship_from_overseas).click()
            print("Product From Overseas")
        except Exception as e:
            print("Not overseas Products")
        self.wait_helper.wait_for_element_visible(self.cart_btn)
        self.driver.find_element(*self.cart_btn).click()
        self.wait_helper.wait_for_element_visible(self.added_to_cart_success)
        print("Added to Cart")

    def swith_to_parent_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
