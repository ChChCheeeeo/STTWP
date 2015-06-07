# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest

# Fill out five textboxes and select a checkbox for the newsletter
class RegisterNewUser(unittest.TestCase):
    """RegisterNewUser
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # home page
        self.driver.get("http://demo.magentocommerce.com/")

    def test_register_new_user(self):
        # open and click on 'Log In'
        driver = self.driver
        account_link = self.driver.find_element_by_link_text("ACCOUNT")
        # some reason "Log In" shows up in firebug but need to
        # click on account first
        account_link.click()

        driver.find_element_by_link_text("Log In").click()


if __name__=='__main__':
    unittest.main(verbosity=2)