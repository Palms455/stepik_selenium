import math
from selenium import webdriver
import time
import pytest


@pytest.fixture(scope = 'module')
def browser():
	browser = webdriver.Chrome()
	yield browser
	browser.quit





@pytest.mark.parametrize('siten', ['236895','236896','236897', '236898' ,'236899','236903', '236904', '236905'])
def test_stepik(browser,siten):
	link = f'https://stepik.org/lesson/{siten}/step/1'
	browser.get(link)
	browser.implicitly_wait(5)
	number = math.log(int(time.time()))
	browser.find_element_by_css_selector('[placeholder]').send_keys(str(number))
	browser.find_element_by_class_name('submit-submission').click()

	browser.implicitly_wait(5)
	answer = browser.find_element_by_class_name('smart-hints__hint').text
	assert answer == 'Correct!', f'expected Correct, got {answer}'
