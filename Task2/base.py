from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base:
    def __init__(self):
        self.driver = self.init_driver()

    def init_driver(self):
        options = Options()
        # options.page_load_strategy = "eager"
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        # Optional: Disable extensions for stability
        options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.daraz.com.np/")
        return driver
