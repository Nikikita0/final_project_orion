from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_button_cart(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_feedback(self):
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_input(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_FIELD), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_search(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_signup(self):
        assert self.hover_action(*locators.BasePageLocators.LOGIN_SIGNUP_MENU), \
            "Element is not present"
        assert self.is_element_present(*locators.BasePageLocators.SIGNUP), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_login(self):
        assert self.hover_action(*locators.BasePageLocators.LOGIN_SIGNUP_MENU), \
            "Element is not present"
        assert self.is_element_present(*locators.BasePageLocators.LOGIN), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_wishlist(self):
        assert self.is_element_present(*locators.BasePageLocators.WISHLIST), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_ukr_lang(self):
        assert self.hover_action(*locators.BasePageLocators.LANGUAGE_MENU), \
            "Element is not present"
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_UKR), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_rus_lang(self):
        assert self.hover_action(*locators.BasePageLocators.LANGUAGE_MENU), \
            "Element is not present"
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_RUS), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_about_us(self):
        assert self.is_element_present(*locators.BasePageLocators.ABOUT_US), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_delivery_payment(self):
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY_PAYMENT), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_refund_warranty(self):
        assert self.is_element_present(*locators.BasePageLocators.RETURN_WARRANTY), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_contacts(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_catalog_menu(self):
        assert self.is_element_present(*locators.BasePageLocators.CATALOG), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_category_in_catalog(self):
        assert self.is_element_present(*locators.BasePageLocators.CARS_TECHNIQUE_CAT), \
            "Element is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_subcat_in_catalog(self):
        assert self.hover_action(*locators.BasePageLocators.CARS_TECHNIQUE_CAT), \
            "Element is not present"
        assert self.is_element_present(*locators.BasePageLocators.BIG_CARS_SUBCAT), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_delivery_in_ukraine(self):
        assert self.is_element_present(*locators.MainPageLocators.DELIVERY_UKR_MAIN), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_delivery_for_free(self):
        assert self.is_element_present(*locators.MainPageLocators.FREE_DELIVERY_MAIN), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_comfortable_pay(self):
        assert self.is_element_present(*locators.MainPageLocators.PAYMENT_MAIN), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_warranty(self):
        assert self.is_element_present(*locators.MainPageLocators.WARRANTY_MAIN), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_next_category(self):
        assert self.is_element_present(*locators.MainPageLocators.NEXT_CATS_MAIN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_prev_category(self):
        assert self.is_element_present(*locators.MainPageLocators.PREV_CATS_MAIN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_category_in_categories_list(self):
        assert self.is_element_present(*locators.MainPageLocators.PREV_CATS_MAIN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_switch_to_popular_products(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_GOODS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_switch_to_recommended_products(self):
        assert self.is_element_present(*locators.MainPageLocators.RECOMENDED_GOODS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_switch_to_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_GOODS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_next_product(self):
        assert self.is_element_present(*locators.MainPageLocators.NEXT_GOODS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_prev_product(self):
        assert self.is_element_present(*locators.MainPageLocators.PREV_GOODS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_product_2(self):
        assert self.is_element_present(*locators.MainPageLocators.PRODUCT_MAIN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_add_to_cart_product_2(self):
        assert self.hover_action(*locators.MainPageLocators.PRODUCT_MAIN), \
            "The element is not present"
        assert self.is_element_present(*locators.MainPageLocators.ADD_PRODUCT_TO_CART), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


    def is_sale_label(self):
        assert self.is_element_present(*locators.MainPageLocators.SALE_LABEL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_day_offer_label(self):
        assert self.is_element_present(*locators.MainPageLocators.DAY_OFFER_LABEL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_input_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.EMAIL_SUBSCRIBE), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_sitemap(self):
        assert self.is_element_present(*locators.BasePageLocators.SITEMAP), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_account(self):
        assert self.is_element_present(*locators.BasePageLocators.ACCOUNT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def subscribe_action(self, email):
        assert self.input_data(*locators.BasePageLocators.EMAIL_SUBSCRIBE, email), \
            "The element is not inserted"
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBE), \
            "The element is not clickable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")















