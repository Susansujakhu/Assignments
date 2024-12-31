import time
from Pages.home_page import HomePage
import json

def get_credentials(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    credentials = get_credentials("Task2/credentials.json")
    mobile_no = credentials['mobile_no']
    password = credentials['password']
    max_price = 1499
    try:
        home_page = HomePage()
        # Log in
        login_page = home_page.click_login()
        # time.sleep(2)
        login_page.enter_login_details(mobile_no, password)
        # time.sleep(2)
        login_page.click_login_btn()
        # time.sleep(2)
        home_page.verify_logged_in("susan sujakhu")
        # time.sleep(2)
        # Search
        search_result_page = home_page.search("JBL")
        # time.sleep(2)
        search_result_page.verify_brand_in_titles("JBL")
        # time.sleep(2)
        # Apply filter
        search_result_page.apply_price_filter(max_price, min_price=0)
        # time.sleep(2)
        products_with_rating_four_plus = search_result_page.check_product_with_rating_four_plus()
        # time.sleep(2)
        # Add to cart
        for product in products_with_rating_four_plus:
            product_page = search_result_page.open_single_product(product)
            product_page.click_add_to_cart()
            product_page.swith_to_parent_window()
            time.sleep(5)
        print("Test Passed: Item added to cart successfully.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        print("Test Completed")
