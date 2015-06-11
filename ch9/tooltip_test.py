# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class ToolTiptest(unittest.TestCase):
    """ToolTiptest
        Call mouse move event moves mouse cursor from current location
        to supplied element.
    """

    URL = "http://jqueryui.com/tooltip/"

    def setUp(self):
        self.driver = webdriver.Firefox()# Chrome non-op
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_tool_tip(self):
        driver = self.driver

        frame_element = driver.find_element_by_class_name("demo-frame")
        driver.switch_to.frame(frame_element)

        age_field = driver.find_element_by_id("age")
        ActionChains(self.driver).move_to_element(
            age_field
        ).perform()

        tool_tip_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, "ui-tooltip-content")
            )
        )

        # verify tooltip message
        self.assertEqual(
            "We ask for your age only for statistical purposes.",
            tool_tip_element.text
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)
