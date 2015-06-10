# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

# provide resuable code so won't need to write for each
# test class

class BaseTestCase(unittest.TestCase):
    """BaseTestCase
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigatetosite
        self.driver.get("http://demo.magentocommerce.com/")

    def tearDown(self):
        self.driver.quit()
