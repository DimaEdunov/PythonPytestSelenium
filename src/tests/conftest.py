import datetime
import os
import shutil
import subprocess
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from pathlib import Path
from datetime import *
import time
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import smtplib

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.assistance_helper_services.test_rail_helpers import create_test_run_in_testrail
from src.assistance_helper_services.testrail_report_results import TestRailReporter
from src.parameters.testrail_parameters import get_testrail_url, get_testrail_api_key


def pytest_addoption(parser):

    parser.addoption(
        "--driver", action="store", default="chrome", help="Returning name of browser")

    parser.addoption(
        "--domain", action="store", default=None, help="Returning name of the domain")

    parser.addoption(
        "--attraction", action="store", default=None, help="Returning name of the attraction")

    parser.addoption(
        "--site_code", action="store", default=None, help="Returning name of the site_code")

    parser.addoption(
        "--domain_cart", action="store", default=None, help="Returning name of the domain_cart")

    parser.addoption(
        "--attraction_cart", action="store", default=None, help="Returning name of the attraction_cart")

    parser.addoption(
        "--site_code_cart", action="store", default=None, help="Returning name of the site_code_cart")

    parser.addoption(
        "--headless", action="store", default="True", help="Returning Headless status")

    parser.addoption(
        "--developer", action="store", default="production", help="Returning Headless status")

    parser.addoption(
        "--env", action="store", default="test", help="Returning Headless status")

    parser.addoption(
        "--from_to_api_time_buffer_seconds", action="store", default=None)



# This method receives driver type from cmd (Default value = 'chrome'), and returns the driver to a test class
# THIS DRIVER IS FOR CRM TESTS ONLY
@pytest.fixture(scope="session")
def driver(request):
    # This section is responsible for webdriver, checking whether to use Headless or Non Headless mode
    options = Options()

    prefs = {"download.default_directory": "c:\\web-automation-downloads"}
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--window-size=1920x1080")

    #for Console logs:
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    # This section is responsible for webdriver, checking whether to use Headless or Non Headless mode
    if request.config.getoption("--headless") == "False":
        options.headless = False
        print("Running in WITHOUT headless mode")
    else:
        options.headless = True
        print("Running WITH headless mode")

    # Initialize the WebDriver with the Service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # size = driver.get_window_size()
    # driver.set_window_size(1920, 1080)
    # print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))
    driver.maximize_window()

    yield driver

    # Quit driver
    driver.quit()

    #All in the following method will happen AFTER the session is ended - DO NOT change this method's name
    # This method contains : Sending Email, Invocing allure report on the screen
    # See additional documentation in here: https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_unconfigure
    try:

        pytest_unconfigure(config=None)

    except AttributeError:
        pass


@pytest.fixture(scope="session")
def application_parameters(request):

    domain = request.config.getoption("--domain")
    environment = request.config.getoption("--env")
    attraction = request.config.getoption("--attraction")
    site_code = request.config.getoption("--site_code")
    domain_cart = request.config.getoption("--domain_cart")
    attraction_cart = request.config.getoption("--attraction_cart")
    site_code_cart = request.config.getoption("--site_code_cart")
    from_to_api_time_buffer_seconds = request.config.getoption("--from_to_api_time_buffer_seconds")

    parameters_dictionary = {"domain": domain,
                             "environment": environment,
                             "attraction": attraction,
                             "site_code": site_code,
                             "domain_cart": domain_cart,
                             "attraction_cart": attraction_cart,
                             "site_code_cart": site_code_cart,
                             "from_to_api_time_buffer_seconds": from_to_api_time_buffer_seconds}
    return parameters_dictionary



