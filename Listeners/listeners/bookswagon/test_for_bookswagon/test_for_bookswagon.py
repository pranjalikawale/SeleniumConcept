import pytest
from utility.UI_operation import UIOperation
from utility.constant import Constant
from page_model.login import LoginPage
from page_model.home import HomePage
from exception.bookswagon_exception import BookswagonException

@pytest.mark.usefixtures("initialize_driver")
class TestBookswagon():
    
    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
            self.driver=initialize_driver
            self.constant=Constant()
    
    def test_login(self):
        login=LoginPage(self.driver)
        myaccount=login.login(self.constant.PATH_LOGIN_CREDENTIAL)
        assert myaccount=="pranjalikawale11@gma"

    def test_search_book_not_available(self):
        with pytest.raises(BookswagonException) as exception:
            home=HomePage(self.driver)
            home.search_book("xzsaz")
        assert str(exception.value)=='NO_SUCH_BOOK_AVAILABLE'  

    def test_search_book(self):
        home=HomePage(self.driver)
        result_count=home.search_book("Life is what is you make it")
        assert self.driver.title=="life is what is you make it - Books - 24x7 online bookstore Bookswagon.com" and  result_count=="42 results found"
    
           
    
    
    
       

    
 
    