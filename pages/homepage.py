from selenium.webdriver.common.by import By
#from pages.loginpage import LoginPage
from utilities.wait_utility import WaitUtility
class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.home_icon = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/home' and contains(text(),'Home')]")
        self.admin_icon = (By.XPATH,"//a[@class='nav-link' and @data-toggle='dropdown']")
        self.logout_icon = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/logout' and @class='dropdown-item']")
    def home_icon_func(self):
        #home_icon = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/home' and contains(text(),'Home')]")
        #home_icon.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.home_icon))
        self.driver.find_element(*self.home_icon).click()
        return self
    def admin_icon_func(self):
        #admin_icon = self.driver.find_element(By.XPATH, "//a[@class='nav-link' and @data-toggle='dropdown']")
        #admin_icon.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.admin_icon))
        self.driver.find_element(*self.admin_icon).click()
        return self
    def logout_icon_func(self):
        #logout_icon = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/logout' and @class='dropdown-item']")
        #logout_icon.click()
        from pages.loginpage import LoginPage
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.logout_icon))
        self.driver.find_element(*self.logout_icon).click()
        return LoginPage(self.driver)