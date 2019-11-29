import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/math.html'
def calcul(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
    
try:

    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calcul(x)
    input1 = browser.find_element_by_id('answer')

    input1.send_keys(y)
    
    input2 = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    input2.click()
    
    input3 = browser.find_element_by_css_selector('[for="robotsRule"]')
    input3.click()
    
    button = browser.find_element_by_class_name('btn')
    button.click()



finally:
    
    time.sleep(9)

    browser.quit()


