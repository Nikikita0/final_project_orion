from selenium.webdriver.common.by import By


class BasePageLocators:
    CART = (By.XPATH, '//span[@class="cart-link"]')
    GO_TO_CHECKOUT = (By.XPATH, '//button[@class="btn btn-primary btn-cartblock"]')

    FEEDBACK = (By.XPATH, '//div[@class="contact-num"]/a')
    SEARCH_FIELD = (By.XPATH, '//input[@id="ajax-search-text"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@id="ajax-search-btn"]')
    LOGIN_SIGNUP_MENU = (By.XPATH, '//span[@class="expand-more"]')
    SIGNUP = (By.XPATH, '//a[@href="https://oriontoys.shop/index.php?route=account/simpleregister"]')
    LOGIN = (By.XPATH, '//a[@href="https://oriontoys.shop/index.php?route=account/login"]')

    CABINET_MENU = (By.XPATH, '//div[@class="user-info"]')
    LOGOUT_BTN = (By.XPATH, '//a[@href="https://oriontoys.shop/index.php?route=account/logout"]')

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

    ALERT_SUCCESS = (By.XPATH, '//div[@class="col-xs-12 alert alert-success"]')

    QTY = (By.XPATH, '//span[@class="cart-products-count hidden-sm hidden-xs"]')



class MainPageLocators:

    DELIVERY_UKR_MAIN = (By.XPATH, '//div[@class="ishiservicesblock"]//div[@class="row"]/div[1]/a')
    FREE_DELIVERY_MAIN = (By.XPATH, '//div[@class="ishiservicesblock"]//div[@class="row"]/div[2]/a')
    PAYMENT_MAIN = (By.XPATH, '//div[@class="ishiservicesblock"]//div[@class="row"]/div[3]/a')
    WARRANTY_MAIN = (By.XPATH, '//div[@class="ishiservicesblock"]//div[@class="row"]/div[4]/a')

    NEXT_CATS_MAIN = (By.XPATH, '//div[@class="section-header"]//div[@class="owl-next"]')
    PREV_CATS_MAIN = (By.XPATH, '//div[@class="section-header"]//div[@class="owl-prev"]')
    CAT_CARS_MAIN = (By.XPATH, '//a[@href="https://oriontoys.shop/mashynky-i-tekhnika/"]')

    POPULAR_GOODS = (By.XPATH, '//a[contains(@href,"#bestseller-products-block")]')
    POPULAR_PRODUCT = (By.XPATH, '//img[@src="https://oriontoys.shop/image/cache/catalog/productsimage/440_04-370x370.jpg"]')
    RECOMMENDED_GOODS = (By.XPATH, '//a[contains(@href,"#featured-products-block")]')
    NEW_GOODS = (By.XPATH, '//a[contains(@href,"#new-products-block")]')
    PREV_GOODS = (By.XPATH, '//div[@class="tab-content"]//div[@class="owl-carousel owl-loaded owl-drag"]/div[@class="owl-nav"]/div[@class="owl-prev"]')
    NEXT_GOODS = (By.XPATH, '//div[@class="tab-content"]//div[@class="owl-carousel owl-loaded owl-drag"]/div[@class="owl-nav"]/div[@class="owl-next"]')
    PRODUCT_MAIN = (By.XPATH, '//a[contains(text(),"Арт.374")]//ancestor::div[@class="item product-thumb"]')
    ADD_PRODUCT_TO_CART = (By.XPATH, '//a[contains(text(),"Арт.374")]//ancestor::div[@class="item product-thumb"]// button[ @class ="remarketing_cart_button"]')
    SALE_LABEL = (By.XPATH, "//span[text()='Акція']")
    DAY_OFFER_LABEL = (By.XPATH, "//span[text()='Пропозиція дня']")


