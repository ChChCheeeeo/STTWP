# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

import unittest

class HomePageTests(unittest.TestCase):
    """HomePageTest
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # home page
        cls.driver.get("http://demo.magentocommerce.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        """Utility method checks precence of element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def test_search_field(self):
        # check Home page search field exits
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_langauge_option(self):
        # check home page language drop down options
        self.assertTrue(self.is_element_present(
            By.ID, "select-language"
        ))

    def test_shopping_cart_empty_message(self):
        # check content
        shopping_cart_icon = self.driver.find_element_by_css_selector(
            "div.header-minicart span.icon"
        )
        shopping_cart_icon.click()
        shopping_car_status = self.driver.find_element_by_css_selector(
            "p.empty"
        ).text
        self.assertEqual(
            "You have no items in your shopping cart.",
            shopping_car_status
        )
        close_button = self.driver.find_element_by_css_selector(
            "div.minicart-wrapper a.close"
        )
        close_button.click()

    def test_search_text_field_max_length(self):
        # get search textbox
        search_field = self.driver.find_element_by_id("search")

        # check maxlength attribute set to 128
        self.assertEqual("128", search_field.get_attribute("maxlength"))

    def test_search_button_enabled(self):
        # get search button
        search_button = self.driver.find_element_by_class_name("button")

        # check search button enabled
        self.assertTrue(search_button.is_enabled())

    def test_count_of_promo_banners_images(self):
        # get promo banner list
        banner_list = self.driver.find_element_by_class_name("promos")

        # get images from banner list
        banners = banner_list.find_elements_by_tag_name("img")

        # check there are 3 tags displayed
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        # test vip promo image
        xpath = "//img[@alt='Shop Private Sales - Members Only']"
        vip_promo = self.driver.find_element_by_xpath(xpath)

        # check home pages displays vip promo logo
        self.assertTrue(vip_promo.is_displayed())

        # click on vip promo to open page
        vip_promo.click()

        # check page title
        self.assertEqual("VIP", self.driver.title)

    def test_shopping_cart_status(self):
        # check My Shopping Cart home page content
        # click and open Shpping Cart icon
        # in Shopping Cart section
        # here using class name and element tag name
        # see cart in firebug
        shopping_cart_icon = self.driver.find_element_by_css_selector(
            "div.header-minicart span.icon"
        )
        shopping_cart_icon.click()

        # get shopping cart status
        shopping_car_status = self.driver.find_element_by_css_selector(
            "p.empty"
        ).text
        self.assertEqual("You have no items in your shopping cart.",
            shopping_car_status
        )

        # close shopping cart section
        close_button = self.driver.find_element_by_css_selector(
            "div.minicart-wrapper a.close"
        )
        close_button.click()

    def test_my_account_link_is_displayed(self):
        # get account link
        account_link = self.driver.find_element_by_link_text("ACCOUNT")

        # check Home page footer displays My Account link
        self.assertTrue(account_link.is_displayed())

    def test_account_links(self):
        # get all links containing 'Account' as text
        account_links = self.driver.find_elements_by_partial_link_text("ACCOUNT")

        # check Home page footer displays Account and My Account link
        self.assertTrue(2, len(account_links))

if __name__=='__main__':
    unittest.main(verbosity=2)