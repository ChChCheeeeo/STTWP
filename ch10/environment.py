# -*- coding: utf-8 -*-
from selenium import webdriver

# This is the enviroment file that is used to set up common
# Behave settings and any code that is shared between steps
# or step definition files before running any feature.
# execute methods before and after feature are executed

def before_all(context):
    context.driver = webdriver.Firefox()

def after_all(context):
    context.driver.quit()