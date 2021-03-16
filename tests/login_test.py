from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import system.page
import time


class LoginSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:/Users/randa/Documents/Chromedriver.exe")
        self.driver.get("https://www.saucedemo.com")

    def test_login_saucedemo(self):

        login_page = system.page.LogInPage(self.driver)
        print(f"Test1:\n Title: {self.driver.title}\n")
        assert "Swag Labs" in self.driver.title

        login_page.input_username()
        login_page.input_password()
        login_page.login_button()

        print(f"Test2:\n Current url: {self.driver.current_url}")
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    def test_add_to_cart(self):
        # Rewrote login to remove all the prints and assert
        login = system.page.LogInPage(self.driver)
        login.input_username()
        login.input_password()
        login.login_button()

        #Checks gets the page and product by name
        inventorypage = system.page.InventoryPage(self.driver)
        inventorypage.add_to_cart_by_name("Sauce Labs Backpack")

        inventorypage.add_to_cart_by_name("Sauce Labs Onesie")
        # Checks if you have items in cart and returns how many.
        inventorypage.check_cart_has_item()

        # Clicks the cart icon and moves to cart.html
        inventorypage.click_cart_icon()
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html"
        print(f"\nTest 3:\nCurrent url: {self.driver.current_url}")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
