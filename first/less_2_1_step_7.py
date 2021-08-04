from selenium import webdriver
import time
import math
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    treas = browser.find_element_by_id("treasure")
    x = treas.get_attribute("valuex")
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    chkbx = browser.find_element_by_id("robotCheckbox")
    chkbx.click()
    rbttn = browser.find_element_by_id("robotsRule")
    rbttn.click()
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
