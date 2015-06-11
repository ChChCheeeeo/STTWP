# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest

class ExecuteJavaScriptTest(unittest.TestCase):
    """ExecuteJavaScriptTest
        Highlight elements before performing actions on them using
        javascript methods. 
    """

    def setUp(self):
        self.driver = webdriver.Firefox()# Chrome non-op
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("http://demo.magentocommerce.com/")

    # def tearDown(self):
    #     self.driver.quit()

    def test_search_by_category(self):
        
        search_field  = self.driver.find_element_by_name("q")
        self.highlightElement(search_field)
        search_field.clear()

        # enter search keyword and submit
        self.highlightElement(search_field)

        search_field.send_keys("phones")
        search_field.submit()

        # get all anchor elementes currently displayed on page using
        # xpath for all anchor elements with product name
        products = self.driver.find_elements_by_xpath(
            "//h2[@class='product-name']/a"
        )

        # check correct number of products
        self.assertEqual(2, len(products))

    def highlightElement(self, element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "color: blue; border: 5px solid red;"
        )
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            ""
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
