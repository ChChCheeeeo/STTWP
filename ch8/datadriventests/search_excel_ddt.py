# -*- coding: utf-8 -*-
from ddt import ddt, data, unpack
from selenium import webdriver
import unittest, xlrd

# search test accepts pair of arguments for different
# search tearms and expected results count
# pass list of tuples using @data decorator
# @unpack to unpack tuples into multiple arguments


def get_data(file_name):
    rows = []
    # open specifiedexcel spreadsheet as workbook
    book = xlrd.open_workbook(file_name)

    # get first sheet
    sheet = book.sheet_by_index(0)

    # iterate through sheet and get data from rows into a list
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))

    return rows

@ddt
class SearchExcelDDT(unittest.TestCase):
    """SearchExcelDDT
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigatetosite
        self.driver.get("http://demo.magentocommerce.com/")

    def tearDown(self):
        self.driver.quit()

    # get data from specific excel file
    # read supplied files and return list of values back
    @data(*get_data("TestData.xlsx"))
    @unpack
    def test_search(self, search_value, expected_count):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter and submitsearch keyword
        # use search_value arg to pass data
        self.search_field.send_keys(search_value)
        self.search_field.submit()

        # get all anchors elements with have product names
        # currently displaed on result page using xpath
        products = self.driver.find_elements_by_xpath(
            "//h2[@class='product-name']/a"
        )
        expected_count = int(expected_count)

        if expected_count > 0:
            # check products count
            self.assertEqual(expected_count, len(products))
        else:
            msg = self.driver.find_element_by_class_name("note-msg")
            self.assertEqual(
                "Your search returns no results.",
                msg.text
            )
if __name__ == '__main__':
    unittest.main(verbosity=2)
