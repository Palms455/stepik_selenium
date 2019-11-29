from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/get_attribute.html'
def calculate(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
    
try:

    browser = webdriver.Chrome()
    browser.get(link)

    sunduk = browser.find_element_by_id('treasure')
    x = sunduk.get_attribute('valuex')
    y = calculate(x)
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    
    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()
    
    input3 = browser.find_element_by_id('robotsRule')
    input3.click()
    
    button = browser.find_element_by_class_name('btn')
    button.click()



finally:
    
    time.sleep(9)
    browser.quit()
