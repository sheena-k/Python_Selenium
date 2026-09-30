import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import constants.constant
from utilities.excel_utility import ExcelUtility
from pages.loginpage import LoginPage
from pages.deliveryboypage import DeliveryBoyPage
#1) #valid login #manage deliveryboy icon #new data enter, save
class TestDeliveryBoy:
    @pytest.mark.smoke
    @pytest.mark.order(4)
    @pytest.mark.describe("new delivery boy details test cases")
    def test_new_data_save(self,browser_load):
        self.driver = browser_load
        obj_excel=ExcelUtility(constants.constant.FILE_PATH)
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
        name_new_value = obj_excel.get_string_data(3, 3, "login_data")
        email_new_value = obj_excel.get_string_data(3, 4, "login_data")
        phone_number_new_value = obj_excel.get_string_data(3, 5, "login_data")
        address_new_value = obj_excel.get_string_data(3, 6, "login_data")
        username_new_value = obj_excel.get_string_data(3, 1, "login_data")
        password_new_value = obj_excel.get_string_data(3, 2, "login_data")

        #manage_delivery_boy_icon = self.driver.find_element(By.XPATH,"//a[contains(@href,'list-deliveryboy') and contains(@class,'nav-link')]")
        #manage_delivery_boy_icon.click()
        deliveryboy_obj = DeliveryBoyPage(self.driver)
        deliveryboy_obj.delivery_boy_icon().delivery_boy_new().delivery_boy_newname(name_new_value).delivery_boy_newemail(email_new_value).delivery_boy_newphonenumber(phone_number_new_value).delivery_boy_addressnew(address_new_value).delivery_boy_usernamenew(username_new_value).perform_scroll_deliveryboypage().delivery_boy_passwordnew(password_new_value).delivery_boy_savenew()

        #delivery_boy_new_add = self.driver.find_element(By.XPATH,"//a[contains(@href,'Deliveryboy/add') and contains(@class,'btn btn-rounded btn-danger')]")
        #delivery_boy_new_add.click()
        #deliveryboy_obj.delivery_boy_new()
        #name_new = self.driver.find_element(By.XPATH,"//input[@placeholder='Enter the Name']")

        #name_new.send_keys(name_new_value)
        #deliveryboy_obj.delivery_boy_newname(name_new_value)
        #email_new = self.driver.find_element(By.XPATH,"//input[@placeholder='Enter the Email']")

        #email_new.send_keys(email_new_value)
        #deliveryboy_obj.delivery_boy_newemail(email_new_value)
        #phone_number_new = self.driver.find_element(By.XPATH,"//input[@placeholder='Enter the Phone Number']")

        #phone_number_new.send_keys(phone_number_new_value)
        #deliveryboy_obj.delivery_boy_newphonenumber(phone_number_new_value)
        #address_new = self.driver.find_element(By.XPATH,"//textarea[@placeholder='Enter the Address']")

        #address_new.send_keys(address_new_value)
        #deliveryboy_obj.delivery_boy_addressnew(address_new_value)
        #username_new= self.driver.find_element(By.XPATH,"//input[@placeholder='Enter the Username']")

        #username_new.send_keys(username_new_value)
        #deliveryboy_obj.delivery_boy_usernamenew(username_new_value)

        #password_new = self.driver.find_element(By.XPATH,"//input[@placeholder='Enter the Password']")




        #password_new.send_keys(password_new_value)
        #deliveryboy_obj.delivery_boy_passwordnew(password_new_value)
        #self.driver.execute_script("arguments[0].scrollIntoView();", password_new)
        #save_new = self.driver.find_element(By.XPATH,"//button[contains(text(),'Save') and contains(@class,'btn btn-danger')]")
        #save_new.click()
        #deliveryboy_obj.delivery_boy_savenew()
        actual_url = self.driver.current_url
        assert actual_url == "https://groceryapp.uniqassosiates.com/admin/Deliveryboy/add"

#2)#valid login #manage deliveryboy icon #search the user
    @pytest.mark.order(5)
    @pytest.mark.describe("user search test cases")
    def test_search_user(self,browser_load):
        self.driver = browser_load
        obj_excel = ExcelUtility(r"C:\Users\hp\OneDrive\Desktop\data_login.xlsx")
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
        name_new_value = obj_excel.get_string_data(3, 3, "login_data")
        email_new_value = obj_excel.get_string_data(3, 4, "login_data")
        phone_number_new_value = obj_excel.get_string_data(3, 5, "login_data")
        #manage_delivery_boy_icon = self.driver.find_element(By.XPATH,"//a[contains(@href,'list-deliveryboy') and contains(@class,'nav-link')]")
        #manage_delivery_boy_icon.click()
        deliveryboy_obj = DeliveryBoyPage(self.driver)
        deliveryboy_obj.delivery_boy_icon().delivery_boy_search_new_icon().delivery_boy_name_search(name_new_value).delivery_boy_email_search(email_new_value).delivery_boy_phone_number_search(phone_number_new_value).delivery_boy_search_button()
        #search_new_icon = self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        #search_new_icon.click()
        #deliveryboy_obj.delivery_boy_search_new_icon()
        #name_search = self.driver.find_element(By.XPATH,"//input[@name='un' and @placeholder='Name']")

        #name_search.send_keys(name_new_value)
        #deliveryboy_obj.delivery_boy_name_search(name_new_value)
        #email_search = self.driver.find_element(By.XPATH,"//input[@name='ut' and @placeholder='Email']")

        #email_search.send_keys(email_new_value)
        #deliveryboy_obj.delivery_boy_email_search(email_new_value)
        #phone_search = self.driver.find_element(By.XPATH,"//input[@name='ph' and @placeholder='Phone Number']")

        #phone_search.send_keys(phone_number_new_value)
        #deliveryboy_obj.delivery_boy_phone_number_search(phone_number_new_value)
        #search_button = self.driver.find_element(By.XPATH,"//button[@class='btn btn-block-sm btn-danger' and @name='Search']")
        #search_button.click()
        #deliveryboy_obj.delivery_boy_search_button()
        actual_url = self.driver.current_url
        assert actual_url == "https://groceryapp.uniqassosiates.com/admin/Deliveryboy/index?un=Anu&ut=anu123%40gmail.com&ph=9876543210&Search=sr"

#3)#validlogin #mange delivery boy icon #home
    @pytest.mark.order(6)
    @pytest.mark.describe("delivery boy page icon and home icon test cases")
    def test_manage_delivery_boy_home(self,browser_load):
        self.driver = browser_load
        obj_excel = ExcelUtility(r"C:\Users\hp\OneDrive\Desktop\data_login.xlsx")
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
        #manage_delivery_boy_icon = self.driver.find_element(By.XPATH,"//a[contains(@href,'list-deliveryboy') and contains(@class,'nav-link')]")
        #manage_delivery_boy_icon.click()
        deliveryboy_obj = DeliveryBoyPage(self.driver)
        deliveryboy_obj.delivery_boy_icon().manage_home_icon()
        #manage_home = self.driver.find_element(By.XPATH,"//a[contains(@href,'admin/home') and contains(text(),'Home')]")
        #manage_home.click()
        #deliveryboy_obj.manage_home_icon()
        actual_url = self.driver.current_url
        assert actual_url == "https://groceryapp.uniqassosiates.com/admin/home"