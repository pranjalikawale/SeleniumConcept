import pytest
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys
sys.path.append("C://Users/User/Desktop/python/DatePicker")
from utility.UI_operation import UIOperation
from utility.constant import Constant
from environment_setup.browser_instance import BrowserInstance
from utility.set_calendar_date import SetCalendarDate

@pytest.mark.usefixtures("initialize_driver")
class TestForJQueryIframCalendar(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
        self.driver=initialize_driver
        self.constant=Constant()
        self.driver.get(self.constant.BASE_URL_FOR_JQUERY_IFRAM_CALENDAR)
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_FOR_JQUERY_IFRAM_CALENDAR)
        self.set_calendar_date=SetCalendarDate(self.ui_action)
        
    def test_jquery_with_ifram_calendar(self):
        frame = self.ui_action.get_locator("iframe_xpath")
        self.driver.switch_to.frame(frame)
        #from date
        from_dp=self.set_calendar_date.set_from_date()
        from_day = self.driver.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-month'))]/a[text()='" + self.constant.expected_fr_date + "']")
        from_day.click()
        #to date
        to_dp=self.set_calendar_date.set_to_date()   
        to_day = self.driver.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-month'))]/a[text()='" + self.constant.expected_to_date + "']")
        to_day.click()
        #Verify whether the values are as expected 
        selected_from_date_str = from_dp.get_attribute('value')
        selected_to_date_str = to_dp.get_attribute('value')
        assert selected_from_date_str == self.constant.expected_from_date_str and selected_to_date_str==self.constant.expected_to_date_str
       
        
 

    

    
