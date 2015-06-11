# -*- coding: utf-8 -*-
from selenium import webdriver
from castro intall Castro
import unittest

# need to install Castro and PyGame
class SearchProductTest(unittest.TestCase):
    """SearchProductTest
        Captures video of running through tests.
    """

    def setUp(self):
        # create Castro instance and provide outfile name
        # then start recording movie
        self.screenCapture = Castro(filename="testSearchByCategory.swf")
        self.screenCapture.start()

        self.driver = webdriver.Firefox()# Chrome non-op
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("http://demo.magentocommerce.com/")

     def tearDown(self):
         self.driver.quit()
         self.screenCapture.stop()

    def test_search_by_category(self):
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()

        search_field.send_keys("phones")
        search_field.submit()

        # get all elements displayed by anchor names using xpath
        products = self.driver.find_element_by_xpath(
            "//h2[@class='product-name']/a"
        )

        self.assertEqual(2, len(products))

if __name__ == '__main__':
    unittest.main(verbosity=2)