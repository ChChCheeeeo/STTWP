# -*- coding: utf-8 -*-

from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to the application home
app_home = "http://demo.magentocommerce.com/"
# wait until page fully loaded before returning control to script
driver.get(app_home)

# get search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()

# get all anchor elements which display product name
# currently on the result pages using find_elements_by_xpath
xpath_query = "//h2[@class='product-name']/a"
# getting error of no len()? remember there's find_element and 
# find_elements
products = driver.find_elements_by_xpath(xpath_query)

# get  number of anchor elements found
print("Found " + str(len(products)) + " things: ")

# iterate through each anchor element and print product name
for product in products:
    print(product.text)

# close browser
driver.quit()