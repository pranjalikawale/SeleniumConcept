import pytest
import socket
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utility.send_mail import SendMail
from utility.constant import Constant
from utility.custom_logger import CustomLogger
from exception.bookswagon_exception import BookswagonException
from utility.read_json import ReadJson

global REMOTE_SERVER 
REMOTE_SERVER= "one.one.one.one"

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    log=CustomLogger.log_utility()
    constant=Constant()
    file_name=[]
    file_name = report.nodeid.split("::")
    if(report.when == 'call' and report.outcome=='passed'):
        log.info('Class Name : '+file_name[1]+' Testcase Name: '+file_name[2]+' when : '+report.when + '  status : ' +report.outcome)
    
    if(report.when == 'call' and report.outcome=='failed'):
        log.error('Class Name : '+file_name[1]+' Testcase Name: '+file_name[2]+' when : '+report.when + '  status : ' +report.outcome)

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
    
        if (report.skipped and xfail) or (report.failed and not xfail):
            screenshot_name=file_name[1]+"::"+file_name[2]+".png"
            screenshot=constant.PATH_SCREENSHOT+screenshot_name
            _capture_screenshot(screenshot)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % screenshot
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False 

@pytest.yield_fixture(scope="class")
def initialize_driver(request):
    global driver
    json_object=ReadJson()
    constant=Constant()
    desired_cap=json_object.read_json(constant.PATH_DESIRED_CAPABILITY)
    credentials=json_object.read_json(constant.PATH_BROWSERSTACK_CREDENTIAL)
    for credential in credentials:
        username=credential['username']
        access_key=credential['access_key']
    for driver_instance in desired_cap:
        url='https://'+str(username)+':'+str(access_key)+'@hub-cloud.browserstack.com/wd/hub'
        driver_instance['browserstack.debug'] = True
        driver_instance['browserstack.networkLogs']=True
        driver_instance['browserstack.console']='info'
        driver = webdriver.Remote(
        command_executor=url,
        desired_capabilities=driver_instance)
        if (is_connected(REMOTE_SERVER)):
            driver.maximize_window()
            driver.get(constant.BASE_URL)
            # Set class attribute and assign the variable
            if request.cls is not None:
                request.cls.driver = driver
            yield driver
            sent_mails=SendMail()
            sent_mails.sent_email_report(constant.PATH_EMAIL,constant.SHEET_MAIL_CREDENTIAL,constant.PATH_REPORT)    
        else:
            raise BookswagonException("No Internet Connection","NO_NETWORK") 
        driver.quit()





