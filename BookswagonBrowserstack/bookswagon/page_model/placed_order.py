from utility.UI_operation import UIOperation
from utility.constant import Constant
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PlacedOrderPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_PLACED_ORDER)
    
    def placing_order(self,quantity):
        self.ui_action.get_locator("button_buy_now_xpath").click()
        self.driver.switch_to.frame(self.ui_action.get_locator("iframe_xpath"))
        quanity_element=self.ui_action.get_locator("textbox_quantity_id")
        quanity_element.clear()
        quanity_element.send_keys(quantity)
        self.ui_action.get_locator("button_placed_order_id").click()
        time.sleep(5)
        if quantity<=0:
            error=self.ui_action.get_locator("text_error_message_id").text
            return error
        self.driver.switch_to.default_content()
        order_status=self.ui_action.get_locator("text_verify_order_status_xpath").text
        return order_status



