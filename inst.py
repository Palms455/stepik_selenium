import time
from selenium import webdriver
from random import randint 

i = 0
link = 'http://www.instagram.com/accounts/login/?source=auth_switcher'

try:

    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    user = browser.find_element_by_css_selector('[name="username"]')
    user.send_keys(input('email or number phone'))
    passw = browser.find_element_by_css_selector('[name="password"]')
    passw.send_keys(str(input('password')))
    enter = browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(10)
    while True:
        if i >= 50:
            time.sleep(150)
            i = 0
        like= browser.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9')
        time.sleep(randint(2,9))
        browser.execute_script('return arguments[0].scrollIntoView(false);', like)
        n = randint(1,9)
        for j in range(n):
            browser.execute_script("window.scrollBy(0,9);")
        time.sleep(randint(1,6))
        like.click()
        i += 1
finally:
    pass


    
