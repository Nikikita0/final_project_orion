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
    CARS_TECHNIQUE_CAT = (By.XPATH, '//a[@href="https://oriontoys.shop/mashynky-ta-tekhnika"]')
    BIG_CARS_SUBCAT = (By.XPATH, '//a[@href="https://oriontoys.shop/mashynky-ta-tekhnika/velyki-mashynky"]')

    SUBSCRIBE = (By.XPATH, '//a[@class="button btn-submit"]')
    EMAIL_SUBSCRIBE = (By.XPATH, '//input[@id="subscribe_email"]')
    SITEMAP = (By.XPATH, '//a[@href="https://oriontoys.shop/index.php?route=information/sitemap"]')
    ACCOUNT = (By.XPATH, '//a[text()= "Аккаунт"]')


class MainPageLocators:

    DELIVERY_UKR_MAIN = (By.XPATH, '//div[@class="ishiservicesblock"]//div[@class="row"]/div[1]/a')
    FREE_DELIVERY_MAIN = (By.XPATH, '//div[@class="ishiservicesblock"]//div[@class="row"]/div[2]/a')
    PAYMENT_MAIN = (By.XPATH, '//div[@class="ishiservicesblock"]//div[@class="row"]/div[3]/a')
    WARRANTY_MAIN = (By.XPATH, '//div[@class="ishiservicesblock"]//div[@class="row"]/div[4]/a')

    NEXT_CATS_MAIN = (By.XPATH, '//div[@class="section-header"]//div[@class="owl-next"]')
    PREV_CATS_MAIN = (By.XPATH, '//div[@class="section-header"]//div[@class="owl-prev"]')
    CAT_CARS_MAIN = (By.XPATH, '//a[@href="https://oriontoys.shop/mashynky-i-tekhnika/"]')

    POPULAR_GOODS = (By.XPATH, '//a[contains(@href,"#bestseller-products-block")]')
    RECOMENDED_GOODS = (By.XPATH, '//a[contains(@href,"#featured-products-block")]')
    NEW_GOODS = (By.XPATH, '//a[contains(@href,"#new-products-block")]')
    PREV_GOODS = (By.XPATH, '//div[@class="tab-content"]//div[@class="owl-carousel owl-loaded owl-drag"]/div[@class="owl-nav"]/div[@class="owl-prev"]')
    NEXT_GOODS = (By.XPATH, '//div[@class="tab-content"]//div[@class="owl-carousel owl-loaded owl-drag"]/div[@class="owl-nav"]/div[@class="owl-next"]')
    PRODUCT_MAIN = (By.XPATH, '//a[contains(text(),"Арт.374")]//ancestor::div[@class="item product-thumb"]')

    SALE_LABEL = (By.XPATH, "//span[text()='Акція']")
    DAY_OFFER_LABEL = (By.XPATH, "//span[text()='Пропозиція дня']")
