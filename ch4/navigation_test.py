# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

import unittest

# use navigation API to navigate browser history and validate
# application state
class NavigationTest(unittest.TestCase):
    """NavigationTest
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("http://www.google.com/")

    def tearDown(self):
        self.driver.quit()

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name("q")
        search_field.clear()

        search_field.send_keys("selenium webdriver")
        search_field.submit()

        se_wd_link = driver.find_element_by_link_text(
            "Selenium WebDriver"
        )
        se_wd_link.click()
        self.assertEqual("Selenium WebDriver", driver.title)

        # search resuilts
        driver.back()

        this_title = "selenium webdriver - Google Search"
        self.assertTrue(
            WebDriverWait(self.driver, 10).until(
                expected_conditions.title_is(this_title))
        )

        # back to apage
        driver.forward()
        self.assertTrue(
            WebDriverWait(self.driver, 10).until(
                expected_conditions.title_is("Selenium WebDriver"))
        )

        driver.refresh()
        self.assertTrue(
            WebDriverWait(self.driver, 10).until(
                expected_conditions.title_is("Selenium WebDriver"))
        )
        
if __name__=='__main__':
    unittest.main(verbosity=2)