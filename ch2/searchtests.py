# -*- coding: utf-8 -*-

from selenium import webdriver

import unittest

class SearchTest(unittest.TestCase):
    """SearchTest
        Test searchproducts
    """

    def setUp(self):
        #  to perform tasks at the start of each test or all the
        # tests that will be defined in the class.
        # create new FireFox session
        # runs before each test method to have consistent state
        # between tests
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        # navigate to demo home page
        self.driver.get("http://demo.magentocommerce.com/")

    def tearDown(self):
        # clean up any initialized values after the test is executed.
        self.driver.quit()

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