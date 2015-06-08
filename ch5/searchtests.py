# -*- coding: utf-8 -*-

from selenium import webdriver

import unittest

class SearchTests(unittest.TestCase):
    """SearchTest
        Test searchproducts
    """

    def setUp(self):
        # share values between the test methods using the setUpClass() 
        # and tearDownClass() methods and using the @classmethod 
        # decorator.
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("http://demo.magentocommerce.com/")

    def tearDown(self):
        self.driver.quit()

    def test_search_by_category(self):
        # search textbox
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

if __name__=='__main__':
    # display amount of test results in console
    unittest.main(verbosity=2)