# -*- coding: utf-8 -*-

from homepagetests import HomePageTests
from searchtests import SearchTests

import unittest

# get all tests from SearchTest HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)

# create test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# run suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)