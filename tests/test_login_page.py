import pytest
from ..pages.base_page import BasePage
from ..pages.login_page import LoginPage
from ..pages.signup_page import SignupPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login_page
class TestLoginPage:
    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.URL)
        page.open()

    def test_login_to_cabinet(self, browser):
        self.link_to_cabinet = browser.current_url
        page = LoginPage(browser, self.link_to_cabinet)
        page.click_button_login()
        page.explicit_wait(2)
        page.login_cabinet(sets.TEST_EMAIL, sets.PASSWORD)
        page.explicit_wait(3)
        page.confirm_login()
        page.is_h1_cabinet()

    def test_logout_cabinet(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupPage(browser, self.link_to_cabinet)
        page.logout_cabinet()
        page.explicit_wait(2)
        page.is_p()
        page.explicit_wait(2)




