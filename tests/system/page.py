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
			return items[result]
		else:
			print(f"{product} not found")

	def return_to_shop(self):
		button = self.driver.find_element(*CartPageLocators.CONTINUE_BUTTON)
		button.click()

	def get_all_remove_button(self):
    	
		remove = []
		button = self.driver.find_elements(*InventoryPageLocators.REMOVE_BUTTON)

		for rb in button:
			remove.append(rb)

		return remove
			

	def get_add_cart_button(self):
		button = self.driver.find_elements(*InventoryPageLocators.ADD_TO_CART_BUTTON)
		removebutton = self.driver.find_elements(*InventoryPageLocators.REMOVE_BUTTON)
		print(f"\nThere are: {len(button)} add to cart buttons\nThere are: {len(removebutton)} remove buttons")
		return len(removebutton)

	def click_remove_button(self,item):
		product = InventoryPage.find_item(self)

		button = self.get_all_remove_button()
		print(f"\nI have found: {len(button)} buttons")
		
		result = product.index(item)

		if item == product[result]:
			print(f"Product found: {product[result]}")
			print(f"Adding to Cart: {product[result]}")
			button[0].click()
			print(f"\nI've clicked: {product[result]}:\nIndice: {result}")
	
	def click_checkout(self):
		button = self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON)
		button.click()

class CheckoutStep1(BasePage):
	
	def click_cancel(self):
		button = self.driver.find_element(*Checkoutstep1Locators.CANCEL_BUTTON)
		button.click()

	def click_continue(self):
		button = self.driver.find_element(*Checkoutstep1Locators.CONTINUE_BUTTON)
		button.click()

	def error_message(self):
		message = self.driver.find_element(*Checkoutstep1Locators.ERROR_MESSAGE)
		print(message.text)
		return message.text

	def input_firstname(self):
		input = self.driver.find_element(*Checkoutstep1Locators.FIRSTNAME_INPUT)
		input.clear()
		input.send_keys("Sebestian")

	def input_lastname(self):
		input = self.driver.find_element(*Checkoutstep1Locators.LASTNAME_INPUT)
		input.clear()
		input.send_keys("HAYES")


	def input_zipcode(self):
		input = self.driver.find_element(*Checkoutstep1Locators.ZIPCODE_INPUT)
		input.clear()
		input.send_keys("78652")

class CheckoutStep2(BasePage):
    	
	def click_finish(self):
		button = self.driver.find_element(*CheckoutStep2Locators.FINISH_BUTTON)
		button.click()

	def message_complete(self):
		message = self.driver.find_element(*CheckoutStep2Locators.COMPLETE_MESSAGE)
		print(message.text)
		return message.text
