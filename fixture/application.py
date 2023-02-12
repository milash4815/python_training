from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def log_out(self):
        self.driver.find_element(By.LINK_TEXT, "Log out").click()

    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".item-box:nth-child(4) img").click()
        self.driver.execute_script("window.scrollTo(0,364)")
        self.driver.find_element(By.CSS_SELECTOR, ".product-essential").click()
        self.driver.find_element(By.ID, "addtocart_72_EnteredQuantity").send_keys("2")
        self.driver.find_element(By.ID, "add-to-cart-button-72").click()

    def log_in(self, email, password):
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "Email").click()
        self.driver.find_element(By.ID, "Email").send_keys(email)
        self.driver.find_element(By.ID, "Password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    def open_home_page(self, link):
        self.driver.get(link)
        self.driver.set_window_size(1936, 1056)

    def destroy(self):
        self.driver.quit()