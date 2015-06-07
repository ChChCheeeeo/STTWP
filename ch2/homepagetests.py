# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

import unittest

class HomePageTest(unittest.TestCase):
    """HomePageTest
    """
    @classmethod
    def setUp(cls):
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
        self.assertTrue(self.is_element_present(By.NAME,"q"))

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

if __name__=='__main__':
    unittest.main(verbosity=2)