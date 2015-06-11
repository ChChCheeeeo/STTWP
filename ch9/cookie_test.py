# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import unittest

class CookiesTest(unittest.TestCase):
    """CookiesTest
        Example validating a cookie created to store langauge selected
        by user on demos application home page.
    """

    URL = "http://demo.magentocommerce.com"

    def setUp(self):

        self.driver = webdriver.Firefox()# Chrome non-op
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.close()#quit()

    def test_store_cookie(self):
        driver = self.driver

        # get Your langauge droptown as instance of Select class
        select_language = Select(self.driver.find_element_by_id(
            "select-language"
        ))

        # check default selected option is English
        self.assertEqual(
            "ENGLISH",
            select_language.first_selected_option.text
        )

        # store cookie should be none
        store_cookie = driver.get_cookie("store")
        print("\nCookie is: ")
        print(store_cookie)
        self.assertEqual(None, store_cookie)

        # select option using select_y_visible text
        select_language.select_by_visible_text("French")

        # store cookie should be populated with selected country
        store_cookie = driver.get_cookie("store")['value']
        print("\nCookie is: ")
        print(store_cookie)
        self.assertEqual(
            "french",
            store_cookie
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)