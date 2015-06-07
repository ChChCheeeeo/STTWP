# -*- coding: utf-8 -*-

from selenium import webdriver

import unittest

class SearchTests(unittest.TestCase):
    """SearchTest
        Test searchproducts
    """

    @classmethod
    def setUpClass(cls):
        # share values between the test methods using the setUpClass() 
        # and tearDownClass() methods and using the @classmethod 
        # decorator.
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to demo home page
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.driver.title

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search_by_category(self):
        # get search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter and submit search keyword
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # get all the anchor and display elements containing
        # product names on the result page
        products = self.driver.find_elements_by_xpath(
            "//h2[@class='product-name']/a"
        )
        self.assertEqual(2, len(products))

    def test_search_by_name(self):
        # get search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter and submit search keyword
        self.search_field.send_keys("sal shaker")
        self.search_field.submit()

        # get all the anchor and display elements containing
        # product names on the result page
        products = self.driver.find_elements_by_xpath(
            "//h2[@class='product-name']/a"
        )
        self.assertEqual(1, len(products))


if __name__=='__main__':
    # display amount of test results in console
    unittest.main(verbosity=2)