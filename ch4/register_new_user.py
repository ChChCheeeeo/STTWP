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

    def tearDown(self):
        self.driver.quit()

    def test_register_new_user(self):
        # open and click on 'Log In'
        driver = self.driver
        account_link = self.driver.find_element_by_link_text("ACCOUNT")
        # some reason "Log In" shows up in firebug but need to
        # click on account first
        account_link.click()

        driver.find_element_by_link_text("Log In").click()

        # get 'Create Account' button
        create_account_button = driver.find_element_by_link_text(
            "CREATE AN ACCOUNT"
        )

        # check 'Create Account' button is displayed and enabled
        self.assertTrue(
            create_account_button.is_displayed() and
            create_account_button.is_enabled()
        )
        # check whether page title matches what's expected
        create_account_button.click()

        # correct page title?
        self.assertEqual(
            "Create New Customer Account",
            driver.title
        )

        # get all fields from 'Create an Account' form
        first_name = driver.find_element_by_id("firstname")
        last_name = driver.find_element_by_id("lastname")
        email_addr = driver.find_element_by_id("email_address")

        news_letter_subscription = driver.find_element_by_id(
            "is_subscribed"
        )
        
        pw = driver.find_element_by_id("password")
        confirm_pw = driver.find_element_by_id("confirmation")

        submit_button = driver.find_element_by_xpath(
            "//button[@title='Register']"
        )


if __name__=='__main__':
    unittest.main(verbosity=2)