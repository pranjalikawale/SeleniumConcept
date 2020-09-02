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
from selenium import webdriver

@pytest.mark.usefixtures("initialize_driver")
class TestNegativeCaseBookswagon():
    
    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
        self.driver=initialize_driver
        self.constant=Constant()
    
    def test_login(self):
        login=LoginPage(self.driver)
        error=login.login_for_multiple_invalid_data(self.constant.PATH_NEGATIVE_LOGIN_CREDENTIAL)
        assert error=="Please enter correct Email or Password."

    def test_shipping_address(self):
        login=LoginPage(self.driver)
        login.login(self.constant.PATH_LOGIN_CREDENTIAL)
        home=HomePage(self.driver)
        home.search_book("Life is what is you make it")
        placed_orders=PlacedOrderPage(self.driver)
        placed_orders.placing_order(1)
        shipping=ShippingAddressPage(self.driver)
        error=shipping.shipping_address(self.constant.PATH_TESTDATA,self.constant.SHEET_SHIPPING_ADDRESS)
        assert error=="Invalid"
    
    def test_add_to_cart_and_placed_order_with_zero_quantity(self):
        logout=LogoutPage(self.driver)
        logout.logout()
        login=LoginPage(self.driver)
        login.login(self.constant.PATH_LOGIN_CREDENTIAL)
        home=HomePage(self.driver)
        home.search_book("Life is what is you make it")
        placed_orders=PlacedOrderPage(self.driver)
        error=placed_orders.placing_order(0)
        assert error=="Invalid"
    
    
    