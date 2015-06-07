# -*- coding: utf-8 -*-

from homepagetests import HomePageTests
from searchtests import SearchTests

import HTMLTestRunner
import unittest
import os

# output file directory path
output_dir_path = os.getcwd()

# get all tests from SearchTests and HomePageTests
search_tests = unittest.TestLoader().loadTestsFromTestCase(
    SearchTests
)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(
    HomePageTests
)

# create test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# open report file
outfile = open(output_dir_path + "/SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Report',
    description='Smoke Tests'
)

# run suite using HTMLTestRunner
runner.run(smoke_tests)