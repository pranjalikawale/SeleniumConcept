from selenium import webdriver
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
            driver = webdriver.Ie(driver_location)
        #invoke Chrome browser 
        elif (self.browser == 'Chrome'):
            driver_location = self.constant.PATH_CHROME_DRIVER
            driver = webdriver.Chrome(driver_location)
        #invoke Firefox browser 
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.delete_all_cookies()
        driver.get(self.constant.BASE_URL)
        return driver
