# -*- coding: utf-8 -*-
from behave import *

# use of GHerkin langauge's GWT
# Given
# When
# Then

# Behave uses the context variable to store information to share 
# around. It runs at three levels, automatically managed by Behave. 
# Can also use context variable to store and share information 
# between the steps.



# create a matching step definition for each GWT
@given('I am on home page')
def step_i_am_on_home_page(context):
    context.driver.get("http://demo.magentocommerce.com")

# can also pass parameters embedded in steps to definition.
@when('I search for {text}')
def step_i_search_for(context, text):
    search_field = context.driver_find_element_by_name("q")
    search_field.clear()

    search_field.send_keys(text)
    search_field.submit()

@then('I should see list of matching products in search results')
def step_i_should_see_list(context):
    products = context.driver.find_elements_by_xpath(
        "//h2[@class='products-name']/a"
    )
    assert len(products) > 0

