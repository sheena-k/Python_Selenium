from selenium.webdriver.common.by import By
import constants.constant
from utilities.excel_utility import ExcelUtility
from pages.loginpage import LoginPage
from pages.managelistpages import ManagePage
import pytest
class TestManagePage:
    @pytest.mark.order(8)
    def test_List_Pages(self,browser_load):
        self.driver = browser_load
        obj_excel=ExcelUtility(constants.constant.FILE_PATH)
        username_value = obj_excel.get_string_data(2, 1, "login_data")
        password_value = obj_excel.get_string_data(2, 2, "login_data")
        #login_username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        #login_username.send_keys(username_value)
        #login_password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        #login_password.send_keys(password_value)
        #login_signin = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        #login_signin.click()
        loginpage_obj = LoginPage(self.driver)
        loginpage_obj.enter_username(username_value).enter_password(password_value).perform_login()
        #loginpage_obj.enter_password(password_value)
        #loginpage_obj.perform_login()
        #manage_page_icon = self.driver.find_element(By.XPATH,"//a[ contains(@href,'admin/list-page') and @class='small-box-footer']")
        #manage_page_icon.click()
        manage_page_obj = ManagePage(self.driver)
        manage_page_obj.manage_page_icon_func().cashew_edit_icon_func().cashew_description_func().cashew_uploadfile_func().perform_scroll().update_cashew_details_func()
        #cashew_edit_icon = self.driver.find_element(By.XPATH,"//a[@class='btn btn-sm btn btn-primary btncss' and (@href='https://groceryapp.uniqassosiates.com/admin/pages/edit?edit=48&page_ad=1')]")
        #cashew_edit_icon.click()
        #manage_page_obj.cashew_edit_icon_func()
        #cashew_description = self.driver.find_element(By.XPATH,"//div[@class='note-editable card-block']")
        #cashew_description.send_keys("cashew edible nut")
        #manage_page_obj.cashew_description_func()
        #file_path = r"C:\Users\hp\OneDrive\Desktop\cashews_image.jpg"
        #upload_file_icon = self.driver.find_element(By.XPATH,"//input[@type='file' and @name='main_img']")
        #upload_file_icon.send_keys(file_path)
        #manage_page_obj.cashew_uploadfile_func()
        #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #update_cashew_details= self.driver.find_element(By.XPATH,"//button[@name='update' and contains(@class,'btn-danger')]")
        #self.driver.execute_script("arguments[0].scrollIntoView();",update_cashew_details)
        #manage_page_obj.perform_scroll()
        #update_cashew_details.click()
        #manage_page_obj.update_cashew_details_func()
        actual_url = self.driver.current_url
        assert actual_url == "https://groceryapp.uniqassosiates.com/admin/list-page?page_ad=1"

