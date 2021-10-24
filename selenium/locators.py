from selenium.webdriver.common.by import By

LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/login/"]')
LOGIN_ID_FIELD_LOCATOR = (By.ID, 'id_username')
PASSWORD_FIELD_LOCATOR = (By.ID, 'id_password')
LOGIN_FORM_BTN_LOCATOR = (By.CSS_SELECTOR, 'button[type="submit"]')
LOGOUT_BTN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/logout/"]')

TAB_OUT_LOCATOR = (By.CSS_SELECTOR, 'a[href="/outgoing/"]')
TAB_IN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/incoming/"]')
TAB_FRIENDS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/friends/"]')
TAB_SEARCH_LOCATOR = (By.CSS_SELECTOR, 'a[href="/search?safe=false"]')
TAB_SAFESEARCH_LOCATOR = (By.CSS_SELECTOR, 'a[href="/search?safe=true"]')
TAB_MODERATE_LOCATOR = (By.CSS_SELECTOR, 'a[href="/moderate/"]')

NAV_ACCOUNT_LOCATOR = (By.CSS_SELECTOR, 'a[href="/profile/"')
PROFILE_CURATOR_CHECKBOX = (By.ID, 'curator-checkbox')
PROFILE_CURATOR_BTN = (By.CSS_SELECTOR, 'a[href="/switchCurator/"')
# .card > * > * > input[type="checkbox"]