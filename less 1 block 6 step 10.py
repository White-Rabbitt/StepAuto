from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector ("input[placeholder='Input your first name']")
    input1.send_keys("Vasya")
    input2 = browser.find_element_by_css_selector ("input[placeholder='Input your last name']")
    input2.send_keys("Pupkin")
    input3 = browser.find_element_by_css_selector ("input[placeholder='Input your email']")
    input3.send_keys("vasy1@mail.ru")
    input4 = browser.find_element_by_css_selector ("input[placeholder='Input your phone:']")
    input4.send_keys("+79999999999")
    input5 = browser.find_element_by_css_selector ("input[placeholder='Input your address:']")
    input5.send_keys("ul Pushkina dom Kolotushkina")
    button = browser.find_element_by_css_selector ("button.btn")
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()
