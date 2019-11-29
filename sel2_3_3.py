import time
import pyperclip
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



link = 'http://suninjuly.github.io/explicit_wait2.html'

try: 
    browser = webdriver.Chrome()

    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    browser.find_element_by_id('book').click()
    

    value = browser.find_element_by_id('input_value').text

    new_value = str(math.log(abs(12*math.sin(int(value)))))
    browser.find_element_by_id('answer').send_keys(new_value)
    browser.find_element_by_id('solve').click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    
    
finally:

    time.sleep(9)
    browser.quit()
