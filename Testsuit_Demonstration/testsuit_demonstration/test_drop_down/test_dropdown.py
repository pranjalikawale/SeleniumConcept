import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import unittest
import sys
sys.path.append("C://Users/User/Desktop/python/Testsuit_Demonstration")

class TestDropDown(unittest.TestCase):

    def test_for_class_locator_and_drop_down(self):
        driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\driver\chromedriver.exe')
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
        driver.get(url)
        #input text field
        inputboxes=driver.find_elements(By.CLASS_NAME,"text_field")
        print(len(inputboxes))
        driver.find_element(By.ID,"RESULT_TextField-1").send_keys("pranjali")
        driver.find_element(By.ID,"RESULT_TextField-2").send_keys("kawale")
        #drop down
        drop_down=Select(driver.find_element_by_id("RESULT_RadioButton-9"))
        #select by visible text
        drop_down.select_by_visible_text('Morning')
        #select by index
        drop_down.select_by_index(2)
        #select by index
        drop_down.select_by_value("Radio-2")
        #count of drop down option
        print(len(drop_down.options))
        #Capture all option
        all_options=drop_down.options
        for option in all_options:
            print(option.text)
        assert driver.current_url==url

if __name__ == "__main__":
    unittest.main()
        