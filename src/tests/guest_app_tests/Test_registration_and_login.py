import time
import allure
import pytest
from allure_commons.types import AttachmentType

from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from src.page_objects.guest_app_po.side_menu_page import SideMenuPage
from src.parameters.domain_settings import DomainSetting
from src.assistance_helper_services import driver_related_actions
from src.assistance_helper_services.api_helpers import ApiHelpers
from src.assistance_helper_services.application_urls import ApplicationUrls
from src.page_objects.guest_app_po.account_settings_page import AccountSettingsPage
from src.page_objects.guest_app_po.add_media_page import AddMediaPage
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.parameters.guest_parameters import GuestParameters
from src.page_objects.guest_app_po.phone_page import PhonePage


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=1)
def test_delete_user_and_register_with_a_new_user(request, driver, application_parameters):
    test_name = "test_delete_user_and_register_with_a_new_user"
    try:
        #####
        # registration
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        GuestParameters.get_registration_tests_backdoor_phone(),
                                        GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone(),
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

        phone_page_object.accept_cookies()

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        # Login Verification
        home_page_object.login_verification()

        # end registration
        #####

        add_media = AddMediaPage(driver)
        get_deleted_user_id = add_media.get_userId_number()

        account_settings_page_object = AccountSettingsPage(driver)
        account_settings_page_object.delete_user()

        #####
        # registration
        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone(),
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

        phone_page_object.accept_cookies()

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        # Login Verification
        home_page_object.login_verification()
        # end registration
        ######

        get_new_user_id = add_media.get_userId_number()

        account_settings_page_object.new_user_verification(get_deleted_user_id, get_new_user_id)

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


@allure.story('Logout')
@pytest.mark.regression
# @pytest.mark.dev
# This decorator gives an order of a test
@pytest.mark.run(order=2)
def test_logout(request, driver):
    test_name = "test_logout"
    try:
        # Logout & Logout verification
        home_page_object = FeedPage(driver)

        home_page_object.logout()

        phone_page_object = PhonePage(driver)
        phone_page_object.logout_verification()

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
@pytest.mark.run(order=3)
def test_negative_login(request, driver, application_parameters):
    test_name = "test_negative_login"
    try:
        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_invalid_phone_number(GuestParameters.get_invalid_login_phone())

        phone_page_object.invalid_phone_number_verification()
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
@pytest.mark.run(order=4)
def test_positive_login(request, driver, application_parameters):
    test_name = "test_positive_login"
    try:
        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone(),
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

        home_page_object.logout()
        phone_page_object.logout_verification()

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
@pytest.mark.run(order=5)
def test_terms_and_conditions_page_verification(request, driver, application_parameters):
    test_name = "test_terms_and_conditions_page_verification"
    try:
        #####
        # registration
        random_phone_number_backdoor = GuestParameters.get_registration_tests_backdoor_phone()

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        random_phone_number_backdoor, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.insert_phone_number_and_country_code(random_phone_number_backdoor,
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

        phone_page_object.accept_cookies()

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)
        home_page_object.login_verification()

        side_menu_object = SideMenuPage(driver)
        side_menu_object.go_to(WebGuestAppStaticElements.TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU.value)

        phone_page_object.terms_and_conditions_page_verification()

        phone_page_object.click_on_go_back_button_in_terms_and_conditions_page()

        #######
        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()
        # - End of log out

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