class SignupPageLocators:
    H1_SIGNUP = (By.XPATH, '//h1[text()="Швидка реєстрація"]')

    EMAIL_SIGNUP_FIELD = (By.XPATH, '//input[@id="register_email"]')
    PASSWORD_SIGNUP_FIELD = (By.XPATH, '//input[@id="register_password"]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//input[@id="register_confirm_password"]')
    FIRST_NAME_SIGNUP_FIELD = (By.XPATH, '//input[@id="register_firstname"]')
    PHONE_SIGNUP_FIELD = (By.XPATH, '//input[@id="register_telephone"]')
    SELECT_REGION_MENU = (By.XPATH, '//select[@id="register_country_id"]')
    REGION_OPTION = (By.XPATH, '//option[@value="300009"]')
    SELECT_CITY_MENU = (By.XPATH, '//select[@id="register_zone_id"]')
    CITY_OPTION = (By.XPATH, '//option[@value="200038"]')
    SELECT_DEPARTMENT_MENU = (By.XPATH, '//select[@id="register_city"]')
    DEPARTMENT_OPTION = (By.XPATH, '//option[@value="Відділення №3 (до 30 кг): вул. Леваневського, 47/1"]')
    POSTCODE_FIELD = (By.XPATH, '//input[@id="register_postcode"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@id="register_address_1"]')
    RADIO_BTN_NEWSLETTER_TRUE = (By.XPATH, '//input[@id="register_newsletter_1"]')
    RADIO_BTN_NEWSLETTER_FALSE = (By.XPATH, '//input[@id="register_newsletter_0"]')
    CONFIRM_BTN = (By.XPATH, '//div[@class="simpleregister-button-right"]')
    GO_TO_MAIN_PAGE = (By.XPATH, '//div[@id="logo"]/a[@href="https://oriontoys.shop/"]')
    P_EXIT = (By.XPATH, '//p[text()="Ви вийшли з Особистого Кабінету."]')


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@id="input-email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="input-password"]')
    FORGOT_PASSWORD = (By.XPATH, '//a[text()="Забули пароль?"]')
    SUBMIT_BTN = (By.XPATH, '//input[@class="btn btn-primary"]')
    GO_TO_SIGNUP_BTN = (By.XPATH, '//a[@class="btn btn-primary"]')

    H1_CABINET = (By.XPATH, '//h1[text()="Особистий Кабінет"]')


class CheckoutPageLocators:
    ALREDY_REGISTRED = (By.XPATH, '//a[@data-onclick="openLoginBox"]')
    EMAIL_IN_LOGIN_BOX = (By.XPATH, '//input[@data-onkeydown="detectEnterAndLogin"and @name="email"]')
    PASSWORD_IN_LOGIN_BOX = (By.XPATH, '//input[@data-onkeydown="detectEnterAndLogin"and @name="password"]')
    CONFIRM_IN_LOGIN_BOX = (By.XPATH, '//a[@id="simplecheckout_button_login"]')
    FORGOT_PASSWORD_IN_LOGIN_BOX = (By.XPATH, '//a[text()="Забули пароль?"]')

    DO_WITH_REGISTRATION = (By.XPATH, '//input[@id="customer_register_1"]')
    DO_WITHOUT_REGISTRATION = (By.XPATH, '//input[@id="customer_register_0"]')

    EMAIL_CHECKOUT_FIELD = (By.XPATH, '//input[@id="customer_email"]')
    PASSWORD_CHECKOUT_FIELD = (By.XPATH, '//input[@id="customer_password"]')
    CONFIRM_CHECKOUT_FIELD = (By.XPATH, '//input[@id="customer_confirm_password"]')
    FIRST_NAME_CHECKOUT_FIELD = (By.XPATH, '//input[@id="shipping_address_firstname"]')
    PHONE = (By.XPATH, '//input[@id="customer_telephone"]')
    SELECT_REGION_MENU = (By.XPATH, '//select[@id="shipping_address_country_id"]')
    REGION_OPTION = (By.XPATH, '//option[@value="300009"]')
    SELECT_CITY_MENU = (By.XPATH, '//select[@id="shipping_address_zone_id"]')
    CITY_OPTION = (By.XPATH, '//option[@value="200038"]')
    SELECT_DEPARTMENT_MENU = (By.XPATH, '//select[@id="shipping_address_city"]')
    DEPARTMENT_OPTION = (By.XPATH, '//option[@value="Відділення №3 (до 30 кг): вул. Леваневського, 47/1"]')

    DELIVERY_TO_DEPARTMENT = (By.XPATH, '//input[@id="novaposhta.novaposhta"]')
    COURIER_DELIVERY = (By.XPATH, '//input[@id="novaposhtacopy.novaposhtacopy"]')

    CARD_PAY = (By.XPATH, '//input[@id="wayforpay"]')
    PAY_ON_RECEIPT = (By.XPATH, '//input[@id="cod"]')

    CALL_TO_CONFIRM_CHECKBOX = (By.XPATH, '//input[@id="payment_address_iscall"]')
    CONFIRM_BUTTON = (By.XPATH, "//input[@id='button-confirm' and @class='btn btn-primary button']")


class ForgotPasswordPageLocators:
    EMAIL_FP_FIELD = (By.XPATH, '//input[id="input-email"]')
    CONFIRM_FP_FIELD = (By.XPATH, '//input[@class="btn btn-primary"]')
    SUCCESS_ALERT = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')
    DANGER_ALERT = (By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]')


class ProductPageLocators:
    QUANTITY_FIELD = (By.XPATH, '//input[@id="input-quantity"]')
    ADD_TO_CART = (By.XPATH, '//button[@id="button-cart"]')
    COLOR_CHOOSE_MENU = (By.XPATH, '//select[@id="input-option438"]')
    COLOR_OPTION = (By.XPATH, '//option[@value="1052"]')












