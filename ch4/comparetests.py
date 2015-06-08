# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest

# check whether 'Clear All' option in the 'Compare Products' feature
# displays alert window recomfirming user's decision

class CompareProducts(unittest.TestCase):
    """CompareProducts
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com/")

    def tearDown(self):
        self.driver.quit()

    def test_compare_products_removal_alert(self):
        # search textbox
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()

        # enter search and submit
        search_field.send_keys("phones")
        search_field.submit()

        # click 'Add to Compare' link
        self.driver.find_element_by_link_text(
            "Add to Compare"
        ).click()

        # click on 'Remove this item' link
        # will display alert
        self.driver.find_element_by_link_text("Clear All").click()

        # switch to alert
        # switch_to_alert() depriciated
        alert = self.driver.switch_to.alert

        # get alert object text
        alert_text = alert.text

        # check what it says
        self.assertEqual(
            "Are you sure you would like to remove all products from your comparison?",
            alert_text
        )

        # click Ok
        alert.accept()



if __name__=='__main__':
    unittest.main(verbosity=2)