# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

import unittest

# use explicit wait with expected condition for element visibility

class CompareProducts(unittest.TestCase):
    """CompareProducts
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com/")

    def tearDown(self):
        self.driver.quit()

    def test_compare_products_removal_alert(self):
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()

        search_field.send_keys("phones")
        search_field.submit()

        # click 'Add' to compare link
        self.driver.find_element_by_link_text("Add to Compare").click()

        # wait for 'Clear All' link to be visible
        clear_all_link = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.LINK_TEXT, "Clear All")
            )
        )

        # click on 'Clear All' link
        # it displays user alert
        clear_all_link.click()

        # wait for alert to be present
        alert = WebDriverWait(self.driver, 10).until(
            expected_conditions.alert_is_present()
        )

        alert_text = alert.text
        self.assertEqual(
            "Are you sure you would like to remove all products from your comparison?",
            alert_text
        )
        alert.accept()

        
if __name__=='__main__':
    unittest.main(verbosity=2)