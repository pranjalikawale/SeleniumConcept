import pytest
import time
import sys
sys.path.append("C://Users/User/Desktop/python/Bookswagon")
from utility.UI_operation import UIOperation
from utility.constant import Constant
from page_model.login import LoginPage
from page_model.home import HomePage
from page_model.placed_order import PlacedOrderPage
from page_model.review_order import ReviewOrderPage
from page_model.shipping_address import ShippingAddressPage
from page_model.logout import LogoutPage
from exception.bookswagon_exception import BookswagonException
from selenium import webdriver


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
        assert self.driver.title=="life is what is you make it - Books - 24x7 online bookstore Bookswagon.com" and  result_count=="43 results found"
    
    def test_add_to_cart_and_placed_order(self):
        placed_orders=PlacedOrderPage(self.driver)
        order_status=placed_orders.placing_order(1)
        assert order_status=="Your order details will be sent to this email address."

    def test_shipping_address(self):
        shipping=ShippingAddressPage(self.driver)
        shipping_address=shipping.shipping_address(self.constant.PATH_TESTDATA,self.constant.SHEET_NAME)
        assert shipping_address=="Maharashtra"
   
    def test_review_order(self):
        review_orders=ReviewOrderPage(self.driver)
        review_status=review_orders.review_order("Please puut cover on it")
        assert review_status=="Choose your mode of payment"

    def test_logout(self):
        logout=LogoutPage(self.driver)
        status=logout.logout()
        assert status=="Login"
       
    def test_select_previously_store_delivery_address(self):
        login=LoginPage(self.driver)
        login.login(self.constant.PATH_LOGIN_CREDENTIAL)
        home=HomePage(self.driver)
        home.search_book("Life is what is you make it")
        placed_orders=PlacedOrderPage(self.driver)
        placed_orders.placing_order(2)
        shipping=ShippingAddressPage(self.driver)
        shipping_address=shipping.previous_address("123456")
        assert shipping_address=="Maharashtra"
    
    
       

    
 
    