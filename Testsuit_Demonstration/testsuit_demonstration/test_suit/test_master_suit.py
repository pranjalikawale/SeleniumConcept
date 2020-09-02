import unittest
from test_login_feature.test_login import TestLogin
from test_drop_down.test_dropdown import TestDropDown

test_cases_login=unittest.TestLoader().loadTestsFromTestCase(TestLogin)
test_cases_dropdown=unittest.TestLoader().loadTestsFromTestCase(TestDropDown)
#create test suit
test_suit=unittest.TestSuite([test_cases_login,test_cases_dropdown])
unittest.TextTestRunner(verbosity=2).run(test_suit)