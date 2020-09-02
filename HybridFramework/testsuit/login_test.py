import unittest
import HtmlTestRunner
import inspect
from selenium import webdriver
import time
import sys
import pytest
sys.path.append("C://Users/User/Desktop/python/HybridFramework")
from utility.UI_operation import UIOperation
from utility.constant import Constant
from environmentsetup.base_class import BaseClass
from utility.xls_util import XlsUtility
from utility.xlxs_data_reader import XlxsDataReader
from objectrepository.read_object import ReadObject

class LoginTest(unittest.TestCase):
    browser =""

    @classmethod
    def setUpClass(cls):
        cls.driver=BaseClass.initialize(cls.browser)
        cls.constant=Constant()
        cls.ui_action=UIOperation(cls.driver)
        cls.xlxs_datareader=XlxsDataReader()
        cls.property=ReadObject(cls.constant)

    def test_login_with_xlsx(self):
        rows=XlsUtility.get_row_count(self.constant.PATH_TESTDATA,self.constant.TEST_SHEET_NAME)
        sheet=XlsUtility.get_sheet_object(self.constant.PATH_TESTDATA,self.constant.TEST_SHEET_NAME)
        for row in range(3,rows+1):
            keyword,object_name,locator_type,value=self.xlxs_datareader.get_xlxs_data(sheet,row)
            locator=self.property.get_property(object_name)
            self.ui_action.perform_action(keyword,locator,locator_type,value)
            time.sleep(5)    
        destination=self.constant.PATH_SCREENSHOOT+str(inspect.currentframe().f_code.co_name)+"_"+str(round(time.time()*10))+".png"
        self.driver.save_screenshot(destination)
        time.sleep(5) 
        assert self.driver.title == "Your store. Login"

    @classmethod
    def tearDownClass(cls):
        cls.driver=BaseClass.close_driver()

if __name__=='__main__':
    LoginTest.browser = sys.argv.pop()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\User\Desktop\python\HybridFramework\report'))

