from selenium.webdriver.common.by import By


class BasePageLocators:
    CART = (By.XPATH, '//span[@class="cart-link"]')
    FEEDBACK = (By.XPATH, '//div[@class="contact-num"]/a')
    SEARCH_FIELD = (By.XPATH, '//input[@id="ajax-search-text"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@id="ajax-search-btn"]')
    LOGIN_SIGNUP_MENU = (By.XPATH, '//span[@class="expand-more"]')
    SIGNUP = (By.XPATH, '//a[@href="https://oriontoys.shop/index.php?route=account/simpleregister"]')
    LOGIN = (By.XPATH, '//a[@href="https://oriontoys.shop/index.php?route=account/login"]')
    WISHLIST = (By.XPATH, '//span[@class="wishlist-text"]')
    LANGUAGE_MENU = (By.XPATH, '//button[@class="btn btn-link dropdown-toggle"]')
    LANGUAGE_UKR = (By.XPATH, '//button[text()= " Українська"]')
    LANGUAGE_RUS = (By.XPATH, '//button[text()= " Русский"]')
    ABOUT_US = (By.XPATH, '//a[@class="extra-link" and contains(text(), "нас")]')
    DELIVERY_PAYMENT = (By.XPATH, '//a[@class="extra-link" and contains(text(), "Доставка")]')
    RETURN_WARRANTY = (By.XPATH, '//a[@class="extra-link" and contains(text(), "гаран")]')
    CONTACTS = (By.XPATH, '//a[@class="extra-link" and contains(text(), "Контакт")]')
    SALES = (By.XPATH, '//a[@class="extra-link" and contains(text(), "Акц")]')
    CATALOG = (By.XPATH, '//h2[@class="home-title hidden-xs hidden-sm"]')
