import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

try:

    browser = webdriver.Chrome()
    browser.get(link)
    
    
    val = browser.find_element_by_id('num1')
    val1 = val.text
    val0 = browser.find_element_by_id('num2')
    val2 = val0.text
    print(val2)

    print(val1)
    summ = int(val1) + int(val2)
    select = Select(browser.find_element_by_css_selector('select#dropdown'))
    select.select_by_value(str(summ))
    button = browser.find_element_by_class_name('btn').click()
    
finally:

    time.sleep(9)

    browser.quit()
