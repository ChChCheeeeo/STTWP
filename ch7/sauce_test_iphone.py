# -*- coding: utf-8 -*-
from keys import get_info
from selenium import webdriver
import unittest
import sys


# sauce test for running on the cloud
# didn't actually run, couldn't get Appium to work properly
# Sauce provides support for testing mobile apps using Appium
class SearchProductsOnIphone(unittest.TestCase):
    """SearchProducts
    """

    SAUCE_USERNAME, SAUCE_KEY = get_info()

    def setUp(self):
        desired_caps = {}
        desired_caps['browserName'] = 'Safari'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['platformName'] = 'iOS'
        desired_caps['deviceName'] = 'iPhone Simulator'

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

    def test_search_by_category(self):
        # click search icon
        self.driver.find_element_by_xpath(
            "//a[@href='#header-search']"
        ).click()
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all anchor elements which have product names
        # displayed on current page using xpath method
        products = self.driver.find_element_by_xpath(
            "//div[@class=\'category-products']/ul/li"
        )

        # check products count
        self.assertEqual(2, len(products))

if __name__ == '__main__':
    unittest.main(verbosity=2)
