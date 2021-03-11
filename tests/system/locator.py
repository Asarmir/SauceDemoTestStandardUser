from selenium.webdriver.common.by import By

class LogInPageLocators(object):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = ( By.ID, "login-button")

class InventoryPageLocators(object):
    ITEM_BLOCK = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    ITEMPRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='btn_primary btn_inventory']")
    
    SHOPPING_CART= (By.CLASS_NAME, "shopping_cart_container")
    SHOPPING_CART_WITH_ITEM = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    