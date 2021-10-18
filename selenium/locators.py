from selenium.webdriver.common.by import By

LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/login/"]')
LOGIN_ID_FIELD_LOCATOR = (By.ID, 'id_username')
PASSWORD_FIELD_LOCATOR = (By.ID, 'id_password')
LOGIN_FORM_BTN_LOCATOR = (By.CSS_SELECTOR, 'button[type="submit"]')
LOGOUT_BTN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/logout/"]')
