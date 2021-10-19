from selenium import webdriver
import locators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(browser):
    assert len(browser.find_elements(*locators.LOGOUT_BTN_LOCATOR)) != 0

def test_logout(browser):
    logout_btn = browser.find_element(*locators.LOGOUT_BTN_LOCATOR)
    logout_btn.click()
    assert len(browser.find_elements(*locators.LOGIN_BTN_LOCATOR)) != 0

def test_tabs(browser):
    pass