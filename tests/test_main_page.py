import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets
import random as rnd


@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % rnd.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.URL)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_site = browser.current_url
        page = MainPage(browser, self.link_to_site)
        page.is_button_cart()
        page.is_button_feedback()
        page.is_search_input()
        page.is_button_search()
        page.is_button_signup()
        page.is_button_login()
        page.is_button_wishlist()
        page.is_button_ukr_lang()
        page.is_button_rus_lang()
        page.is_button_about_us()
        page.is_button_delivery_payment()
        page.is_button_refund_warranty()
        page.is_button_contacts()
        page.is_catalog_menu()
        page.is_category_in_catalog()
        page.is_subcat_in_catalog()

    def test_main_page_content(self, browser):
        self.link_to_site = browser.current_url
        page = MainPage(browser, self.link_to_site)
        page.is_info_delivery_in_ukraine()
        page.is_info_delivery_for_free()
        page.is_info_comfortable_pay()
        page.is_info_warranty()
        page.is_show_next_category()
        page.is_show_prev_category()
        page.is_category_in_categories_list()
        page.is_switch_to_popular_products()
        page.is_switch_to_recommended_products()
        page.is_switch_to_new_products()
        page.is_show_next_product()
        page.is_show_prev_product()
        page.is_product_2()
        page.is_sale_label()
        page.is_day_offer_label()

    def test_main_page_footer(self, browser):
        self.link_to_site = browser.current_url
        page = MainPage(browser, self.link_to_site)
        page.is_button_subscribe()
        page.is_input_subscribe()
        page.is_button_sitemap()
        page.is_button_account()

    def subscribe_action(self, browser):
        self.link_to_site = browser.current_url
        page = MainPage(browser, self.link_to_site)
        page.subscribe_action(self.email_for_subscribe)



