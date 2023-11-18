from ..pages import base_page, locators
import inspect


class LoginPage(base_page.BasePage):

    def click_button_login(self):
        assert self.click_element(*locators.BasePageLocators.LOGIN_SIGNUP_MENU), \
            "The element is not present or intractable"
        assert self.click_element(*locators.BasePageLocators.LOGIN), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def login_cabinet(self, user_email, user_password):
        assert self.input_data(*locators.LoginPageLocators.EMAIL_FIELD, user_email), \
            "The element is not present or intractable"
        assert self.input_data(*locators.LoginPageLocators.PASSWORD_FIELD, user_password), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def confirm_login(self):
        assert self.click_element(*locators.LoginPageLocators.SUBMIT_BTN), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_cabinet(self):
        assert self.is_element_present(*locators.LoginPageLocators.H1_CABINET), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


