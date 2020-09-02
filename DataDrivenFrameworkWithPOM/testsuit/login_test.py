import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import json
import sys
sys.path.append("C://Users/User/Desktop/python/DataDrivenFrameworkWithPOM")
from pageobjects.login_page import LoginPage
from environmentsetup.baseclass import BaseClass
from datadriven.xls_util import XlsUtility

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver=BaseClass.initialize()

    def test_login_with_json(self):
        path="C://Users/User/Desktop/python/DataDrivenWithPOM/resource/credential.json"
        login=LoginPage(self.driver) 
        with open(path,"r") as json_file:
            data = json.load(json_file)
        i=0
        for credential in data['credentials']:
            username=credential['username']
            password=credential['password']
            login.set_username(username)   
            login.set_password(password)
            login.click_login()
            time.sleep(5)
            if self.driver.title=="Dashboard / nopCommerce administration":
                print("Test no {0} is Pass \n".format(i+1))
                login.click_logout()
            else:
                print("Test no {0} is Fail \n".format(i+1))
            self.driver.save_screenshot("C://Users/User/Desktop/python/DataDrivenFrameworkWithPOM/screenshot/xlxs_credential_verification.png")

    def test_login_with_xlsx(self):
        path="C://Users/User/Desktop/python/DataDrivenFrameworkWithPOM/resource/credential.xlsx"
        sheet_name="Sheet1"
        login=LoginPage(self.driver) 
        rows=XlsUtility.get_row_count(path,sheet_name)
        for row in range(2,rows+1):
            username=XlsUtility.read_data(path,sheet_name,row,1)
            password=XlsUtility.read_data(path,sheet_name,row,2)
            login.set_username(username)   
            login.set_password(password)
            login.click_login()
            time.sleep(5)
            if self.driver.title=="Dashboard / nopCommerce administration":
                print("Test no {0} is Pass \n".format(row-1))
                login.click_logout()
            else:
                print("Test no {0} is Fail \n".format(row-1))
            self.driver.save_screenshot("C://Users/User/Desktop/python/DataDrivenFrameworkWithPOM/screenshot/json_credential_verification.png")
        
            
    @classmethod
    def tearDownClass(cls):
        cls.driver=BaseClass.close_driver()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\User\Desktop\python\DataDrivenFrameworkWithPOM\Report'))

