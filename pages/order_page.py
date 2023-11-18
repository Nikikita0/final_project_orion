from ..pages import base_page, locators
import inspect


class OrderPage(base_page.BasePage):

    def go_to_main_after_login(self):
        assert self.click_element(*locators.SignupPageLocators.GO_TO_MAIN_PAGE), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def choose_product_main_page(self):
        assert self.hover_action(*locators.MainPageLocators.PRODUCT_MAIN), \
            "Element is not present"
        assert self.click_element(*locators.MainPageLocators.ADD_PRODUCT_TO_CART), \
            "Element is not present"
        assert self.is_element_present(*locators.BasePageLocators.ALERT_SUCCESS), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def go_to_popular_product_page(self):
        assert self.click_element(*locators.MainPageLocators.POPULAR_GOODS), \
            "Element is not present"
        assert self.click_element(*locators.MainPageLocators.POPULAR_PRODUCT), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_popular_product_to_cart(self):
        assert self.click_element(*locators.ProductPageLocators.COLOR_CHOOSE_MENU), \
            "Element is not present"
        assert self.click_element(*locators.ProductPageLocators.COLOR_OPTION), \
            "Element is not present"
        assert self.clear_field(*locators.ProductPageLocators.QUANTITY_FIELD), \
            "Element is not present"
        assert self.input_data(*locators.ProductPageLocators.QUANTITY_FIELD, 2), \
            "Element is not present"
        assert self.click_element(*locators.ProductPageLocators.ADD_TO_CART), \
            "Element is not present"
        assert self.is_element_present(*locators.BasePageLocators.ALERT_SUCCESS), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def go_to_order(self):
        assert self.click_element(*locators.BasePageLocators.CART), \
            "Element is not present"
        assert self.click_element(*locators.BasePageLocators.GO_TO_CHECKOUT), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def make_order(self):
        assert self.click_element(*locators.CheckoutPageLocators.CALL_TO_CONFIRM_CHECKBOX), \
            "Element is not present"
        assert self.click_element(*locators.CheckoutPageLocators.PAY_ON_RECEIPT), \
            "Element is not present"
        assert self.is_element_present(*locators.CheckoutPageLocators.CONFIRM_BUTTON), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def check_qty(self,qty):
        qty_actual = self.get_text(*locators.BasePageLocators.QTY).split(" ")
        assert int(qty_actual[1]) == qty, \
            "QTY doesn't match to actual"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")





