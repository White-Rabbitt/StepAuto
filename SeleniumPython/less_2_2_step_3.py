from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text
    c = str(int(a)+int(b))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(c)
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()
finally:
    time.sleep(5)
    browser.quit()