from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from utilities.wait_utility import WaitUtility


#page object model for improving locators interaction/ reusing the web-element command.
class LoginPage:
    def __init__(self,driver):
        self.driver =driver
        self.waitutility=WaitUtility()
        self.login_username = (By.XPATH, "//input[@placeholder='Username']") #pagefactory - for resue of locators
        self.login_password = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//button[text()='Sign In']")
    def enter_username(self,username_value):
        #login_username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        #login_username.send_keys(username_value)
        self.driver.find_element(*self.login_username).send_keys(username_value)
        return self
    def enter_password(self,password_value):
        #login_password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        #login_password.send_keys(password_value)
        self.driver.find_element(*self.login_password).send_keys(password_value)
        return self
    def perform_login(self):
        #login_signin = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        #login_signin.click()
        self.waitutility.wait_until_clickable(self.driver,self.driver.find_element(*self.login_button))
        self.driver.find_element(*self.login_button).click()
        return HomePage(self.driver)
