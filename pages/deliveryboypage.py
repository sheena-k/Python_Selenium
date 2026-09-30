from selenium.webdriver.common.by import By
from utilities.wait_utility import WaitUtility
class DeliveryBoyPage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.manage_delivery_boy_icon = (By.XPATH,"//a[contains(@href,'list-deliveryboy') and contains(@class,'nav-link')]")
        self.delivery_boy_new_add =(By.XPATH,"//a[contains(@href,'Deliveryboy/add') and contains(@class,'btn btn-rounded btn-danger')]")
        self.name_new = (By.XPATH, "//input[@placeholder='Enter the Name']")
        self.email_new = (By.XPATH, "//input[@placeholder='Enter the Email']")
        self.phone_number_new = (By.XPATH, "//input[@placeholder='Enter the Phone Number']")
        self.address_new = (By.XPATH, "//textarea[@placeholder='Enter the Address']")
        self.username_new = (By.XPATH, "//input[@placeholder='Enter the Username']")
        self.password_new = (By.XPATH, "//input[@placeholder='Enter the Password']")
        self.save_new = (By.XPATH,"//button[contains(text(),'Save') and contains(@class,'btn btn-danger')]")
        self.search_new_icon = (By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        self.name_search = (By.XPATH, "//input[@name='un' and @placeholder='Name']")
        self.email_search = (By.XPATH, "//input[@name='ut' and @placeholder='Email']")
        self.phone_search = (By.XPATH, "//input[@name='ph' and @placeholder='Phone Number']")
        self.search_button = (By.XPATH, "//button[@class='btn btn-block-sm btn-danger' and @name='Search']")
        self.manage_home = (By.XPATH,"//a[contains(@href,'admin/home') and contains(text(),'Home')]")
    def delivery_boy_icon(self):
        #manage_delivery_boy_icon = self.driver.find_element(By.XPATH,"//a[contains(@href,'list-deliveryboy') and contains(@class,'nav-link')]")
        #manage_delivery_boy_icon.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.manage_delivery_boy_icon))
        self.driver.find_element(*self.manage_delivery_boy_icon).click()
        return self
    def delivery_boy_new(self):
        #delivery_boy_new = self.driver.find_element(By.XPATH,"//a[contains(@href,'Deliveryboy/add') and contains(@class,'btn btn-rounded btn-danger')]")
        #delivery_boy_new.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.delivery_boy_new_add))
        self.driver.find_element(*self.delivery_boy_new_add).click()
        return self
    def delivery_boy_newname(self,name_new_value):
        #name_new = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter the Name']")
        #name_new.send_keys(name_new_value)
        self.driver.find_element(*self.name_new).send_keys(name_new_value)
        return self
    def delivery_boy_newemail(self,email_new_value):
        #email_new = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter the Email']")
        #email_new.send_keys(email_new_value)
        self.driver.find_element(*self.email_new).send_keys(email_new_value)
        return self
    def delivery_boy_newphonenumber(self,phone_number_new_value):
        #phone_number_new = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter the Phone Number']")
        #phone_number_new.send_keys(phone_number_new_value)
        self.driver.find_element(*self.phone_number_new).send_keys(phone_number_new_value)
        return self
    def delivery_boy_addressnew(self,address_new_value):
        #address_new = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Enter the Address']")
        #address_new.send_keys(address_new_value)
        self.driver.find_element(*self.address_new).send_keys(address_new_value)
        return self
    def delivery_boy_usernamenew(self,username_new_value):
        #username_new = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter the Username']")
        #username_new.send_keys(username_new_value)
        self.driver.find_element(*self.username_new).send_keys(username_new_value)
        return self
    def delivery_boy_passwordnew(self,password_new_value):
        #password_new = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter the Password']")
        #password_new.send_keys(password_new_value)
        self.driver.find_element(*self.password_new).send_keys(password_new_value)
        return self
    def delivery_boy_savenew(self):
        #save_new = self.driver.find_element(By.XPATH,"//button[contains(text(),'Save') and contains(@class,'btn btn-danger')]")
        #save_new.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.save_new))
        self.driver.find_element(*self.save_new).click()
        return self
    def delivery_boy_search_new_icon(self):
        #search_new_icon = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        #search_new_icon.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.search_new_icon))
        self.driver.find_element(*self.search_new_icon).click()
        return self
    def delivery_boy_name_search(self,name_new_value):
        #name_search = self.driver.find_element(By.XPATH, "//input[@name='un' and @placeholder='Name']")
        #name_search.send_keys(name_new_value)
        self.driver.find_element(*self.name_search).send_keys(name_new_value)
        return self
    def delivery_boy_email_search(self,email_new_value):
        #email_search = self.driver.find_element(By.XPATH, "//input[@name='ut' and @placeholder='Email']")
        #email_search.send_keys(email_new_value)
        self.driver.find_element(*self.email_search).send_keys(email_new_value)
        return self
    def delivery_boy_phone_number_search(self,phone_number_new_value):
        #phone_search = self.driver.find_element(By.XPATH, "//input[@name='ph' and @placeholder='Phone Number']")
        #phone_search.send_keys(phone_number_new_value)
        self.driver.find_element(*self.phone_search).send_keys(phone_number_new_value)
        return self
    def delivery_boy_search_button(self):
        #search_button = self.driver.find_element(By.XPATH,"//button[@class='btn btn-block-sm btn-danger' and @name='Search']")
        #search_button.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.search_button))
        self.driver.find_element(*self.search_button).click()
        return self
    def manage_home_icon(self):
        #manage_home = self.driver.find_element(By.XPATH,"//a[contains(@href,'admin/home') and contains(text(),'Home')]")
        #manage_home.click()
        self.waitutility.wait_until_clickable(self.driver, self.driver.find_element(*self.manage_home))
        self.driver.find_element(*self.manage_home).click()
        return self
    def perform_scroll_deliveryboypage(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        return self