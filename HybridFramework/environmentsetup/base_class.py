from selenium import webdriver
from environmentsetup.browser_instance import BrowserInstance

class BaseClass():
    
    @staticmethod
    def initialize(browser):
        global driver
        driver=BrowserInstance(browser).get_browser_instance()
        return driver
        
    @staticmethod
    def close_driver():
        driver.close()
        return driver
        
