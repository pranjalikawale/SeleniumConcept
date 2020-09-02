import pytest
import unittest
from allure_commons.types import AttachmentType
import allure
import inspect
import time
from selenium import webdriver
import sys
sys.path.append("C://Users/User/Desktop/python/AllureReportGeneration")
from utility.UI_operation import UIOperation
from utility.constant import Constant
from environment_setup.browser_instance import BrowserInstance
from utility.xls_util import XlsUtility
from utility.xlxs_data_reader import XlxsDataReader
from object_repository.read_object import ReadObject

@pytest.mark.usefixtures("initialize_driver")
@allure.severity(allure.severity_level.NORMAL)
class TestForDemoNonCommerce():

    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
        self.driver=initialize_driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver)
        self.xlxs_datareader=XlxsDataReader()
        self.property=ReadObject(self.constant)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_xlsx(self):
        rows=XlsUtility.get_row_count(self.constant.PATH_TESTDATA,self.constant.TEST_SHEET_NAME)
        sheet=XlsUtility.get_sheet_object(self.constant.PATH_TESTDATA,self.constant.TEST_SHEET_NAME)
        for row in range(3,rows):
            keyword,object_name,locator_type,value=self.xlxs_datareader.get_xlxs_data(sheet,row)
            locator=self.property.get_property(object_name)
            self.ui_action.perform_action(keyword,locator,locator_type,value)
            time.sleep(5)    
        time.sleep(5) 
        destination=self.constant.PATH_SCREENSHOOT+str(inspect.currentframe().f_code.co_name)+"_"+str(round(time.time()*10))+".png"
        allure.attach(self.driver.get_screenshot_as_png(),name=destination,attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Dashboard / nopCommerce administration"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_feature(self):
        rows=XlsUtility.get_row_count(self.constant.PATH_TESTDATA,self.constant.TEST_SHEET_NAME)
        sheet=XlsUtility.get_sheet_object(self.constant.PATH_TESTDATA,self.constant.TEST_SHEET_NAME)
        for row in range(3,rows+1):
            keyword,object_name,locator_type,value=self.xlxs_datareader.get_xlxs_data(sheet,row)
            locator=self.property.get_property(object_name)
            self.ui_action.perform_action(keyword,locator,locator_type,value)
            time.sleep(5)    
        #self.driver.save_screenshot(destination)
        time.sleep(5) 
        assert self.driver.title == "Your store. Login"

