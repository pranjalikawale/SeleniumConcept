import pytest
import time
import sys
sys.path.append("C://Users/User/Desktop/python/AlertAndPopup")
from utility.UI_operation import UIOperation
from utility.constant import Constant
from environment_setup.browser_instance import BrowserInstance
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("initialize_driver")
class TestJSAlertCheck():
    
    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
        self.driver=initialize_driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE)
    
    def test_jsalert(self):
       #this searches for for the first alert button and clicks on that
        js_alert_button=self.ui_action.get_locator('js_alert_button')
        js_alert_button.click()
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
            #now we switch to alert
            popup = self.driver.switch_to.alert
            #use the accept() method to accept the alert
            popup.accept()
        except TimeoutException:
            print("no alert")
        time.sleep(5)
        #this gets the result text returned
        textreturned = self.ui_action.get_locator('result')        
        #we assert if the text returned is what we wanted
        assert textreturned.text=="You successfuly clicked an alert"

    def test_jsalert_confirm_click_on_ok(self):
        #get the second button by xpath and click on it
        js_alert_confirm_button = self.ui_action.get_locator("js_alert_confirm")
        js_alert_confirm_button.click()
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
            #switch to the alert
            jsalert= self.driver.switch_to.alert
            #accept the alert
            jsalert.accept()
        except TimeoutException:
            print("no alert")
        time.sleep(5)
        #this gets the result text returned
        textreturned = self.ui_action.get_locator('result')        
        #we assert if the text returned is what we wanted
        assert textreturned.text=="You clicked: Ok"
 
    def test_jsalert_confirm_click_on_cancel(self):
        #get the second button by xpath and click on it
        js_alert_confirm_button = self.ui_action.get_locator("js_alert_confirm")
        js_alert_confirm_button.click()
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
            #switch to the alert
            jsalert= self.driver.switch_to.alert
            #accept the alert
            jsalert.dismiss()
        except TimeoutException:
            print("no alert")
        time.sleep(5)
        #this gets the result text returned
        textreturned = self.ui_action.get_locator('result')        
        #we assert if the text returned is what we wanted
        assert textreturned.text=="You clicked: Cancel"

    def test_jsprompt_with_text(self):
        #get the third button by using it's xpath and click on it
        js_prompt_button = self.ui_action.get_locator("js_prompt_button")
        js_prompt_button.click()
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
            #switch to the alert
            jsprompt= self.driver.switch_to.alert
            #send custom text to the prompt using send_keys( ) method
            jsprompt.send_keys('xyz')
            #accept the alert
            jsprompt.accept()
        except TimeoutException:
            print("no alert")
        time.sleep(5)
        #this gets the result text returned
        textreturned = self.ui_action.get_locator('result')        
        #we assert if the text returned is what we wanted
        assert textreturned.text=="You entered: xyz"
 
    