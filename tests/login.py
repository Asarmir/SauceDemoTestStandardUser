from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import system.page


class LoginSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/randa/Documents/Chromedriver.exe")
        self.driver.get("https://www.saucedemo.com")

    # def test_login_saucedemo(self):
        
    #     login_page = system.page.LogInPage(self.driver)
    #     print(f"Test1:\n Title: {self.driver.title}\n")
    #     assert "Swag Labs" in self.driver.title

    #     login_page.input_username()
    #     login_page.input_password()
    #     login_page.login_button()

    #     print(f"Test2:\n Current url: {self.driver.current_url}")
    #     assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    def test_inventory(self):
        login = system.page.LogInPage(self.driver)
        login.input_username()
        login.input_password()
        login.login_button()
        
        inventorypage = system.page.InventoryPage(self.driver)
        inventorypage.add_to_cart_by_name("Sauce Labs Backpack")
        #inventorypage.add_to_cart_by_price("$29.99")

        inventorypage.add_to_cart_by_name("Sauce Labs Onesie")
        #inventorypage.add_to_cart_by_price("$7.99")
        inventorypage.check_cart_has_item()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


