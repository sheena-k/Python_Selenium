import pytest
from selenium.webdriver.common.by import By

import constants.constant
from utilities.excel_utility import ExcelUtility
from pages.loginpage import LoginPage
#from pages.homepage import HomePage
class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.order(1)
    @pytest.mark.describe("valid login test cases")
    def test_valid_login(self,browser_load):
        self.driver=browser_load
        obj_excel= ExcelUtility(constants.constant.FILE_PATH)
        username_value = obj_excel.get_string_data(2,1,"login_data")
        password_value = obj_excel.get_string_data(2,2,"login_data")

        loginpage_obj = LoginPage(self.driver)
        loginpage_obj.enter_username(username_value).enter_password(password_value).perform_login() #chaining of methods and classes
        #loginpage_obj.enter_password(password_value)
        #loginpage_obj.perform_login()


        #login_username = self.driver.find_element(By.XPATH,"//input[@placeholder='Username']")
        #login_username = send_keys("admin") # replace this hardcode with data driven inputs as below
        #login_username.send_keys(username_value)
        #login_password = self.driver.find_element(By.XPATH,"//input[@placeholder='Password']")
        #login_password.send_keys(password_value)
        #login_signin = self.driver.find_element(By.XPATH,"//button[text()='Sign In']")
        #login_signin.click()
        actual_url =self.driver.current_url
        assert actual_url =="https://groceryapp.uniqassosiates.com/admin"
    @pytest.mark.smoke
    @pytest.mark.order(2)
    @pytest.mark.describe("invalid login test cases")
    @pytest.mark.parametrize("username,password",[("invaliduser","admin"),("admin","invalidpassword"),("invaliduser","invalidpassword"),(" "," ")])
    def test_invalid_login(self,browser_load,username,password):
        self.driver = browser_load
        #login_username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        #login_username.send_keys(username)
        #login_password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        #login_password.send_keys(password)
        #login_signin = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        #login_signin.click()
        loginpage_obj = LoginPage(self.driver)
        loginpage_obj.enter_username(username).enter_password(password).perform_login()
        #loginpage_obj.enter_username(username)
        #loginpage_obj.enter_password(password)
        #loginpage_obj.perform_login()
        actual_url =self.driver.current_url
        assert actual_url == "https://groceryapp.uniqassosiates.com/admin/login"
    @pytest.mark.smoke
    @pytest.mark.order(3)
    @pytest.mark.describe("admin logout test cases")
    def test_admin_logout(self,browser_load):
        self.driver = browser_load
        obj_excel = ExcelUtility("C:\\Users\\hp\\PycharmProjects\\PythonSeleniumPytest\\test_data\\data_login.xlsx")
        username_value = obj_excel.get_string_data(2,1,"login_data")
        password_value = obj_excel.get_string_data(2,2,"login_data")
        #login_username.send_keys(username_value)
        #login_password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        #login_password.send_keys(password_value)
        #login_signin = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        #login_signin.click()
        loginpage_obj = LoginPage(self.driver)
        loginpage_obj.enter_username(username_value).enter_password(password_value).perform_login().home_icon_func().admin_icon_func().logout_icon_func()
       # loginpage_obj.enter_password(password_value)
        #loginpage_obj.perform_login()
        #home_icon = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/home' and contains(text(),'Home')]")
        #home_icon.click()
        #loginpage_obj.home_icon_func()
        #admin_icon = self.driver.find_element(By.XPATH,"//a[@class='nav-link' and @data-toggle='dropdown']")
        #admin_icon.click()
        #loginpage_obj.admin_icon_func()
        #logout_icon = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/logout' and @class='dropdown-item']")
        #logout_icon.click()
        #loginpage_obj.logout_icon_func()
        actual_url = self.driver.current_url
        assert actual_url == "https://groceryapp.uniqassosiates.com/admin/login"


