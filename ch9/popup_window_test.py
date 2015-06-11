# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

# need to install Castro and PyGame
class PopupWindowTest(unittest.TestCase):
    """PopupWindowTest
        Working with popup child windows. Can work with any child window
        as long as it belongs to the current WebDriver context.
    """

    URL = 'https://rawgit.com/upgundecha/learnsewithpython/master/pages/Config.html'

    def setUp(self):

        self.driver = webdriver.Firefox()# Chrome non-op
        self.driver.implicitly_wait(30)
        self.driver.get(self.URL)
        self.driver.maximize_window()

    # def tearDown(self):
    #     self.driver.close()#quit()

    def test_window_popup(self):
        driver = self.driver

        # save Parent Browser's Window WindowHandle 
        parent_window_id = driver.current_window_handle
        print("This is parent_window_id: {}".format(parent_window_id))

        # clicking Help Button will open Help Page in a new popup browser window
        help_button = driver.find_element_by_id('helpbutton')
        help_button.click()

        driver.switch_to.window("HelpWindow")
        child_window_id = driver.current_window_handle
        print("This is child_window_id: {}".format(child_window_id))
        driver.close()

        driver.switch_to.window(parent_window_id)
        print("back to window_id: {}".format(driver.current_window_handle))

if __name__ == '__main__':
    unittest.main(verbosity=2)