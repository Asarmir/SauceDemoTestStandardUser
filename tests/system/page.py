from system.locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

	def __init__(self,driver):
		self.driver = driver

class LogInPage(BasePage):

	def input_username(self):
		username = self.driver.find_element(*LogInPageLocators.USERNAME_INPUT)
		username.clear()
		username.send_keys("standard_user")

	def input_password(self):
		password = self.driver.find_element(*LogInPageLocators.PASSWORD_INPUT)
		password.clear()
		password.send_keys("secret_sauce")

	def login_button(self):
		button = self.driver.find_element(*LogInPageLocators.LOGIN_BUTTON)
		button.click()

class InventoryPage(BasePage):

	"""
	This was my first idea which worked.
	def find_item(self, item):
		product = []
		itemname = self.driver.find_elements(*InventoryPageLocators.ITEM_NAME)

		for items in itemname:
			items = items.text
			product.append(items)
		
		result = product.index(item)
		print(f"Product found: {product[result]}")"""

	def add_to_cart_by_name(self, product):
    	
		itemname = self.driver.find_elements(*InventoryPageLocators.ITEM_NAME)

		for items in itemname:
			items = items.text

			if product == items: 
				print(f"Product found: {items}")
				button = self.driver.find_element(*InventoryPageLocators.ADD_TO_CART_BUTTON)
				print(f"I'm clicking: {button.text}")
				if len(button.text) == 11:					
					button.click()
					print('Product added to cart.\n')
				else:
					print("I didn't click a button")
			

	def add_to_cart_by_price(self,saletag):
    	
		itemprice = self.driver.find_elements(*InventoryPageLocators.ITEMPRICE)
	
		for price in itemprice:
			price = price.text
			
			if saletag == price:
				print(f"Product Price: {price}")
				button = self.driver.find_element(*InventoryPageLocators.ADD_TO_CART_BUTTON)
				print(f"I'm clicking: {button.text}")
				if len(button.text) == 11:					
					button.click()
					print('Product added to cart.\n')
				else:
					print("I didn't click a button")
			

	def check_cart_has_item(self):
		cartWithItem = self.driver.find_element(*InventoryPageLocators.SHOPPING_CART_WITH_ITEM).text
		if cartWithItem == "":
    			print('You have nothing in your cart.')
		if cartWithItem != "":
			print(f'You have {cartWithItem} items in your cart.')
