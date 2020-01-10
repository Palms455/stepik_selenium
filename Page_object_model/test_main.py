from main_page import MainPage 
from selenium import webdriver

broser = webdrider.Chrome()

def  test_quest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser,link)
	page.open()
	page.go_to_login_page()
