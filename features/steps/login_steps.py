from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given('I am on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I login with valid username and password')
def step_impl(context):
    context.inventory_page = context.login_page.login(
        "standard_user", "secret_sauce"
    )


@then('I should be logged in successfully')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )


@then('I should see the inventory page')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_container")
        )
    )


@when('I login with invalid username and password')
def step_impl(context):
    context.login_page.login("standard_user", "secret_sauce_fail")


@then('I should see an error message')
def step_impl(context):
    wait = WebDriverWait(context.driver, 5)
    try:
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".error-button")
            )
        )
    except TimeoutException:
        raise AssertionError("Error message did not appear")


@then('I should remain on the login page')
def step_impl(context):
    wait = WebDriverWait(context.driver, 5)
    wait.until(
        EC.presence_of_element_located(
            (By.ID, "user-name")
        )
    )