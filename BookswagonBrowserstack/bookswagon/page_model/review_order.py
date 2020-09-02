from utility.UI_operation import UIOperation
from utility.constant import Constant
import time

class ReviewOrderPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_REVIEW_ORDER)
    
    def review_order(self,instruction):
        time.sleep(2)
        self.ui_action.get_locator("textarea_Instruction_id").send_keys(instruction)
        self.ui_action.get_locator("button_save_id").click()
        time.sleep(5)
        order_status=self.ui_action.get_locator("text_payment_mode_xpath").text
        return order_status
        