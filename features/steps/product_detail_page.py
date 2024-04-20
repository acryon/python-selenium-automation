from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
COLOR_SELECTED = (By.CSS_SELECTOR,"[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(7)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Gray', 'Green', 'Heather Beige']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        color_selected = context.driver.find_element(*COLOR_SELECTED).text
        print('Current color', color_selected)

        color_selected = color_selected.split('\n')[1]
        actual_colors.append(color_selected)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
