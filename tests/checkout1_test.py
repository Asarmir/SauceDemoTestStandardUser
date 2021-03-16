from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import system.page
import time


class Checkout1SauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:/Users/randa/Documents/Chromedriver.exe")
        self.driver.get("https://www.saucedemo.com")


    # def test_checkout_step1(self):

    #     login = system.page.LogInPage(self.driver)
    #     login.input_username()
    #     login.input_password()
    #     login.login_button()

    #     inventorypage = system.page.InventoryPage(self.driver)

    #     inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
    #     inventorypage.add_to_cart_by_name("Sauce Labs Onesie")

    #     inventorypage.check_cart_has_item()
    #     inventorypage.click_cart_icon()

    #     cartpage = system.page.CartPage(self.driver)
    #     print(f"\nPage: {self.driver.current_url}")

    #     cartpage.check_cart("Sauce Labs Backpack")
    #     cartpage.check_cart("Sauce Labs Onesie")

    #     cartpage.click_checkout()
    #     # time.sleep(2)
    #     assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    #     print(f"\n Current page: {self.driver.current_url}")


    # def test_checkout_step1_cancel(self):
    #     login = system.page.LogInPage(self.driver)
    #     login.input_username()
    #     login.input_password()
    #     login.login_button()

    #     inventorypage = system.page.InventoryPage(self.driver)

    #     inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
    #     inventorypage.add_to_cart_by_name("Sauce Labs Onesie")

    #     inventorypage.check_cart_has_item()
    #     inventorypage.click_cart_icon()

    #     cartpage = system.page.CartPage(self.driver)
    #     print(f"\n Current page: {self.driver.current_url}")

    #     cartpage.check_cart("Sauce Labs Backpack")
    #     cartpage.check_cart("Sauce Labs Onesie")

    #     cartpage.click_checkout()
    #     # time.sleep(2)
    #     print(f"\n Current page: {self.driver.current_url}")

    #     checkoutstep1 = system.page.CheckoutStep1(self.driver)
    #     checkoutstep1.click_cancel()

    #     assert self.driver.current_url == "https://www.saucedemo.com/cart.html"
    #     print(f"\n Current page: {self.driver.current_url}")
    
    # def test_checkout_step1_firstname_error(self):

    #     login = system.page.LogInPage(self.driver)
    #     login.input_username()
    #     login.input_password()
    #     login.login_button()

    #     inventorypage = system.page.InventoryPage(self.driver)

    #     inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
    #     inventorypage.add_to_cart_by_name("Sauce Labs Onesie")

    #     inventorypage.check_cart_has_item()
    #     inventorypage.click_cart_icon()

    #     cartpage = system.page.CartPage(self.driver)
    #     print(f"\n Current page: {self.driver.current_url}")

    #     cartpage.check_cart("Sauce Labs Backpack")
    #     cartpage.check_cart("Sauce Labs Onesie")

    #     cartpage.click_checkout()
    #     print(f"\n Current page: {self.driver.current_url}")

    #     checkoutstep1 = system.page.CheckoutStep1(self.driver)
    #     checkoutstep1.click_continue()
    #     checkoutstep1.error_message()
        # time.sleep(2)
    # def test_check_step1_lastname_error(self):
    #     login = system.page.LogInPage(self.driver)
    #     login.input_username()
    #     login.input_password()
    #     login.login_button()

    #     inventorypage = system.page.InventoryPage(self.driver)

    #     inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
    #     inventorypage.add_to_cart_by_name("Sauce Labs Onesie")

    #     inventorypage.check_cart_has_item()
    #     inventorypage.click_cart_icon()

    #     cartpage = system.page.CartPage(self.driver)
    #     print(f"\nCurrent page: {self.driver.current_url}")

    #     cartpage.check_cart("Sauce Labs Backpack")
    #     cartpage.check_cart("Sauce Labs Onesie")

    #     cartpage.click_checkout()
    #     print(f"\nCurrent page: {self.driver.current_url}")

    #     checkoutstep1 = system.page.CheckoutStep1(self.driver)
    #     checkoutstep1.input_firstname()
    #     checkoutstep1.click_continue()
    #     checkoutstep1.error_message()
    
    # def test_checkout_step1_zipcode_error(self):
    #     login = system.page.LogInPage(self.driver)
    #     login.input_username()
    #     login.input_password()
    #     login.login_button()

    #     inventorypage = system.page.InventoryPage(self.driver)

    #     inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
    #     inventorypage.add_to_cart_by_name("Sauce Labs Onesie")

    #     inventorypage.check_cart_has_item()
    #     inventorypage.click_cart_icon()

    #     cartpage = system.page.CartPage(self.driver)
    #     print(f"\nCurrent page: {self.driver.current_url}")

    #     cartpage.check_cart("Sauce Labs Backpack")
    #     cartpage.check_cart("Sauce Labs Onesie")

    #     cartpage.click_checkout()
    #     print(f"\nCurrent page: {self.driver.current_url}")

    #     checkoutstep1 = system.page.CheckoutStep1(self.driver)
    #     checkoutstep1.input_firstname()
    #     checkoutstep1.input_lastname()
    #     checkoutstep1.click_continue()
    #     checkoutstep1.error_message()
    
    # def test_checkout_step1_continue(self):
    #     login = system.page.LogInPage(self.driver)
    #     login.input_username()
    #     login.input_password()
    #     login.login_button()

    #     inventorypage = system.page.InventoryPage(self.driver)

    #     inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
    #     inventorypage.add_to_cart_by_name("Sauce Labs Onesie")

    #     inventorypage.check_cart_has_item()
    #     inventorypage.click_cart_icon()

    #     cartpage = system.page.CartPage(self.driver)
    #     print(f"\nCurrent page: {self.driver.current_url}")

    #     cartpage.check_cart("Sauce Labs Backpack")
    #     cartpage.check_cart("Sauce Labs Onesie")

    #     cartpage.click_checkout()
    #     print(f"\nCurrent page: {self.driver.current_url}")

    #     checkoutstep1 = system.page.CheckoutStep1(self.driver)
    #     checkoutstep1.input_firstname()
    #     checkoutstep1.input_lastname()
    #     checkoutstep1.input_zipcode()
    #     checkoutstep1.click_continue()
    #     print(self.driver.current_url)

    def test_complete_order(self):
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

        complete = system.page.CheckoutStep2(self.driver)
        complete.click_finish()
        print()
        print(self.driver.current_url)
        assert complete.message_complete() == "THANK YOU FOR YOUR ORDER"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
