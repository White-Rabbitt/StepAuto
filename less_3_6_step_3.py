import pytest
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestUfo():
    message = ''
    massive = ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1",
               "236904/step/1", "236905/step/1"]

    @pytest.mark.parametrize('links', massive)
    def test_ufo(self, browser, links):
        answer = math.log(int(time.time()))
        answer_text = str(answer)
        link = f"https://stepik.org/lesson/{links}/"
        browser.get(link)
        browser.implicitly_wait(10)
        input = browser.find_element_by_css_selector(".ember-text-area.ember-view")
        input.send_keys(answer_text)
        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()
        ufo_msg = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        ufo_text = ufo_msg.text
        assert ufo_text != 'Correct!'
        if ufo_text != 'Correct!':
            TestUfo.message += ufo_text
            print(self.message)

        print(TestUfo.message)