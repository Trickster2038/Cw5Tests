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
PROFILE_MODERATION_STATUS = (By.XPATH, """//*[@class="card-body"]//p[7]""")
PROFILE_BIO = (By.XPATH, """//div[@class="card-body"]//p[6]""")
PROFILE_COURSE = (By.XPATH, """//div[@class="card-body"]//p[5]""")
PROFILE_AVATAR_BTN = (By.CSS_SELECTOR, 'a[href="/avatar/"]')
PROFILE_VERIFY_PHOTO_BTN = (By.CSS_SELECTOR, 'a[href="/verify/"')
PROFILE_EDIT_BTN = (By.CSS_SELECTOR, 'a[href="/edit/"]')
EDIT_BIO_FIELD = (By.ID, 'id_bio')
EDIT_COURSE_FIELD = (By.ID, 'id_course')
FILE_INPUT = (By.CSS_SELECTOR, 'input[type="file"]')
SUBMIT_BTN = (By.CSS_SELECTOR, 'input[type="submit"]')

NAV_SWITCH_LOCALE = (By.CSS_SELECTOR, 'a[href="/setlanguage/"]')
# .card > * > * > input[type="checkbox"]