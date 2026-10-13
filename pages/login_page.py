from pages.inventory_page import InventoryPage


class LoginPage:
    URL = "https://www.saucedemo.com"

    USERNAME_FIELD = ("id", "user-name")
    PASSWORD_FIELD = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return InventoryPage(self.driver)