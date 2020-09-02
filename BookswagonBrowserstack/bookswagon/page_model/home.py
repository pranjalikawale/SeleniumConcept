from utility.UI_operation import UIOperation
from utility.constant import Constant
from exception.bookswagon_exception import BookswagonException
import time
import re

class HomePage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_HOME)

    def search_book(self,bookname):
        search_textbox=self.ui_action.get_locator("textbox_search_id")
        search_textbox.clear()
        search_textbox.send_keys(bookname)
        self.ui_action.get_locator("button_search_id").click()
        time.sleep(5)
        search_result=self.ui_action.get_locator("search_result_xpath").text
        if (len(re.findall(' - did not match any books.', search_result))>0):
            raise BookswagonException("No such book available","NO_SUCH_BOOK_AVAILABLE")
        return search_result        
        
            
            
        
    
       
        