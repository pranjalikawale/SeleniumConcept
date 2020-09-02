import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from utility.UI_operation import UIOperation
from utility.constant import Constant

class SetCalendarDate():  

    def __init__(self,ui_object):
        self.constant=Constant()
        self.ui_action=ui_object

    def set_date(self):    
        target_month_year_string = self.constant.target_month + self.constant.space + self.constant.target_year
 
        elem_selected_year = self.ui_action.get_locator("date_picker_year")
        selected_year_string = elem_selected_year.get_attribute("innerHTML")
 
        elem_selected_month = self.ui_action.get_locator("date_picker_month")
        selected_month_string = elem_selected_month.get_attribute("innerHTML")
 
        # Concatenate selected month and year strings
        selected_month_year_string = selected_month_string + selected_year_string
        
        # Navigate through the calendar to go to the required year
        # and than the required month
       
        while (selected_month_year_string != target_month_year_string):
            if (((int(self.constant.target_year)) < int(selected_year_string))):
                next_button=self.ui_action.get_locator("next_button_xpath")
                next_button.click()
            else: 
                previous_button=self.ui_action.get_locator("previous_button_xpath")   
                previous_button.click()
            time.sleep(10)
 
            elem_selected_year = self.ui_action.get_locator("date_picker_year")
            selected_year_string = elem_selected_year.get_attribute("innerHTML")
 
            elem_selected_month = self.ui_action.get_locator("date_picker_month")
            selected_month_string = elem_selected_month.get_attribute("innerHTML")
 
            # Compute the final day-month-year string
            selected_month_year_string = selected_month_string + self.constant.space + selected_year_string
               
    def set_from_date(self):
        #Steps for the From Date 
        from_dp = self.ui_action.get_locator("from_date_xpath")
        from_dp.click()
        time.sleep(5)
        from_month = self.ui_action.get_locator("from_month_xpath")
        selected_from_month = Select(from_month)
        selected_from_month.select_by_visible_text("Jan")
        time.sleep(5)
        return from_dp
        
    def set_to_date(self):
        #Steps for the to Date 
        to_dp = self.ui_action.get_locator("to_date_xpath")
        to_dp.click()
        time.sleep(5)
        to_month = self.ui_action.get_locator("to_month_xpath")
        selected_to_month=Select(to_month)
        selected_to_month.select_by_visible_text("Jan")
        time.sleep(5)
        return to_dp