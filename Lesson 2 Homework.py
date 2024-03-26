#Lesson 2 Homework: Locators

#Amazon Logo, search by aria-label="Amazon"
#Email field, search by id="ap_email"
#Continue button, search by id="continue-announce"
#Condition of use link, search by id="legalTextRow"
#Privacy Notice link, search by id="legalTextRow"
#Need help link, search by class="a-expander-prompt"
#Forgot password link, search by id="auth-fpp-link-bottom"
#Other issues with signin link, search by id="ap-other-signin-issues-link"
#Create your Amazon account button, search by id="createAccountSubmit"


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# Enter 'dog food' in search field
driver.find_element(By.ID, 'search').send_keys('dog food')

# Click search button
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()

# Wait 7 seconds
sleep(7)

# Verification
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert 'dog food' in actual_text, f'Error! Text dog food not in {actual_text}'
print('Test case passed.')

driver.quit()
