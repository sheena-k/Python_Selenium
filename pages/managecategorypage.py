from selenium.webdriver.common.by import By
from utilities.wait_utility import WaitUtility

class CategoryPage:
    def __init__(self,driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.category_icon = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-category' and contains(@class,'small-box-footer')]")

    def manage_category_icon(self):
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.category_icon))
        self.driver.find_element(*self.category_icon).click()
        return self
