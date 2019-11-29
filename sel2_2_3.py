import time
from selenium import webdriver
import math
import os


link = 'http://suninjuly.github.io/file_input.html'

try:

    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_css_selector('[name="firstname"]').send_keys('Ivan')

    browser.find_element_by_css_selector('[name="lastname"]').send_keys('Petrov')

    browser.find_element_by_css_selector('[name="email"]').send_keys('Ivansfsfefsef@ffdrfdrf.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'super.txt')
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_class_name('btn').click()
   
    
    
finally:
 
 
    time.sleep(9)
    browser.quit()
    
