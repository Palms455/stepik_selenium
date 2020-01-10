from selenium import webdriver

class BasePage():
 	
 	def __init__(self, browser, url):
 		self.url = url
 		self.browser = browser
 		self.browser.implicitly_wait(timeout) # неявное ожидание элемента
 		

 	def open(self):
 		self.browser.get(self.url)

 	def close(self):
 		return self.browser.close()

