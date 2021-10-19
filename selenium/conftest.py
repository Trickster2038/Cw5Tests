from selenium import webdriver
import locators
import pytest
from testdb import  init_test_db
from selenium.common.exceptions import ElementClickInterceptedException

@pytest.fixture(scope='function', autouse=True)
def init_db():
    init_test_db()

@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito") # user is not authed in this mode
    browser = webdriver.Chrome(executable_path="./chromedriver", \
        options=chrome_options)
    try:
        browser.get("http://localhost:8000/")
        browser.implicitly_wait(10) # set wait for elemnts load if it is needed
        browser.maximize_window() # all tabs are on the screen
        login_btn = browser.find_element(*locators.LOGIN_BTN_LOCATOR)
        login_btn.click()
        id_field = browser.find_element(*locators.LOGIN_ID_FIELD_LOCATOR)
        id_field.send_keys("421423205")
        pass_field = browser.find_element(*locators.PASSWORD_FIELD_LOCATOR)
        pass_field.send_keys("Fz12481632")
        login_btn = browser.find_element(*locators.LOGIN_FORM_BTN_LOCATOR)
        login_btn.click()
        yield browser
    finally:
        browser.quit()
