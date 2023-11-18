import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.login_page import LoginPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:
    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.URL)
        page.open()

    def test_login_cabinet(self, browser):
        self.link_to_cabinet = browser.current_url
        page = LoginPage(browser, self.link_to_cabinet)
        page.click_button_login()
        page.explicit_wait(2)
        page.login_cabinet(sets.TEST_EMAIL, sets.PASSWORD)
        page.explicit_wait(3)
        page.confirm_login()
        page.is_h1_cabinet()
        page = OrderPage(browser, self.link_to_cabinet)
        page.explicit_wait(3)
        page.go_to_main_after_login()

    def add_products_to_cart(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.explicit_wait(3)
        page.choose_product_main_page()
        page.explicit_wait(3)
        page.go_to_popular_product_page()
        page.explicit_wait(3)
        page.add_popular_product_to_cart()
        page.explicit_wait(3)
        page.make_order()
        page.explicit_wait(3)





