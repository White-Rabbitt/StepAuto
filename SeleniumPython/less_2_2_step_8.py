from selenium import webdriver
import time
import math
import os
link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("White Rabbit")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Lacrimozzy")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("wrbbt@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__)) #получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'testfile.txt') #добавляем к этому пути имя файла
    file = browser.find_element_by_id("file")
    file.send_keys(file_path) #отправляем выбранный файл
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
finally:
	time.sleep(5)
	browser.quit()
