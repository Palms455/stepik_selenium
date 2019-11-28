import time
from selenium import webdriver
import pyperclip
import math


link = 'http://suninjuly.github.io/redirect_accept.html'

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_class_name('btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
   
    value = browser.find_element_by_id('input_value').text
    new_value = str(math.log(abs(12*math.sin(int(value)))))
    browser.find_element_by_id('answer').send_keys(new_value)
    browser.find_element_by_class_name('btn').click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    
    
finally:

    time.sleep(9)
    browser.quit()