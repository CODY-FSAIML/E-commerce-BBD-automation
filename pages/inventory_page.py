from pages.cart_page import CartPage


class InventoryPage:
    ADD_TO_CART_BUTTON = ("xpath", "//button[contains(@class, 'btn_primary')]")
    PRODUCT_NAME = ("xpath", "//div[@class='inventory_item_name']")
    CART_BADGE = ("class name", "shopping_cart_badge")
    CART_LINK = ("class name", "shopping_cart_link")
    PRODUCT_LIST = ("xpath", "//div[@class='inventory_item']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com")
        return self

    def add_first_product_to_cart(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By

        wait = WebDriverWait(self.driver, 10)
        add_btn = wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        add_btn.click()
        return self

    def get_cart_badge_text(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 10)
        badge = wait.until(EC.presence_of_element_located(self.CART_BADGE))
        return badge.text

    def go_to_cart(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 10)
        cart_link = wait.until(EC.element_to_be_clickable(self.CART_LINK))
        cart_link.click()
        return CartPage(self.driver)

    def get_product_names(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 10)
        products = wait.until(EC.presence_of_all_elements_located(self.PRODUCT_LIST))
        return [p.text for p in products]