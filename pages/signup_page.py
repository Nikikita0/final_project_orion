from ..pages import base_page, locators
import inspect


class SignupPage(base_page.BasePage):

    def click_button_signup(self):
        assert self.click_element(*locators.BasePageLocators.LOGIN_SIGNUP_MENU), \
            "The element is not present or intractable"
        assert self.click_element(*locators.BasePageLocators.SIGNUP), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_text(self):
        assert self.is_element_present(*locators.SignupPageLocators.H1_SIGNUP), \
            'Element is not present'
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_signup_data(self, email, password, name, phone, postcode, address):
        assert self.input_data(*locators.SignupPageLocators.EMAIL_SIGNUP_FIELD, email), \
            "The element is not present or intractable"
        assert self.input_data(*locators.SignupPageLocators.PASSWORD_SIGNUP_FIELD, password), \
            "The element is not present or intractable"
        assert self.input_data(*locators.SignupPageLocators.CONFIRM_PASSWORD_FIELD, password), \
            "The element is not present or intractable"
        assert self.input_data(*locators.SignupPageLocators.FIRST_NAME_SIGNUP_FIELD, name), \
            "The element is not present or intractable"
        assert self.input_data(*locators.SignupPageLocators.PHONE_SIGNUP_FIELD, phone), \
            "The element is not present or intractable"
        assert self.click_element(*locators.SignupPageLocators.SELECT_REGION_MENU), \
            "The element is not present or intractable"
        assert self.click_element(*locators.SignupPageLocators.REGION_OPTION), \
            "The element is not present or intractable"
        assert self.click_element(*locators.SignupPageLocators.SELECT_CITY_MENU), \
            "The element is not present or intractable"
        assert self.click_element(*locators.SignupPageLocators.CITY_OPTION), \
            "The element is not present or intractable"
        assert self.click_element(*locators.SignupPageLocators.SELECT_DEPARTMENT_MENU), \
            "The element is not present or intractable"
        assert self.click_element(*locators.SignupPageLocators.DEPARTMENT_OPTION), \
            "The element is not present or intractable"
        assert self.input_data(*locators.SignupPageLocators.POSTCODE_FIELD, postcode), \
            "The element is not present or intractable"
        assert self.input_data(*locators.SignupPageLocators.ADDRESS_FIELD, address), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def newsletter_decline(self):
        assert self.click_element(*locators.SignupPageLocators.RADIO_BTN_NEWSLETTER_FALSE), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def confirm_signup(self):
        assert self.click_element(*locators.SignupPageLocators.CONFIRM_BTN), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def logout_cabinet(self):
        assert self.click_element(*locators.SignupPageLocators.GO_TO_MAIN_PAGE), \
            "The element is not present or intractable"
        assert self.click_element(*locators.BasePageLocators.CABINET_MENU), \
            "The element is not present or intractable"
        assert self.click_element(*locators.BasePageLocators.LOGOUT_BTN), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_p(self):
        assert self.is_element_present(*locators.SignupPageLocators.P_EXIT), \
            'Element is not present'
        print(f"{inspect.currentframe().f_code.co_name} - Ok")




