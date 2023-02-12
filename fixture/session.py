from selenium.webdriver.common.by import By


class sessionHelper:
    def __init__(self, app):
        self.app = app

    def log_in(self, email, password):
        self.app.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.app.driver.find_element(By.ID, "Email").click()
        self.app.driver.find_element(By.ID, "Email").send_keys(email)
        self.app.driver.find_element(By.ID, "Password").send_keys(password)
        self.app.driver.find_element(By.CSS_SELECTOR, "label:nth-child(3)").click()
        self.app.driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    def log_out(self):
        self.app.driver.find_element(By.LINK_TEXT, "Log out").click()