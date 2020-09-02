from selenium import webdriver
import os
from utility.constant import Constant

class BrowserInstance():

    ### Browser value is retrieved from request variable in conftest
    def __init__(self,browser):
        self.browser = browser
        self.constant = Constant()

    # Method to invoke browser based on the input from the command prompt
    def get_browser_instance(self):
        #invoke IE browser 
        if (self.browser == 'IE'):
            driver_location = self.constant.PATH_IE_DRIVER
            #os.environ["webdriver.IE.driver"] = driver_location
            driver = webdriver.Ie(driver_location)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()
        #invoke Chrome browser 
        elif (self.browser == 'Chrome'):
            driverLocation = self.constant.PATH_CHROME_DRIVER
            #os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()
        #invoke Firefox browser 
        else:
            #driverLocation = self.constants.Path_Firefox_driver
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()
        return driver
