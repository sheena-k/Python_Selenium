from selenium.webdriver.common.by import By
from utilities.wait_utility import WaitUtility
class ManageCod:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.manage_cod_icon = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/add-cod' and @class='small-box-footer']")
        self.button_cod_no_click = (By.XPATH,"//input[@value='no' and @type='radio' and @name='cod']")
        self.button_cod_yes_click = (By.XPATH,"//input[@value='yes' and @type='radio' and @name='cod']")
        self.cod_save = (By.XPATH, "//button[contains(text(),'Save') and @name='create']")
    def cod_icon_click(self):
        #manage_cod_icon = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/add-cod' and @class='small-box-footer']")
        #manage_cod_icon.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.manage_cod_icon))
        self.driver.find_element(*self.manage_cod_icon).click()
        return self
    def button_cod_no_icon(self):
        #button_cod_no_click = self.driver.find_element(By.XPATH,"//input[@value='no' and @type='radio' and @name='cod']")
        #button_cod_no_click.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.button_cod_no_click))
        self.driver.find_element(*self.button_cod_no_click).click()
        return self
    def button_cod_yes_icon(self):
        #button_cod_yes_click = self.driver.find_element(By.XPATH,"//input[@value='yes' and @type='radio' and @name='cod']")
        #button_cod_yes_click.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.button_cod_yes_click))
        self.driver.find_element(*self.button_cod_yes_click).click()
        return self
    def cod_save_icon(self):
        #cod_save = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save') and @name='create']")
        #cod_save.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.cod_save))
        self.driver.find_element(*self.cod_save).click()
        return self
