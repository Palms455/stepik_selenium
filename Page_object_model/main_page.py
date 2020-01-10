from base_class import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
#импортируем модуль базового класса

class MainPage(BasePage):
	def go_to_login_page(self):
		#self.browser.find_element_by_css_selector('#login_link')
		login_link=self.browser.find_element(By.CSS_SELECTOR, '#login_link')
		login_link.click()

		