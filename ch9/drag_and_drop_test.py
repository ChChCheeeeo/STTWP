# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

import unittest

class DragAndDroptest(unittest.TestCase):
    """DragAndDroptest
        Method requires source element that'll be dragged, target element
        where source element will be dropped.
    """

    URL = "http://jqueryui.com/resources/demos/droppable/default.html"

    def setUp(self):
        self.driver = webdriver.Firefox()# Chrome non-op
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    # def tearDown(self):
    #     self.driver.quit()

    def test_drag_and_drop(self):
        driver = self.driver

        source = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("droppable")

        ActionChains(self.driver).drag_and_drop(source, target).perform()

        self.assertEqual("Dropped!", target.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
