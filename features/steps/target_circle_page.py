from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CIRCLE_TARGET = (By.CSS_SELECTOR, "[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")
DEALS_TARGET = (By.CSS_SELECTOR, "div[class*='styles__CellsComponentContainer']")

@when('click on Target Circle')
def click_target_circle(context):
    context.driver.find_element(*CIRCLE_TARGET).click()
    sleep(7)


@then('Verify there are {expected_amount} deals links')
def verify_deals(context, expected_amount):
    expected_amount = int(expected_amount)
    deal_links = context.driver.find_elements(*DEALS_TARGET)
    assert len(deal_links) == expected_amount, f'Expected {expected_amount} deals links but got {len(deal_links)}'
