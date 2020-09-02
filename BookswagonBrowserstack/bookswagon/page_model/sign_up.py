from utility.UI_operation import UIOperation
from utility.constant import Constant

class SignUpPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE)

    def set_username(self,email,locator_object):
        email_textbox=self.ui_action(locator_object)
        email_textbox.clear()
        email_textbox.send_keys(email)

    def set_password(self,password,locator_object):
        password_textbox=self.ui_action(locator_object)
        password_textbox.clear()
        password_textbox.send_keys(password)
    
    def set_confirm_password(self,confirm_password,locator_object):
        confirm_password_textbox=self.ui_action(locator_object)
        confirm_password_textbox.clear()
        confirm_password_textbox.send_keys(confirm_password)

    def checked_subscribe(self,locator_object):
        subscribe_checked=self.ui_action(locator_object)
        if(not subscribe_checked.is_selected()):
            subscribe_checked.click()

    def unchecked_subscribe(self,locator_object):
        subscribe_unchecked=self.ui_action(locator_object)
        if(subscribe_unchecked.is_selected()):
            subscribe_unchecked.click()

    def click_create_account(self,locator_object):
        self.ui_action(locator_object).click()