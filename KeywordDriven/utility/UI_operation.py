from selenium import webdriver

class UIOperation():

    def __init__(self,driver):
        self.driver=driver
    
    def perform_action(self,operation,locator,locator_type,value):
        element=self.get_element_by_object(locator,locator_type)
        if operation=="CLICK":
            element.click()
        elif operation=="SETTEXT":
            element.clear()
            element.send_keys(value)
        elif operation=="GOTOURL":
            self.driver.get(value)
       
    def get_element_by_object(self,locator,locator_type):
        try:
            #Find by xpath
            if locator_type == "XPATH":
                return self.driver.find_element_by_xpath(str(locator))
            #find by id
            elif locator_type == "ID":
                return self.driver.find_element_by_id(str(locator))
            #find by link
            elif locator_type == "LINK_TEXT":
                return self.driver.find_element_by_link_text(str(locator))
            #find by name
            elif locator_type == "NAME":
                return self.driver.find_element_by_name(str(locator))
            #find by partiallink
            elif locator_type == "PARTIAL_LINK_TEXT":
                return self.driver.find_element_by_partial_link_text(str(locator))
            #find by tag_name
            elif locator_type == "TAG_NAME":
                return self.driver.find_element_by_tag_name(str(locator))
            #find by classname
            elif locator_type == "CLASS_NAME":
                return self.driver.find_element_by_class_name(str(locator))
            #find by css
            elif locator_type == "CSS":
                return self.driver.find_element_by_css(str(locator))
        except Exception as e:
            print("Invalid Locator Type",e)
