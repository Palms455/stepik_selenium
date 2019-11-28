import time
from selenium import webdriver
import math


link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_id('input_value')
    x = input1.text
    
    def calcul(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calcul(int(x))
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    radio = browser.find_element_by_id('robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
    radio.click()
    browser.find_element_by_class_name('btn').click()
    
    
finally:
 
 
    time.sleep(9)
    browser.quit()
    