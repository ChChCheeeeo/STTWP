# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

import unittest

# use explicit wait with expected condition for element visibility

class ExplicitWaitTests(unittest.TestCase):
    """ExplicitWaitTests
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com/")

    def tearDown(self):
        self.driver.quit()

    def test_account_link(self):
        # use explicit wait until "Log In" link is visible
        # in DOM, using expected visibility_of_element_located
        # condition. Explicitly waits 10 seconds looking for
        # element to be visible. Once element visible with special
        # locator, expected condition returns the located element
        # back to the script. TimeoutExecption raised if element
        # not visible with specified locator in the given timeout,
        WebDriverWait(self.driver, 10).until(
            lambda s: s.find_element_by_id(
                "select-language"
            ).get_attribute("length") == "3"
        )

        account = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.LINK_TEXT, "ACCOUNT")
            )
        )
        account.click()

    def test_create_new_customer(self):
        # wait for 'Create an Account' to be clickable. click it
        # and wait for next page

        self.driver.find_element_by_link_text("ACCOUNT").click()

        # wait for 'My Account' link in menu
        my_account = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.LINK_TEXT, "My Account")
            )
        )
        my_account.click()

        # get 'Create Account' button
        # wait for element to be enabled
        create_account_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.LINK_TEXT, "CREATE AN ACCOUNT")
            )
        )

        # display new account
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_contains(
                "Create New Customer Account"
            )
        )

if __name__=='__main__':
    # display amount of test results in console
    unittest.main(verbosity=2)