from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import locators
import time
import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def click_card_btn(browser: WebDriver, tab_locator, btn_locator):
    tab = browser.find_element(*tab_locator)
    tab.click()
    btn = browser.find_element(*btn_locator)
    btn.click()
    browser.implicitly_wait(0)
    WebDriverWait(browser, 5).until_not(
        EC.visibility_of_element_located(btn_locator)
    )
    browser.refresh()
    WebDriverWait(browser, 3).until_not(
        EC.presence_of_element_located(btn_locator)
    )
    assert 0 == len(browser.find_elements(*btn_locator))
    browser.implicitly_wait(10)


@pytest.mark.skip("skip")
def test_login(browser: WebDriver):
    assert len(browser.find_elements(*locators.LOGOUT_BTN_LOCATOR)) != 0

@pytest.mark.skip("skip")
def test_logout(browser: WebDriver):
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
def test_tabs(browser: WebDriver, tab_locator, page_url):
    tab = browser.find_element(*tab_locator)
    tab.click()
    assert browser.current_url.count(page_url) == 1

"""
1 - add Aleksandr Petrov
2 - delete him from friends
"""
@pytest.mark.skip("skip")
def test_accept_delete_friend(browser: WebDriver):
    browser.implicitly_wait(0.5)
    accept_btn_locator = (By.CSS_SELECTOR, """button[onclick="send_ajax(4, 'accept_incoming')"]""")
    click_card_btn(browser, locators.TAB_IN_LOCATOR, accept_btn_locator)
    delete_btn_locator = (By.CSS_SELECTOR, \
        """button[onclick="send_ajax(4, 'delete_friend')"]""")
    click_card_btn(browser, locators.TAB_FRIENDS_LOCATOR, delete_btn_locator)



@pytest.mark.skip("skip")
@pytest.mark.parametrize(
        'tab_locator, btn_onclick',
        [
            pytest.param(locators.TAB_OUT_LOCATOR, "send_ajax(1, 'delete_outgoing')"),
            pytest.param(locators.TAB_IN_LOCATOR, "send_ajax(3, 'delete_incoming')"),
            pytest.param(locators.TAB_SEARCH_LOCATOR, "send_ajax(7, 'send_subscribe_request')"),
            pytest.param(locators.TAB_SAFESEARCH_LOCATOR, "send_ajax(5, 'send_subscribe_request')"),
        ]
    )
def test_delete_or_subscribe_cards(browser: WebDriver, tab_locator, btn_onclick):
    btn_locator = (By.CSS_SELECTOR, f"""button[onclick="{btn_onclick}"]""")
    click_card_btn(browser, tab_locator, btn_locator)

@pytest.mark.skip("skip")
@pytest.mark.parametrize(
        'btn_onclick, status',
        [
            pytest.param("send_ajax(1, 'confirm_moderation')", "проверен"),
            pytest.param("send_ajax(1, 'discard_moderation')", "не проверен"),
        ]
    )
def test_moderate(browser: WebDriver, btn_onclick, status):
    tab_out = browser.find_element(*locators.TAB_OUT_LOCATOR)
    tab_out.click()
    moder_status = browser.find_element(By.XPATH, """//*[@id="card-1"]//p[5]""")
    assert moder_status.text.lower().count("на проверке") == 1
    tab_moderate = browser.find_element(*locators.TAB_MODERATE_LOCATOR)
    tab_moderate.click()
    btn_locator = (By.CSS_SELECTOR, f"""button[onclick="{btn_onclick}"]""")
    btn = browser.find_element(*btn_locator)
    btn.click()
    tab_out = browser.find_element(*locators.TAB_OUT_LOCATOR)
    tab_out.click()
    moder_status = browser.find_element(By.XPATH, """//*[@id="card-1"]//p[5]""")
    assert moder_status.text.lower().count(status) == 1

@pytest.mark.skip("skip")
def test_switch_mode(browser: WebDriver):
    nav_account = browser.find_element(*locators.NAV_ACCOUNT_LOCATOR)
    nav_account.click()
    curator_checkbox = browser.find_element(*locators.PROFILE_CURATOR_CHECKBOX)
    checkbox_prev_state = curator_checkbox.is_selected()
    switch_mode_btn = browser.find_element(*locators.PROFILE_CURATOR_BTN)
    switch_mode_btn.click()
    curator_checkbox = browser.find_element(*locators.PROFILE_CURATOR_CHECKBOX)
    assert not checkbox_prev_state == curator_checkbox.is_selected()

@pytest.mark.parametrize(
        'form_btn_locator, status',
        [
            pytest.param(locators.PROFILE_AVATAR_BTN, "не проверен"),
            pytest.param(locators.PROFILE_VERIFY_PHOTO_BTN, "на проверке"),
        ]
    )
def test_photo_upload(browser: WebDriver, form_btn_locator, status):
    nav_account = browser.find_element(*locators.NAV_ACCOUNT_LOCATOR)
    nav_account.click()
    moder_status = browser.find_element(*locators.PROFILE_MODERATION_STATUS)
    assert moder_status.text.lower().count("проверен") == 1
    avatar_btn = browser.find_element(*form_btn_locator)
    avatar_btn.click()
    file_input = browser.find_element(*locators.FILE_INPUT)
    file_input.send_keys(os.path.abspath("./media/upload.png"))
    submit_btn = browser.find_element(*locators.SUBMIT_BTN)
    submit_btn.click()
    moder_status = browser.find_element(*locators.PROFILE_MODERATION_STATUS)
    assert moder_status.text.lower().count(status) == 1

    