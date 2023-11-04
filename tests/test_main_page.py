import pytest
from ..pages.base_page import BasePage
from ..settings import sets


@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.URL)
        page.open()
