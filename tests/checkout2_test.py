from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import system.page
import time


class Checkout2SauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:/Users/randa/Documents/Chromedriver.exe")
        self.driver.get("https://www.saucedemo.com")

    def test_checkoutstep2(self):
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
        print(f"\nCurrent page: {self.driver.current_url}")

        cartpage.check_cart("Sauce Labs Backpack")
        cartpage.check_cart("Sauce Labs Onesie")

        cartpage.click_checkout()
        print(f"\nCurrent page: {self.driver.current_url}")

        checkoutstep1 = system.page.CheckoutStep1(self.driver)
        checkoutstep1.input_firstname()
        checkoutstep1.input_lastname()
        checkoutstep1.input_zipcode()
        checkoutstep1.click_continue()
        print(self.driver.current_url)

        checkoutstep2 = system.page.CheckoutStep2(self.driver)
        checkoutstep2.click_finish()
        print(self.driver.current_url)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