# POST SESSION actions - HTML report sending by email, Allure report auto open
def pytest_unconfigure(config)->None:
    import os.path

    print("DOMAIN NAME : "+str(config.getoption('--domain')))
    print("DEVELOPER NAME : "+str(config.getoption("--developer")))

    """ Open Allure report """
    # report_fire_up = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # print("Allure is opening up")
    # os.popen("allure serve C:\\AllureReports\\Data && pause")


    filepath="C:\\AllureReports\\RunAllureLocally.bat"
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    time.sleep(3)

    # Email report functionality
    try:

        """ Time Calculation For HTML Report """
        # Path of report.html file within src/tests path
        base_path = Path(__file__).parent
        file_path = (base_path / "../tests/report.html").resolve()

        # Calculates raw timestamp of html report creation
        raw_value_of_report_creation_timestamp = os.path.getmtime(file_path)
        email_report_creation_time = datetime.fromtimestamp(raw_value_of_report_creation_timestamp)
        delta_time = datetime.now() - email_report_creation_time

        # Log of HTML report creation time
        print("Time passed since report was created in seconds - " + str(delta_time.seconds))

        if delta_time.seconds < 10:

            """ Subscription distribution for HTML report : 'Local' run vs 'Production' run """

            developer_list = {"dima" : "dima@pomvom.com",
                              "xxx" : "xxxx@gmail.com.com"}

            # Helper variables for loop
            developer_list_length = len(developer_list)
            loop_counter = 0
            cc = None

            # Local run
            for list_developer_name, list_developer_email in developer_list.items():
                print("LOOP COUNTER - " +str(loop_counter))
                if config.getoption("--developer") == list_developer_name:
                    cc = list_developer_email
                    print("1 HTML Report Subscription sent to : " +str(cc))
                    break

            # Production
                if config.getoption("--developer") == "production":
                    cc = "dima.e+1@pandats.com,anastasiia.vintrovich@pandats.com"
                    print("2 HTML Report Subscription sent to :" +str(cc))
                    break
                loop_counter += 1


            """ Creation and sending of HTML report """
            # Building an email + HTML report attachment
            fromaddr = "pandaautomation.report@gmail.com"
            to = "dima.e@pandats.com"

            rcpt = cc.split(",") + [to]

            # instance of MIMEMultipart
            msg = MIMEMultipart()

            # storing the senders email address
            msg['From'] = fromaddr

            # storing the receivers email address
            msg['To'] = to

            msg['Cc'] = cc

            # storing the subject
            msg['Subject'] = "Automation %s suite run completed for the domain : %s | %s " %(config.getoption('-m').title(),
                                                                                            config.getoption('--domain').title(),
                                                                                            str(datetime.today().strftime('%d-%m-%Y , %H:%M')))

            # string to store the body of the mail
            body = "Automation run has been completed. \n\n" \
                   "Time : " +str(datetime.today().strftime('%d-%m-%Y , %H:%M')) +"\n" \
                   "Domain : " +config.getoption('--domain').title() +"\n" \
                   "Suite : " +config.getoption('-m').title() +"\n\n\n" \
                   "To review the report - please download the file and open it locally on your device. \n\n" \
                    "- QA & Automation Team -"

            # attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # open the file to be sent
            filename = file_path
            attachment = open(filename, "rb")

            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')

            # To change the payload into encoded form
            p.set_payload((attachment).read())

            # encode into base64
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            # attach the instance 'p' to instance 'msg'
            msg.attach(p)

            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login("pandaautomation.report@gmail.com", "p4Mq4EEhUyEQ")

            # Converts the Multipart msg into a string
            text = msg.as_string()

            # sending the mail
            s.sendmail(fromaddr, rcpt, text)

            print("EMAIL SENT")

            # The temporary download directory removal
            shutil.rmtree("c:\\web-automation-downloads")

            # terminating the session
            s.quit()
    except OSError as e:
        pass

# this function is to retrive all test names in this project
# def pytest_collection_modifyitems(config, items):
#     test_names = [item.name for item in items if isinstance(item, pytest.Function)]
#     print("All test names in the entire project:", test_names)


@pytest.fixture(scope="session", autouse=True)
def setup_test_run(request):
    current_date = datetime.today().strftime('%d-%m-%Y , %H:%M')
    test_run_name = "Regression " + str(current_date)

    # Create a new Test Run at the beginning of the test run
    test_run_id = create_test_run_in_testrail(test_run_name)

    # Instantiate TestRailReporter
    testrail_reporter = TestRailReporter()

    # Pass the Test Run ID and TestRailReporter instance to subsequent tests
    request.config.test_run_id = test_run_id
    request.config.testrail_reporter = testrail_reporter

    yield testrail_reporter

    # Finalize the Test Run at the end of the session
    testrail_reporter.update_test_results(get_testrail_url(), request.config.test_run_id)


