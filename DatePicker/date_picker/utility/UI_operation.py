from selenium import webdriver
from selenium.webdriver.common.by import By
from object_repository.read_properties_object import ReadPropertiesObject
from utility.constant import Constant
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class UIOperation():
    def __init__(self,driver,path):
        self.driver=driver
        self.properties_object=ReadPropertiesObject(path)
       
    def get_locator(self,web_element_name):
        locator_type,locator_value=self.properties_object.get_property(web_element_name)
        try:
            #Find by xpath
            if locator_type.strip().upper() == "XPATH":
                while True:
                    try:
                        # Define an element that you can start scraping when it appears
                        # If the element appears after 5 seconds, break the loop and continue
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, str(locator_value))))
                        break
                    except TimeoutException:
                        # If the loading took too long, print message and try again
                        print("Loading took too much time!")
                return self.driver.find_element_by_xpath(str(locator_value))
            #find by id
            elif locator_type.strip().upper() == "ID":
                while True:
                    try:
                        # Define an element that you can start scraping when it appears
                        # If the element appears after 5 seconds, break the loop and continue
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, str(locator_value))))
                        break
                    except TimeoutException:
                        # If the loading took too long, print message and try again
                        print("Loading took too much time!")
                return self.driver.find_element_by_id(str(locator_value))
            #find by link
            elif locator_type.strip().upper() == "LINK_TEXT":
                while True:
                    try:
                        # Define an element that you can start scraping when it appears
                        # If the element appears after 5 seconds, break the loop and continue
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, str(locator_value))))
                        break
                    except TimeoutException:
                        # If the loading took too long, print message and try again
                        print("Loading took too much time!")
                return self.driver.find_element_by_link_text(str(locator_value))
            #find by name
            elif locator_type.strip().upper() == "NAME":
                while True:
                    try:
                        # Define an element that you can start scraping when it appears
                        # If the element appears after 5 seconds, break the loop and continue
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, str(locator_value))))
                        break
                    except TimeoutException:
                        # If the loading took too long, print message and try again
                        print("Loading took too much time!")
                return self.driver.find_element_by_name(str(locator_value))
            #find by partiallink
            elif locator_type.strip().upper() == "PARTIAL_LINK_TEXT":
                while True:
                    try:
                        # Define an element that you can start scraping when it appears
                        # If the element appears after 5 seconds, break the loop and continue
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, str(locator_value))))
                        break
                    except TimeoutException:
                        # If the loading took too long, print message and try again
                        print("Loading took too much time!")
                return self.driver.find_element_by_partial_link_text(str(locator_value))
            #find by tag_name
            elif locator_type.strip().upper() == "TAG_NAME":
                while True:
                    try:
                        # Define an element that you can start scraping when it appears
                        # If the element appears after 5 seconds, break the loop and continue
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, str(locator_value))))
                        break
                    except TimeoutException:
                        # If the loading took too long, print message and try again
                        print("Loading took too much time!")
                return self.driver.find_element_by_tag_name(str(locator_value))
            #find by classname
            elif locator_type.strip().upper() == "CLASS_NAME":
                while True:
                    try:
                        # Define an element that you can start scraping when it appears
                        # If the element appears after 5 seconds, break the loop and continue
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, str(locator_value))))
                        break
                    except TimeoutException:
                        # If the loading took too long, print message and try again
                        print("Loading took too much time!")
                return self.driver.find_element_by_class_name(str(locator_value))
            #find by css
            elif locator_type.strip().upper() == "CSS_SELECTOR":
                while True:
                    try:
                        # Define an element that you can start scraping when it appears
                        # If the element appears after 5 seconds, break the loop and continue
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, str(locator_value))))
                        break
                    except TimeoutException:
                        # If the loading took too long, print message and try again
                        print("Loading took too much time!")
                return self.driver.find_element_by_css_selector(str(locator_value))
        except Exception as e:
            print("Invalid Locator Type",e)
            


