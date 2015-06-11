# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

import unittest, datetime, time

class ScreenShotTest(unittest.TestCase):
    """ScreenShotTest
        Captures screenshot when fails to locate element that should be
        present in home page applicatin.
    """

    def setUp(self):
        self.driver = webdriver.Firefox()# Chrome non-op
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("http://demo.magentocommerce.com/")

    # def tearDown(self):
    #     self.driver.quit()

    def test_screen_shot(self):
        driver = self.driver
        try:
            promo_banner_element = driver.find_element_by_id(
                "promo_banner"
            )
            self.assertEqual(
                "Promotions",
                promo_banner_element.text
            )
        except NoSuchElementException:
            st = datetime.datetime.fromtimestamp(
                time.time()
            ).strftime('%Y%m%d_%H%M%S')
            file_name = "main_page_missing_banner" + st + ".png"
            driver.save_screenshot(file_name)
           # raise

if __name__ == '__main__':
    unittest.main(verbosity=2)