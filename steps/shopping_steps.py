from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@given('I am on the inventory page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)


@when('I add the first product to the cart')
def step_impl(context):
    context.inventory_page.add_first_product_to_cart()


@then('I should see the cart badge with count 1')
def step_impl(context):
    badge_text = context.inventory_page.get_cart_badge_text()
    assert badge_text == "1", f"Expected badge count '1', got '{badge_text}'"


@when('I add a product to the cart')
def step_impl(context):
    context.inventory_page.add_first_product_to_cart()


@when('I open the cart')
def step_impl(context):
    context.cart_page = context.inventory_page.go_to_cart()


@then('I should see the product in the cart')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    product = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )
    product_name = product.text
    assert len(product_name) > 0, "No product found in cart"