import pytest
from environment_setup.browser_instance import BrowserInstance

@pytest.yield_fixture(scope="function")
def initialize_driver(request,browser):
    driver=BrowserInstance(browser).get_browser_instance()
    # Set class attribute and assign the variable
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    
# Create parsers to get value from command prompt
def pytest_addoption(parser):
    parser.addoption("--browser")

#Return the argument value
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")    




