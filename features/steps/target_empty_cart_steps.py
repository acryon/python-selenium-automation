from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[data-test='@web/CartLink']"))).click()


@then('Verify "Your cart is empty" message is shown')
def verify_cart_is_empty(context):
    actual_text= context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg']").text
    assert 'Your cart is empty' in actual_text, f'Error! The cart is not empty'


@when('Verify sign in is clickable')
def click_sign_in(context):
   context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()


@then('Verify sign in is clickable from right side navigation menu')
def sign_in_side_navigation(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='accountNav-signIn']"))).click()


@then('Verify "Sign into your Target account" message is shown')
def verify_message(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'