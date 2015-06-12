# -*- coding: utf-8 -*-
from selenium import webdriver

# execute methods before and after feature are executed

def before_all(context):
    context.driver = webdriver.Firefox()

def after_all(context):
    context.driver.quit()