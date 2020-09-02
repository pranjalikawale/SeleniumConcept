import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys
sys.path.append("C://Users/User/Desktop/python/DatePicker")
from utility.UI_operation import UIOperation
from utility.constant import Constant
from environment_setup.browser_instance import BrowserInstance
from utility.set_calendar_date import SetCalendarDate

@pytest.mark.usefixtures("initialize_driver")
class TestForJQueryCalendarDatesFromMultipleMonth():

    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
        self.driver=initialize_driver
        self.constant=Constant()
        self.driver.get(self.constant.BASE_URL_FOR_JQUERY_CALENDAR_DATES_FROM_MULTIPLE_MONTH)
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_FOR_JQUERY_CALENDAR_DATES_FROM_MULTIPLE_MONTH)
        self.set_calendar_date=SetCalendarDate(self.ui_action)

    def test_jquery_calendar_dates_from_multiple_month(self):
        datepicker_val = self.ui_action.get_locator("date_picker")
        datepicker_val.click()
        # Check the selected month, date, and year from the Calendar
        self.set_calendar_date.set_date()
        elem_date = self.driver.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='" + self.constant.target_date + "']")
        elem_date.click()
        time.sleep(10)
        selected_month_year_val = datepicker_val.get_attribute('value')
        assert selected_month_year_val==self.constant.expected_month_year_val
        
       