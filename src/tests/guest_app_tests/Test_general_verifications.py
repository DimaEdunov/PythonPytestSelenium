import time
import allure
import pytest
from allure_commons.types import AttachmentType

from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from src.parameters.domain_settings import DomainSetting
from src.assistance_helper_services.email_page import EmailPage
from src.page_objects.guest_app_po.help_and_support_page import HelpAndSupportPage
from src.parameters import email_parameters
from src.page_objects.guest_app_po.side_menu_page import SideMenuPage
from src.assistance_helper_services import driver_related_actions
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.phone_page import PhonePage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.assistance_helper_services.api_helpers import ApiHelpers
from src.parameters.guest_parameters import GuestParameters
from src.assistance_helper_services.application_urls import ApplicationUrls


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=1)
def test_terms_and_conditions_login_page_verification(request, driver, application_parameters):
    test_name = "test_terms_and_conditions_login_page_verification"
    try:
        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.go_to_terms_and_conditions_page()

        phone_page_object.terms_and_conditions_page_verification()

        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=True))

    except:
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=False))

        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        assert False


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=2)
def test_contact_us_form_verification(request, driver, application_parameters):
    test_name = "test_contact_us_form_verification"
    try:
        phone_number = GuestParameters.get_random_backdoor_phone()

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        phone_number, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(phone_number,
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        # Login Verification
        home_page_object = FeedPage(driver)
        home_page_object.login_verification()

        side_menu_object = SideMenuPage(driver)
        side_menu_object.go_to(WebGuestAppStaticElements.HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU.value)

        help_and_support_object = HelpAndSupportPage(driver)

        help_and_support_object.contact_us_form_open_verification()

        #######
        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()
        # - End of log out

        driver.get(email_parameters.get_contact_us_url())

        help_and_support_object.send_contact_us_form()

        help_and_support_object.contact_us_verification()

        time.sleep(7)

        driver.get(email_parameters.get_outlook_url())

        gmail_object = EmailPage(driver)
        gmail_object.email_login()

        gmail_object.confirm_email_received()

        gmail_object.delete_email()

        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=True))

    except:

        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=False))

        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        assert False
