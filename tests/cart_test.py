from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import system.page
import time

class CartSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:/Users/randa/Documents/Chromedriver.exe")
        self.driver.get("https://www.saucedemo.com")
 
    def test_items_on_cartpage(self):
    
        login = system.page.LogInPage(self.driver)
        login.input_username()
        login.input_password()
        login.login_button()

        inventorypage = system.page.InventoryPage(self.driver)

        inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
        inventorypage.add_to_cart_by_name("Sauce Labs Onesie")

        inventorypage.check_cart_has_item()
        inventorypage.click_cart_icon()

        cartpage = system.page.CartPage(self.driver)
        print(f"\nPage: {self.driver.current_url}")

        cartpage.check_cart("Sauce Labs Backpack")
        cartpage.check_cart("Sauce Labs Onesie")

        assert cartpage.check_cart("Sauce Labs Backpack") == "Sauce Labs Backpack"
        assert cartpage.check_cart("Sauce Labs Onesie") == "Sauce Labs Onesie"

    def test_cart_continue_shopping(self):

        login = system.page.LogInPage(self.driver)
        login.input_username()
        login.input_password()
        login.login_button()

        inventorypage = system.page.InventoryPage(self.driver)

        inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
        inventorypage.add_to_cart_by_name("Sauce Labs Onesie")

        inventorypage.check_cart_has_item()
        inventorypage.click_cart_icon()

        cartpage = system.page.CartPage(self.driver)
        print(f"\nPage: {self.driver.current_url}")

        cartpage.check_cart("Sauce Labs Backpack")
        cartpage.check_cart("Sauce Labs Onesie")

        cartpage.return_to_shop()
        print(f"\nPage: {self.driver.current_url}")
        print(inventorypage.find_item())
        #time.sleep(5)

        assert cartpage.get_add_cart_button() == 2

        cartpage.click_remove_button("Sauce Labs Backpack")
        cartpage.click_remove_button("Sauce Labs Onesie")
        assert cartpage.get_add_cart_button() == 0
        print("Test Pass - All removed buttons have been clicked.")

   
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
