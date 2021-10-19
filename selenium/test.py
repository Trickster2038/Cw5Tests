from selenium import webdriver
import locators
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skip("skip")
def test_login(browser):
    assert len(browser.find_elements(*locators.LOGOUT_BTN_LOCATOR)) != 0

@pytest.mark.skip("skip")
def test_logout(browser):
    logout_btn = browser.find_element(*locators.LOGOUT_BTN_LOCATOR)
    logout_btn.click()
    assert len(browser.find_elements(*locators.LOGIN_BTN_LOCATOR)) != 0

@pytest.mark.skip("skip")
@pytest.mark.parametrize(
        'tab_locator, page_url',
        [
            pytest.param(locators.TAB_OUT_LOCATOR, '/outgoing'),
            pytest.param(locators.TAB_IN_LOCATOR, '/incoming'),
            pytest.param(locators.TAB_FRIENDS_LOCATOR, '/friends'),
            pytest.param(locators.TAB_SEARCH_LOCATOR, '/search/?safe=false'),
            pytest.param(locators.TAB_SAFESEARCH_LOCATOR, '/search/?safe=true'),
            pytest.param(locators.TAB_MODERATE_LOCATOR, '/moderate'),
        ]
    )
def test_tabs(browser, tab_locator, page_url):
    tab = browser.find_element(*tab_locator)
    tab.click()
    assert browser.current_url.count(page_url) == 1