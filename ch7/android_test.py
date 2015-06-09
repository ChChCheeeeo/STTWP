# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


# didn't actually run, couldn't get Appium to work properly

class SearchProductsOnAndroid(unittest.TestCase):
    """SearchProductsOnIphone
    """

    # need RemoteWebDriver to run tests with Appium. To use desired
    # platform, pass set of desired capailities
    def setUp(self):
        desired_caps = {}
        # platform
        desired_caps['device'] = 'Android'
        # platform vesion
        desired_caps['version'] = '4.3'
        # mobile browser
        desired_caps['app'] = 'Chrome'

        # connect to Appium server
        # pass desired capabilities to RemoteWebDriver
        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub',
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
        # click on serch idcon
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
            "//div[@class='catagory-products'/ul/li"
        )

        # check products count
        self.assertEqual(2, len(products))

if __name__ == '__main__':
    unittest.main(verbosity=2)
