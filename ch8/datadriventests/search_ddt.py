# -*- coding: utf-8 -*-
from ddt import ddt, data, unpack
from selenium import webdriver
import unittest

# search test accepts pair of arguments for different
# search tearms and expected results count
# pass list of tuples using @data decorator
# @unpack to unpack tuples into multiple arguments

@ddt
class SearchDDT(unittest.TestCase):
    """SearchDDT
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigatetosite
        self.driver.get("http://demo.magentocommerce.com/")

    def tearDown(self):
        self.driver.quit()

    # specify test data using @data decorator
    @data(("phones", 2), ("music", 5))
    @unpack
    def test_search(self, search_value, expected_count):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter and submitsearch keyword
        # use search_value arg to pass data
        self.search_field.send_keys(search_value)
        self.search_field.submit()

        # get all anchors elements with have product names
        # currently displaed on result page using xpath
        products = self.driver.find_elements_by_xpath(
            "//h2[@class='product-name']/a"
        )

        # check products count
        self.assertEqual(expected_count, len(products))

if __name__ == '__main__':
    unittest.main(verbosity=2)
