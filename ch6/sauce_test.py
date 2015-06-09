# -*- coding: utf-8 -*-
from keys import get_info
from selenium import webdriver
import unittest
import sys


# sauce test for running on the cloud

class SearchProducts(unittest.TestCase):
    """SearchProducts
    """

    PLATFORM = 'WINDOWS'
    BROWSER = 'firefox'
    SAUCE_USERNAME, SAUCE_KEY = get_info()

    def setUp(self):
        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browserName'] = self.BROWSER

        sauce_string = self.SAUCE_USERNAME + ":" + self.SAUCE_KEY

        self.driver = webdriver.Remote(
            'http://' + sauce_string + '@ondemand.saucelabs.com:80/wd/hub',
            desired_caps
        )
        self.desired_caps.get(
            'http://demo.magentocommerce.com/'
        )
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def teatSearchByCategory(self):
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all anchor elements which have product names
        # displayed on current page using xpath method
        products = self.driver.find_element_by_xpath(
            "//h2[@class=\'product-name']/a"
        )

        # check products count
        self.assertEqual(2, len(products))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SearchProducts.BROWSER = sys.argv.pop()
        SearchProducts.PLATFORM = sys.argv.pop()
    unittest.main(verbosity=2)
