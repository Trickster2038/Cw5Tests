from selenium import webdriver
import locators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(browser):
    time.sleep(1)
    assert len(browser.find_elements(*locators.LOGOUT_BTN_LOCATOR)) != 0
