import time
from selenium.webdriver.common.by import By
from Pages.product_page import ProductPage
from helper.helper import WaitHelper


class SearchResultsPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait_helper = WaitHelper(self.driver, 10)

    product_titles = (By.XPATH, "//div[@class='RfADt']/a")
    product_prices = (By.CSS_SELECTOR, ".ooOxS")
    min_price_filter = (By.XPATH, "//div[@class='_1lPeN']/input[1]")
    max_price_filter = (By.XPATH, "//div[@class='_1lPeN']/input[2]")
    filter_price_btn = (By.XPATH, "//div[@class='_1lPeN']/button")
    # Searched Product Locators
    products_id = []
    product_with_rating = (By.XPATH, "//div[@class='mdmmT _32vUv']")
    no_of_ratings = ".//i[contains(@class, '_9-ogB') and contains(@class, 'Dy1nx')]"

    def verify_brand_in_titles(self, brand):
        titles = self.driver.find_elements(*self.product_titles)
        for title in titles[:5]:
            print(title.text)
            assert brand.lower() in title.text.lower(
            ), f"Brand {brand} not found in {title.text}"

    def apply_price_filter(self, max_price, min_price):
        self.wait_helper.scroll_into_view(self.min_price_filter)
        self.driver.find_element(*self.min_price_filter).send_keys(min_price)
        self.driver.find_element(*self.max_price_filter).send_keys(max_price)
        self.driver.find_element(*self.filter_price_btn).click()

    def check_product_with_rating_four_plus(self):
        all_products_with_rating = self.driver.find_elements(
            *self.product_with_rating)
        for product_ratings in all_products_with_rating:
            rating = product_ratings.find_elements(
                By.XPATH, self.no_of_ratings)
            print(f"Product Rating: {len(rating)}")
            if len(rating) >= 4:
                main_product = product_ratings.find_element(
                    By.XPATH, "ancestor::div[contains(@class, 'Bm3ON')]")
                print(main_product.get_attribute("data-item-id"))
                self.products_id.append(
                    main_product.get_attribute("data-item-id"))
        return self.products_id

    def open_single_product(self, product_id):
        self.wait_helper.scroll_into_view(
            (By.XPATH, f"//div[@data-item-id='{product_id}']//a"))
        product_link = self.driver.find_element(
            By.XPATH, f"//div[@data-item-id='{product_id}']//a")
        self.driver.execute_script(
            "window.open(arguments[0].getAttribute('href'), '_blank');", product_link)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return ProductPage(self.driver)
