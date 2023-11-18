import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.signup_page import SignupPage
from ..settings import sets
import random as rnd


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def setup_method(self):
        hash_name = "%032x" % rnd.getrandbits(128)
        self.email_for_signup = f"{hash_name}@mail.com"
        self.password_for_signup = "123654789"
        self.name_for_signup = 'Андрійов Андрій Андрійович'
        phone = ''
        for i in range(10): phone += str(rnd.randint(1, 9))
        self.phone_for_signup = phone
        self.postcode_for_signup = '09103'
        self.address_for_signup = 'Шевченка, 15'

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.URL)
        page.open()

    def test_login_cabinet(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupPage(browser, self.link_to_cabinet)
        page.click_button_signup()
        page.explicit_wait(5)
        page.input_signup_data(self.email_for_signup, self.password_for_signup, self.name_for_signup,
                               self.phone_for_signup, self.postcode_for_signup, self.address_for_signup)
        page.explicit_wait(5)
        page.newsletter_decline()
        page.explicit_wait(2)
        page.confirm_signup()
        page.explicit_wait(3)
        page = OrderPage(browser, self.link_to_cabinet)
        page.explicit_wait(3)
        page.go_to_main_after_login()

    def test_add_product_to_cart(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.explicit_wait(3)
        page.choose_product_main_page()
        page.explicit_wait(3)
        page.go_to_popular_product_page()
        page.explicit_wait(3)
        page.add_popular_product_to_cart()
        page.explicit_wait(3)
        page.check_qty(qty=3)
        page.go_to_order()

    def test_make_order(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.make_order()
        page.explicit_wait(3)





