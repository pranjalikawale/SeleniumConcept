import pytest
import time
import sys
sys.path.append("C://Users/User/Desktop/python/Tooltip")
from utility.UI_operation import UIOperation
from utility.constant import Constant
from environment_setup.browser_instance import BrowserInstance
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("initialize_driver")
class TestTooltip():
    
    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
        self.driver=initialize_driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE)

    def test_tool_tip(self):
        try:
            frame=self.ui_action.get_locator("iframe")
            self.driver.switch_to.frame(frame)
            time.sleep(5)
            tooltip_input=self.ui_action.get_locator("textbox_age")
            time.sleep(5)
            ActionChains(self.driver).move_to_element(tooltip_input).perform()
            time.sleep(5)
            tooltip_message=self.ui_action.get_locator("txt_input_tooltip")
            assert "We ask for your age only for statistical purposes."==tooltip_message.text
        except TimeoutException:
            print("Take too much time to load")

    def test_tooltip(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((self.ui_action.get_locator("iframe"))))
            tooltip_input =self.ui_action.get_locator("textbox_age")
            time.sleep(5)
            ActionChains(self.driver).move_to_element(tooltip_input).perform()
            time.sleep(5)
            tooltip_message = self.ui_action.get_locator("txt_input_tooltip")
            assert "We ask for your age only for statistical purposes."== tooltip_message.text
        except TimeoutException:
            print("Take too much time to load")
    
