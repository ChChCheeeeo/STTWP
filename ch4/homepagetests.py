# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import Select
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

    # def test_shopping_cart_empty_message(self):
    #     # check content
    #     shopping_cart_icon = self.driver.find_element_by_css_selector(
    #         "div.header-minicart span.icon"
    #     )
    #     shopping_cart_icon.click()
    #     shopping_car_status = self.driver.find_element_by_css_selector(
    #         "p.empty"
    #     ).text
    #     self.assertEqual(
    #         "You have no items in your shopping cart.",
    #         shopping_car_status
    #     )
    #     close_button = self.driver.find_element_by_css_selector(
    #         "div.minicart-wrapper a.close"
    #     )
    #     close_button.click()

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

    def test_my_account_link_is_displayed(self):
        # get account link
        account_link = self.driver.find_element_by_link_text("ACCOUNT")

        # check Home page footer displays My Account link
        self.assertTrue(account_link.is_displayed())

    def test_account_links(self):
        # get all links containing 'Account' as text
        account_links = self.driver.find_elements_by_partial_link_text("ACCOUNT")

        # check Home page footer displays Account and My Account link
        self.assertEqual(2, len(account_links))

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
        self.driver.back()

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

    def test_lanuage_options(self):
        # list expected values in 'Langauge Dropbown'
        exp_options = ["ENGLISH", "FRENCH", "GERMAN"]

        # empty list for capturing actual options displayed
        act_options = []

        # get Your langauge dropbown as instance of select class
        select_language = Select(self.driver.find_element_by_id(
            "select-language"
        ))

        # check number of dropbodwn options
        self.assertEqual(3, len(select_language.options))

        # get options in list
        for option in select_language.options:
            act_options.append(option.text)

        # check expected options list with actual options list
        self.assertListEqual(exp_options, act_options)

        # check default selected otiosn is English
        self.assertEqual(
            "ENGLISH",
            select_language.first_selected_option.text
        )

        # select option
        select_language.select_by_visible_text("German")

        # check if now German
        self.assertTrue("store=german" in self.driver.current_url)

        # changing langauge refreshes page
        # need to find dropdown again
        select_language = Select(self.driver.find_element_by_id(
            "select-langauge"
        ))
        select_language.select_by_index(0)

        # # select an item and check whether the store URL is changed
        # # based on the language selection
        # select_language.select_by_visible_text("German")

        # # check store now German
        # self.assertTrue("store=german" in self.driver.current_url)


if __name__=='__main__':
    unittest.main(verbosity=2)