from selenium import webdriver



def openPage():
    PATH = 'C:/Users/randa/Documents/Chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    driver.get('https://www.saucedemo.com/')

    assert "Swag Labs" in driver.title
    print(driver.title)

def log_in():
    PATH = 'C:/Users/randa/Documents/Chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    driver.get('https://www.saucedemo.com')

    username = driver.find_element_by_id("user-name")
    username.clear()
    username.send_keys("standard_user")

    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys("secret_sauce")

    driver.find_element_by_id("login-button").click()
    print(driver.current_url)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'


log_in()