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
        # runs before each test method.
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.criver.maximize_window()

        # navigate to demo home page
        self.driver.get("http://demo.magentocommerce.com/")
