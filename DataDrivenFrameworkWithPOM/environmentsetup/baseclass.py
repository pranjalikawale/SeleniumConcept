from selenium import webdriver

class BaseClass():
    
    @staticmethod
    def initialize():
        global driver
        base_url="https://admin-demo.nopcommerce.com/"
        driver=webdriver.Chrome(executable_path=r"C:\Users\User\Desktop\python\DataDrivenWithPOM\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get(base_url)
        return driver
    
    @staticmethod
    def close_driver():
        driver.close()
        return driver
        
