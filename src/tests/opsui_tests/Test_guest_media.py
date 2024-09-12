import time
from allure_commons.types import AttachmentType
import allure
import pytest

from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.page_objects.opsui_app_po.find_media_by_attraction_page import FindMediaByAttractionPage
from src.parameters.domain_settings import DomainSetting
from src.assistance_helper_services import application_helpers
from src.elements.ops_ui.dynamic_elemenets.opsui_dynamic_elements_picklists import OpsuiDynamicElementsPicklists
from src.page_objects.opsui_app_po.global_opsui_actions import GlobalOpsuiActions
from src.page_objects.guest_app_po.account_settings_page import AccountSettingsPage
from src.page_objects.opsui_app_po.global_guest_search_opsui import GlobalGuestSearchOpsui
from src.parameters.opsui_parameters import OpsuiAppParameters
from src.assistance_helper_services import driver_related_actions
from src.assistance_helper_services.api_helpers import ApiHelpers
from src.assistance_helper_services.application_urls import ApplicationUrls
from src.page_objects.guest_app_po.add_media_page import AddMediaPage
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.phone_page import PhonePage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.page_objects.opsui_app_po.guest_page import GuestPage
from src.page_objects.opsui_app_po.home_page import OpsuiHomePage
from src.page_objects.opsui_app_po.search_guest_page import SearchGuestPage
from src.parameters.guest_parameters import GuestParameters


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
@pytest.mark.run(order=1)
def test_guest_media_search_a_non_existing_guest_by_qr(request, driver, application_parameters):
    test_name = "test_guest_media_search_a_non_existing_guest_by_qr"
    try:

        qr_number = OpsuiAppParameters.get_opsui_qr("random_qr")

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        phone_or_qr=qr_number,
                                        account_type=GuestParameters.get_account_type("qr")
                                        )

        get_user_id = api_helpers_object.api_get_userid_by_qr_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page_object = OpsuiHomePage(driver)
        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        # Login to opsui
        opsui_home_page_object.opsui_login()
        opsui_home_page_object.login_verification()
        opsui_guest_page_object = GuestPage(driver)

        # Search guest by non existing qr

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.guest_search)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        time.sleep(1.5)

        opsui_global_search_object.type_qr_or_userid(qr_number)

        opsui_global_search_object.click_on_submit()

        opsui_global_search_object.click_on_create()

        opsui_guest_page_object.new_qr_creation_verification()

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
@pytest.mark.run(order=2)
def test_guest_media_search_an_existing_guest_by_guest_id(request, driver, application_parameters):
    test_name = "test_guest_media_search_an_existing_guest_by_guest_id"
    try:
        used_phone_number = GuestParameters.get_random_backdoor_phone()

        ######
        # Registration to app & login
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        used_phone_number, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(used_phone_number, GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        home_page_object.login_verification()

        #######
        # Registration to app & Login

        add_media = AddMediaPage(driver)

        get_new_user_id = add_media.get_userId_number()

        #######
        # Logout
        home_page_object.logout()
        phone_page_object.logout_verification()
        # End of Logout
        #######

        ########
        #### - Navigate to OpsUI & Login
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.guest_search)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        print(get_user_id)

        opsui_global_search_object.type_qr_or_userid(get_new_user_id)

        opsui_global_search_object.click_on_submit()

        guest_page_object = GuestPage(driver)

        global_opsui_actions = GlobalOpsuiActions(driver)

        actual_user_id = global_opsui_actions.get_guest_id()

        print(get_new_user_id)
        print(actual_user_id)

        guest_page_object.guest_exist_and_has_correct_id_verification(get_new_user_id, actual_user_id)

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
@pytest.mark.run(order=3)
def test_guest_media_search_a_non_existing_guest_by_phone(request, driver, application_parameters):
    test_name = "test_guest_media_search_a_non_existing_guest_by_phone"
    try:
        new_phone = GuestParameters.get_random_backdoor_phone()

        # Deleting a guest, for the last case of 'None existing guest'
        guest_page_object = GuestPage(driver)

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        new_phone,
                                        GuestParameters.get_account_type("qr"))

        # get_user_id = api_helpers_object.api_get_userid_request()
        get_user_id = api_helpers_object.api_get_userid_by_phone_request(type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        ########
        #### - Navigate to OpsUI & Login

        driver.refresh()

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.guest_search)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        search_guest_page = SearchGuestPage(driver)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        ### needs to be separated test
        opsui_global_search_object.type_guest_phone(GuestParameters.get_country_code_without_plus_prefix("Israel"),
                                                    GuestParameters.get_too_short_phone())

        search_guest_page.guest_search_phone_verification(GuestParameters.get_too_short_phone())

        new_phone = GuestParameters.get_random_backdoor_phone()

        # Delete phone precondition
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel, new_phone, GuestParameters.get_account_type("qr"))

        # get_user_id = api_helpers_object.api_get_userid_request()
        get_user_id = api_helpers_object.api_get_userid_by_phone_request(type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        # Delete phone ending here
        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        opsui_global_search_object.type_guest_phone(GuestParameters.get_country_code_without_plus_prefix("Israel"), new_phone)

        opsui_global_search_object.click_on_submit()

        time.sleep(1.5)

        guest_page = GuestPage(driver)

        guest_page.photos_in_guest_page_verification(test_status=FindMediaByAttractionPage.positive)

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
@pytest.mark.run(order=4)
def test_guest_media_search_an_existing_guest_by_phone(request, driver, application_parameters):
    test_name = "test_guest_media_search_an_existing_guest_by_phone"
    try:
        ########
        #### - Navigate to OpsUI & Login

        driver.refresh()

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.guest_search)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_guest_phone(GuestParameters.get_country_code_without_plus_prefix("Israel"),
                                                    GuestParameters.get_valid_existing_phone())

        opsui_global_search_object.click_on_submit()

        guest_page = GuestPage(driver)
        guest_page.photos_in_guest_page_verification(test_status=FindMediaByAttractionPage.negative)

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


#STABLE
@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
@pytest.mark.run(order=5)
def test_guest_media_search_a_non_existing_guest_by_guest_id(request, driver, application_parameters):
    test_name = "test_guest_media_search_a_non_existing_guest_by_guest_id"
    try:
        used_phone_number = GuestParameters.get_random_backdoor_phone()

        ######
        # Registration to app & login
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        used_phone_number, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(used_phone_number, GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        home_page_object.login_verification()

        #######
        # Registration to app & Login

        add_media = AddMediaPage(driver)

        get_new_user_id = add_media.get_userId_number()
        print(get_new_user_id)
        account_settings_page_object = AccountSettingsPage(driver)
        account_settings_page_object.delete_user()

        #######
        # Logout
        phone_page_object.logout_verification()
        # End of Logout
        #######

        ########
        #### - Navigate to OpsUI & Login
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.guest_search)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        search_guest = SearchGuestPage(driver)

        search_guest.search_guest_by_qr_or_userid(OpsuiAppParameters.get_too_short_userid())
        search_guest.userid_too_short_verification()

        search_guest.search_guest_by_qr_or_userid(get_new_user_id)

        # search_guest.click_on_create_or_submit()
        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.click_on_submit()
        search_guest.guest_does_not_exist_popup_verification()

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
