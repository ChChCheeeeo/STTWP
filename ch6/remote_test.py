# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

# connect Selenium server and request it to set up a
# firefox browser running on Windows
# test shows interactin between test and server
# can also go to http://<remote-machine-ip>:4444/wd/hub/static/
# resource/hub.html, which displays a new session being created. If you hover over
# the capabilities link, it displays the capabilities being used to run the tests

class SearchProducts(unittest.TestCase):
    """SearchProducts
    """

    def setUp(self):
        desired_caps = {}
        desired_caps['platform'] = 'WINDOWS'
        desired_caps['browserName'] = 'firefox'

        self.driver = webdriver.Remote(
            'http://192.168.1.102:4444/wd/hub/',
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

if __name__=='__main__':
    unittest.main()

