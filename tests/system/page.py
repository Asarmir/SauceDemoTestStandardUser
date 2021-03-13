from system.locator import *


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
	def find_item(self):
		product = []

		itemname = self.driver.find_elements(*InventoryPageLocators.ITEM_NAME)
		
		for items in itemname:
			items = items.text
			product.append(items)
		
		return product

	def add_to_cart_by_name(self, item):
		product = self.find_item()

		button = self.driver.find_elements(*InventoryPageLocators.ADD_TO_CART_BUTTON)
		print(f"\nI have found: {len(button)} buttons")
		
		result = product.index(item)

		if item == product[result]:
			print(f"Product found: {product[result]}")
			print(f"Adding to Cart: {product[result]}")
			if len(button) == 6:
				button[result].click()
				print(f"\nI've clicked: {product[result]}:\nIndice: {result}")
			else:
				button[result - 1].click()
				print(f"\nI've clicked: {product[result]}:\nIndice: {result}")
					
	def check_cart_has_item(self):
		cartWithItem = self.driver.find_element(*InventoryPageLocators.SHOPPING_CART_WITH_ITEM).text
		if cartWithItem == "":
			print('\nYou have nothing in your cart.')
		if cartWithItem != "":
			print(f'\nYou have {cartWithItem} items in your cart.')

	def click_cart_icon(self):
		
		cartButton = self.driver.find_element(*InventoryPageLocators.SHOPPING_CART)
		cartButton.click()
		
class CartPage(BasePage):
		
	def check_cart(self, product):

		items = InventoryPage.find_item(self)
		result = items.index(product)
		
		if product == items[result]:
			print(f"Product match found: {items[result]}")
		else:
			print(f"{product} not found")
			
