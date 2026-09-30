#1)
#login
#click manage cod, #select no for radio button and save # again select yes radiobutton 7 save
#2) #click home , #admin icon(right side)# click logout
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants.constant
from utilities.excel_utility import ExcelUtility
from pages.loginpage import LoginPage
from pages.managecod import ManageCod
import pytest
class TestManageCod:
    @pytest.mark.order(7)
    def test_manage_add_cod(self,browser_load):
        self.driver = browser_load
        obj_excel = ExcelUtility(constants.constant.FILE_PATH)
        username_value = obj_excel.get_string_data(2,1,"login_data")
        password_value = obj_excel.get_string_data(2,2,"login_data")
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
        #manage_cod_icon = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/add-cod' and @class='small-box-footer']")
        #manage_cod_icon.click()
        managecod_obj = ManageCod(self.driver)
        managecod_obj.cod_icon_click().button_cod_no_icon().cod_save_icon().button_cod_yes_icon().cod_save_icon()

        #button_cod_no_click= self.driver.find_element(By.XPATH,"//input[@value='no' and @type='radio' and @name='cod']")
        #button_cod_no_click.click()
        #managecod_obj.button_cod_no_icon()
        #print(button_cod_no_click.is_selected())
        #cod_save = self.driver.find_element(By.XPATH,"//button[contains(text(),'Save') and @name='create']")
        #cod_save.click()
        #managecod_obj.cod_save_icon()
        #button_cod_yes_click = self.driver.find_element(By.XPATH,"//input[@value='yes' and @type='radio' and @name='cod']")
        #button_cod_yes_click.click()
        #managecod_obj.button_cod_yes_icon()
        #cod_save = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save') and @name='create']")
        #cod_save.click()
        #managecod_obj.cod_save_icon()
        actual_url = self.driver.current_url
        assert actual_url =="https://groceryapp.uniqassosiates.com/admin/Cod/index"

