# -*- coding: utf-8 -*-

from base.basetestcase import BaseTestCase
from pages.homepage import HomePage
import unittest

class SearchProductTest(BaseTestCase):
    """SearchProductTest
        Call page objcts and test application search feature.
    """

    def testSearchForProduct(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor('earphones')
        self.assertEqual(2, search_results.product_count)
        product = search_results.open_product_page('MADISON EARBUDS')
        self.assertEqual('MADISON EARBUDS', product.name)
        self.assertEqual('$35.00', product.price)
        self.assertEqual('IN STOCK', product.stock_status)

if __name__ == '__main__':
    unittest.main(verbosity=2)