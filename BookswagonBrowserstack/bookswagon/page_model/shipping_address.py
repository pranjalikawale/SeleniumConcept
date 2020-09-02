from utility.UI_operation import UIOperation
from utility.constant import Constant
from utility.xls_util import XlsUtility
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import re

class ShippingAddressPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_SHIPPING_ADDRESS)
    
    def shipping_address(self,path,sheet):
        data=[]
        data=XlsUtility.read_data_from_sheet(path,sheet)
        self.ui_action.get_locator("button_continue_class").click()
        time.sleep(5)
        self.ui_action.get_locator("textbox_recipient_name_id").send_keys(data[0])
        self.ui_action.get_locator("textbox_company_name_id").send_keys(data[1])
        self.ui_action.get_locator("textbox_address_id").send_keys(data[2])
        country=Select(self.ui_action.get_locator("select_country_id"))
        #select by visible text
        country.select_by_visible_text(data[3])
        state=Select(self.ui_action.get_locator("select_state_id"))
        #select by visible text
        state.select_by_visible_text(data[4])
        self.ui_action.get_locator("textbox_city_id").send_keys(data[5])
        self.ui_action.get_locator("textbox_pincode_id").send_keys(data[6])
        self.ui_action.get_locator("textbox_mobile_id").send_keys(data[7])
        if "YES"==data[8].strip().upper():
            self.ui_action.get_locator("checkbox_default_id").click()
        self.ui_action.get_locator("button_save_id").click()
        time.sleep(5)
        return self.validation()

    def validation(self):
        if self.driver.current_url =="https://www.bookswagon.com/viewshoppingcart.aspx":
            order_status=self.ui_action.get_locator("verfiy_shipping_address_id").text
            return order_status
        error=self.ui_action.get_locator("text_error_message_id").text
        return error

    def previous_address(self,pincode):
        self.ui_action.get_locator("button_continue_class").click()
        time.sleep(5)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_cpBody_plnCustomerAdd > div > div.checkout-bg > div.returning > div.prv-address")))
            address_webelement=[]
            address_webelement=self.driver.find_elements_by_css_selector("#ctl00_cpBody_plnCustomerAdd > div > div.checkout-bg > div.returning > div.prv-address")
            counter=0 
            for address in address_webelement:
                result = re.findall('\\b'+pincode+'\\b', address.text)
                if len(result)>0:
                    element=self.driver.find_element_by_xpath("//*[@id='ctl00_cpBody_lvCustomerAdd_ctrl"+str(counter)+"_imgUseAddress']")
                    element.click()
                    break
                counter=counter+1
            return self.validation()
        except NoSuchElementException:
            return True
          
            
        