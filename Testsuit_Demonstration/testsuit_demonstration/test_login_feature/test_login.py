import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import unittest
import sys
sys.path.append("C://Users/User/Desktop/python/Testsuit_Demonstration")
class TestLogin(unittest.TestCase):
    
    def test_for_id_locator_and_waits(self):
        driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\driver\chromedriver.exe')
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="http://demo.guru99.com/test/facebook.html"
        driver.get(url)
        #id
        driver.find_element(By.ID,"email").send_keys("abc")
        driver.find_element(By.ID,"pass").send_keys("123")
        driver.find_element(By.ID,"loginbutton").click()
        time.sleep(10)
        #expicit wait
        wait=WebDriverWait(driver,5)
        status=wait.until(EC.title_is(u"Broward College - Fort Lauderdale, FL - Organization, College & University | Facebook"))
        assert status==True
        driver.quit()

if __name__ == "__main__":
    unittest.main()
