from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CLICK_ITEM = (By.ID, 'addToCartButtonOrTextIdFor89302941')
ITEM_IN_CART = (By.CSS_SELECTOR, "a[href*='poppi-strawberry-lemon-prebiotic-soda']")


@when('Search for {item}')
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BUTTON).click()



@then('Add {item} to cart')
def add_to_cart(context,item):
    context.driver.find_element(*CLICK_ITEM).click()
sleep(10)


@then('Verify item in cart')
def verify_cart(context):
    actual_text = context.driver.find_element(*ITEM_IN_CART).text
    expected_text = 'Poppi Strawberry Lemon Prebiotic Soda'
    assert actual_text == actual_text, f'Expected: {expected_text}, but got {actual_text}'