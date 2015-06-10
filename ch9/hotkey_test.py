# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class HotKeyTest(unittest.TestCase):
    """HotKeyTest
        Demonstrate how keyboard actions such as pressing a hot key
        combination.
    """

    URL = "http://rawgit.com/jeresig/jquery.hotkeys/master/test-static-05.html"

    def setUp(self):
        self.driver = webdriver.Firefox()# Chrome non-op
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_hotkey(self):
        driver = self.driver

        shift_n_label = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "_Shift_n")
            )
        )

        # needs driver instance then can arrage sequence of events by
        # calling the availaable methods and executing the action with
        # the perform method
        ActionChains(driver).key_down(
            Keys.SHIFT
        ).send_keys(
            'n'
        ).key_up(
            Keys.SHIFT
        ).perform()
        self.assertEqual(
            "rgba(255, 255, 255, 1)",
            #"rgba(12, 162, 255, 1)",
            shift_n_label.value_of_css_property("background-color")
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)
