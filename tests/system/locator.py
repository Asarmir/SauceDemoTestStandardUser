from selenium.webdriver.common.by import By

class LogInPageLocators(object):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = ( By.ID, "login-button")

class InventoryPageLocators(object):
    
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    ITEMPRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[class='btn_primary btn_inventory']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[class='btn_secondary btn_inventory']")
    
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_container")
    SHOPPING_CART_WITH_ITEM = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

class CartPageLocators(object):
    ITEMNAME = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[class='btn_secondary']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a[class='btn_action checkout_button']")
    
class Checkoutstep1Locators(object):
    CANCEL_BUTTON = (By.CSS_SELECTOR, "a[class='cart_cancel_link btn_secondary']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[class='btn_primary cart_button']") 
    ERROR_MESSAGE = (By.TAG_NAME, "h3")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='first-name']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='last-name']")
    ZIPCODE_INPUT = (By.CSS_SELECTOR,"input[id='postal-code']")

class CheckoutStep2Locators(object):
    FINISH_BUTTON = (By.CSS_SELECTOR, "a[class='btn_action cart_button']")
    COMPLETE_MESSAGE = (By.TAG_NAME, "h2[class='complete-header']")