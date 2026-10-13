class CartPage:
    PRODUCT_NAME_IN_CART = ("xpath", "//div[@class='cart_item']//div[@class='inventory_item_name']")
    REMOVE_BUTTON = ("xpath", "//button[contains(@class, 'btn_medium')]")
    CHECKOUT_BUTTON = ("id", "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 10)
        product = wait.until(EC.presence_of_element_located(self.PRODUCT_NAME_IN_CART))
        return product.text

    def remove_product(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 10)
        remove_btn = wait.until(EC.element_to_be_clickable(self.REMOVE_BUTTON))
        remove_btn.click()
        return self

    def proceed_to_checkout(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 10)
        checkout_btn = wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_btn.click()
        return self