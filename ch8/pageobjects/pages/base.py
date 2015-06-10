# -*- coding: utf-8 -*-

from abc import abstractmethod
# BasePage object acts as a parent object for all the page objects 
# created in test suite. it provides common code that the page object 
# can use.

class BasePage(object):
    """BasePage
        All page objects inherit from this.
    """

    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        # will be implimented by inheriting page objects from BasePage
        # to validate that page represented is loaded in teh browser
        # before test can use attributes or actions.
        return

    """ Regions define functionality available through all page objects """
    @property
    def search(self):
        # similar to page object. SearchRegion represents search box
        # displayed on all application pages. So adding to each page
        # object is sharing this from the BasePage class.
        from .search import SearchRegion
        return SearchRegion(self.driver)


class InvalidPageException(Exception):
    """InvalidPageException
        Throw this exception when correct page not found.
    """
    pass
