from selenium.webdriver.common.by import By
from utilities.wait_utility import WaitUtility
class ManagePage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility =WaitUtility()
        self.manage_page_icon = (By.XPATH,"//a[ contains(@href,'admin/list-page') and @class='small-box-footer']")
        self.cashew_edit_icon = (By.XPATH,"//a[@class='btn btn-sm btn btn-primary btncss' and (@href='https://groceryapp.uniqassosiates.com/admin/pages/edit?edit=48&page_ad=1')]")
        self.cashew_description = (By.XPATH, "//div[@class='note-editable card-block']")
        self.upload_file_icon = (By.XPATH, "//input[@type='file' and @name='main_img']")
        self.update_cashew_details = (By.XPATH,"//button[@name='update' and contains(@class,'btn-danger')]")
    def manage_page_icon_func(self):
        #manage_page_icon = self.driver.find_element(By.XPATH,"//a[ contains(@href,'admin/list-page') and @class='small-box-footer']")
        #manage_page_icon.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.manage_page_icon))
        self.driver.find_element(*self.manage_page_icon).click()
        return self
    def cashew_edit_icon_func(self):
        #cashew_edit_icon = self.driver.find_element(By.XPATH,"//a[@class='btn btn-sm btn btn-primary btncss' and (@href='https://groceryapp.uniqassosiates.com/admin/pages/edit?edit=48&page_ad=1')]")
        #cashew_edit_icon.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.cashew_edit_icon))
        self.driver.find_element(*self.cashew_edit_icon).click()
        return self

    def cashew_description_func(self):
        #cashew_description = self.driver.find_element(By.XPATH, "//div[@class='note-editable card-block']")
        #cashew_description.send_keys("cashew edible nut")

        self.driver.find_element(*self.cashew_description).send_keys("cashew edible nut")
        return self

    def cashew_uploadfile_func(self):
        file_path = r"C:\Users\hp\OneDrive\Desktop\cashews_image.jpg"
        #upload_file_icon = self.driver.find_element(By.XPATH, "//input[@type='file' and @name='main_img']")
        #upload_file_icon.send_keys(file_path)
        self.driver.find_element(*self.upload_file_icon).send_keys(file_path)
        return self
    def update_cashew_details_func(self):
        #update_cashew_details = self.driver.find_element(By.XPATH,"//button[@name='update' and contains(@class,'btn-danger')]")
        #update_cashew_details.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.update_cashew_details))
        self.driver.find_element(*self.update_cashew_details).click()
        return self
    def perform_scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        update_details=self.driver.find_element(*self.update_cashew_details)
        self.driver.execute_script("arguments[0].scrollIntoView();", update_details)