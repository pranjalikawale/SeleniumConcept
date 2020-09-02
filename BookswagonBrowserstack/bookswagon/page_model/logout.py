from utility.UI_operation import UIOperation
from utility.constant import Constant

class LogoutPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_lOGOUT)

    def logout(self):
        self.ui_action.get_locator("link_logout_id").click()
        logout_status=self.ui_action.get_locator("text_verify_logout_xpath").text
        return logout_status