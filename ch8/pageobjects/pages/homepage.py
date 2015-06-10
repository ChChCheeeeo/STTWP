# -*- coding: utf-8 -*-
from base import InvalidPageException
from base import BasePage


class HomePage(BasePage):
    """HomePage
        Page ojects for each page that'll be dealt with in test.
    """

    _home_page_slideshow_locator = 'div.slidesohw-container'

    def __int__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name(
                self._home_page_slideshow_locator
            )
        except:
            raise InvalidPageException(
                "Home page not loaded"
            )