from utility.UI_operation import UIOperation
from utility.constant import Constant
from utility.read_json import ReadJson
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_lOGIN)
        self.json_object=ReadJson()
    
    def login(self,path):
        data=self.json_object.read_json(path)
        for credential in data :
            self.ui_action.get_locator("link_login_xpath").click()
            email_textbox=self.ui_action.get_locator("textbox_email_id")
            email_textbox.clear()
            email_textbox.send_keys(credential['email'])
            password_textbox=self.ui_action.get_locator("textbox_password_id")
            password_textbox.clear()
            password_textbox.send_keys(credential['password'])
            self.ui_action.get_locator("button_login_id").click()
        myaccount=self.ui_action.get_locator("text_verify_myaccount_id").text
        return myaccount

    def login_for_multiple_invalid_data(self,path):
        data=self.json_object.read_json(path)
        for credential in data :
            self.ui_action.get_locator("link_login_xpath").click()
            email_textbox=self.ui_action.get_locator("textbox_email_id")
            email_textbox.clear()
            email_textbox.send_keys(credential['email'])
            password_textbox=self.ui_action.get_locator("textbox_password_id")
            password_textbox.clear()
            password_textbox.send_keys(credential['password'])
            self.ui_action.get_locator("button_login_id").click()
        time.sleep(5)
        error=self.ui_action.get_locator("text_error_message_xpath").text
        return error
            



    