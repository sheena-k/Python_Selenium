import pytest
from selenium.webdriver.common.by import By
import constants.constant
from utilities.excel_utility import ExcelUtility
from pages.loginpage import LoginPage
from pages.managecategorypage import CategoryPage
class TestCategoryPage:
    @pytest.mark.smoke
    def test_category_page(self,browser_load):
        self.driver = browser_load
        obj_excel = ExcelUtility(constants.constant.FILE_PATH)
        username_value = obj_excel.get_string_data(2, 1, "login_data")
        password_value = obj_excel.get_string_data(2, 2, "login_data")
        loginpage_obj = LoginPage(self.driver)
        loginpage_obj.enter_username(username_value).enter_password(password_value).perform_login()
        managecategory_obj = CategoryPage(self.driver)
        managecategory_obj.manage_category_icon()
