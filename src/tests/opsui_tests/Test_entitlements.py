import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.parameters.domain_settings import DomainSetting
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements
from src.page_objects.opsui_app_po.guest_page import GuestPage
from src.parameters.domains import get_region_code, get_site_code, get_attraction_code
from src.assistance_helper_services import application_helpers
from src.elements.ops_ui.dynamic_elemenets.opsui_dynamic_elements_picklists import OpsuiDynamicElementsPicklists
from src.assistance_helper_services.connector import Connector
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from src.page_objects.guest_app_po.side_menu_page import SideMenuPage
from src.page_objects.opsui_app_po.find_media_by_attraction_page import FindMediaByAttractionPage
from src.page_objects.opsui_app_po.global_opsui_actions import GlobalOpsuiActions
from src.parameters.side_menu_parameters import SideMenuParameters
from src.page_objects.opsui_app_po.global_guest_search_opsui import GlobalGuestSearchOpsui
from src.parameters.opsui_parameters import OpsuiAppParameters
from src.page_objects.guest_app_po.account_settings_page import AccountSettingsPage
from src.page_objects.opsui_app_po.entitlements_page import EntitlementsPage
from src.assistance_helper_services import driver_related_actions
from src.assistance_helper_services.api_helpers import ApiHelpers
from src.assistance_helper_services.application_urls import ApplicationUrls
from src.page_objects.guest_app_po.add_media_page import AddMediaPage
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.page_objects.opsui_app_po.home_page import OpsuiHomePage
from src.page_objects.opsui_app_po.search_guest_page import SearchGuestPage
from src.parameters.guest_parameters import GuestParameters
from src.page_objects.guest_app_po.phone_page import PhonePage

guest_object = GuestParameters(media_prefix=None, user_id=None, phone=None)


# STABLE
@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
@pytest.mark.run(order=1)
def test_entitlement_search_a_non_existing_guest_by_guest_id(request, driver, application_parameters):
    test_name = "test_entitlement_search_a_non_existing_guest_by_guest_id"
    try:
        user_phone_number = GuestParameters.get_random_backdoor_phone()

        ######
        # Registration to app & login
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        user_phone_number, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(user_phone_number,
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

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
                                                                                 OpsuiAppParameters.entitlements)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(get_new_user_id)

        opsui_global_search_object.click_on_submit()

        search_guest = SearchGuestPage(driver)

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


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
@pytest.mark.run(order=2)
def test_entitlement_search_an_existing_guest_by_guest_id(request, driver, application_parameters):
    test_name = "test_entitlement_search_an_existing_guest_by_guest_id"
    try:
        used_phone_number = GuestParameters.get_random_backdoor_phone()

        ######
        # Registration to app & login
        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(used_phone_number,
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

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
                                                                                 OpsuiAppParameters.entitlements)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        guest_search = SearchGuestPage(driver)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(get_new_user_id)

        opsui_global_search_object.click_on_submit()

        entitlements_page = EntitlementsPage(driver)

        entitlements_page.entitlements_page_opened_verification()

        ###### Delete guest via API
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        used_phone_number, GuestParameters.get_account_type("app"))

        api_helpers_object.api_delete_userid_request(get_new_user_id,
                                                     type=DomainSetting.get_domain_type('non_cart_domain'))

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
def test_entitlement_search_a_non_existing_guest_by_phone(request, driver, application_parameters):
    test_name = "test_entitlement_search_a_non_existing_guest_by_phone"
    try:
        used_phone_number = GuestParameters.get_random_backdoor_phone()

        ######
        # Registration to app & login
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        used_phone_number, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(used_phone_number,
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        home_page_object.login_verification()

        #######
        # Registration to app & Login

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
                                                                                 OpsuiAppParameters.entitlements)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_guest_phone(GuestParameters.get_country_code_without_plus_prefix("Israel"),
                                                    used_phone_number)

        opsui_global_search_object.click_on_submit()

        opsui_global_search_object.click_on_create()

        entitlements_guest_object = EntitlementsPage(driver)

        entitlements_guest_object.entitlements_page_opened_verification()

        entitlements_guest_object.entitlements_verify_phone_number(used_phone_number)

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

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
def test_entitlement_search_an_existing_guest_by_phone(request, driver, application_parameters):
    test_name = "test_entitlement_search_an_existing_guest_by_phone"
    try:
        #### - Navigate to OpsUI & Login
        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.entitlements)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_guest_phone(GuestParameters.get_country_code_without_plus_prefix("Israel"),
                                                    GuestParameters.get_login_backdoor_phone())

        opsui_global_search_object.click_on_submit()

        entitlements_guest_object = EntitlementsPage(driver)

        entitlements_guest_object.entitlements_page_opened_verification()

        entitlements_guest_object.entitlements_verify_phone_number(GuestParameters.get_login_backdoor_phone())

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
@pytest.mark.run(order=5)
def test_entitlement_search_a_non_existing_guest_by_qr(request, driver, application_parameters):
    test_name = "test_entitlement_search_a_non_existing_guest_by_qr"
    try:
        qr_number = OpsuiAppParameters.get_opsui_qr("random_qr")

        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.entitlements)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(qr_number)

        opsui_global_search_object.click_on_submit()

        opsui_global_search_object.click_on_create()

        entitlements_guest_object = EntitlementsPage(driver)

        entitlements_guest_object.entitlements_page_opened_verification()

        global_opsui_actions = GlobalOpsuiActions(driver)

        qr_user_id = global_opsui_actions.get_guest_id()

        api_helpers_object = ApiHelpers(application_parameters, key=None,
                                        phone_or_qr=None,
                                        account_type=GuestParameters.get_account_type("qr"))

        api_helpers_object.api_delete_userid_request(qr_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

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
@pytest.mark.run(order=6)
def test_entitlement_search_an_existing_guest_by_qr(request, driver, application_parameters):
    test_name = "test_entitlement_search_an_existing_guest_by_qr"
    try:
        existing_qr = GuestParameters.get_random_qr()

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        existing_qr, GuestParameters.get_account_type("qr"))

        api_helpers_object.api_create_qr_user_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.entitlements)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(existing_qr)

        opsui_global_search_object.click_on_submit()

        entitlements_guest_object = EntitlementsPage(driver)

        entitlements_guest_object.entitlements_page_opened_verification()

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        user_id = api_helpers_object.api_get_userid_by_qr_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        api_helpers_object.api_delete_userid_request(user_id, type=DomainSetting.get_domain_type('non_cart_domain'))
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
@pytest.mark.run(order=7)
def test_entitlement_give_guest_entitlement(request, driver, application_parameters):
    test_name = "test_entitlement_give_guest_entitlement"
    try:
        ####
        # registration
        guest_phone_for_add_and_delete_entitlement_tests = GuestParameters.get_random_backdoor_phone()

        guest_object.set_phone(guest_phone_for_add_and_delete_entitlement_tests)

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        guest_object.get_phone(),
                                        GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)
        url_manager = ApplicationUrls(application_parameters)
        url_with_qr = url_manager.return_url(ApplicationUrls.guestapp) + GuestParameters.get_qr_for_url(
            GuestParameters.get_random_qr())
        driver.get(url_with_qr)

        driver_related_actions.delete_cookies(driver)

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(guest_object.get_phone(),
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

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
        user_id = add_media.get_userId_number()
        guest_object.set_user_id(user_id)

        # open opsui in a new tab - keep guest app open in the existing tab
        driver_related_actions.open_and_switch_to_new_url_in_new_window(driver,
                                                                        url_manager.return_url(ApplicationUrls.opsui))

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.entitlements)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(guest_object.get_user_id())

        opsui_global_search_object.click_on_submit()

        entitlements_guest_object = EntitlementsPage(driver)

        entitlements_guest_object.entitlements_page_opened_verification()

        entitlement_type_text = entitlements_guest_object.add_entitlement_to_guest()

        entitlements_guest_object.verify_entitlement_added_to_guest(entitlement_type_text,
                                                                    OpsuiAppStaticElements.ENTITLEMENT_PAGE_TYPE_TEXT_FIRST.value)

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        connector_object = Connector(application_parameters=application_parameters,
                                     connector_main_path=Connector.get_connector_main_path(),
                                     media_path=Connector.get_media_path(Connector.get_connector_main_path()),
                                     uploads_path=Connector.get_uploads_path(Connector.get_connector_main_path()))

        connector_object.edit_config_file(type=DomainSetting.get_domain_type('non_cart_domain'))

        connector_object.drag_and_drop_media_to_uploads_folder()

        connector_object.run_connector()

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_attraction)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_attraction_object = FindMediaByAttractionPage(driver)

        find_media_by_attraction_object.find_media_by_attraction_page_opened_verification()

        find_media_by_attraction_object.search_photos()

        global_opsui_actions = GlobalOpsuiActions(driver)

        global_opsui_actions.open_photo_details()

        global_opsui_actions.add_photo_to_guest()

        opsui_global_search_object.type_qr_or_userid(guest_object.get_user_id())

        opsui_global_search_object.click_on_submit()

        find_media_by_attraction_object.popup_added_to_guest_pass_verification()

        global_opsui_actions.go_to_home_page()

        # go to guest app tab
        driver_related_actions.switch_to_default_window(driver)

        # go to home page and refresh
        guest_app_side_menu_object = SideMenuPage(driver)

        guest_app_side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        guest_app_side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("home"))

        driver.refresh()

        home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=False)

        #######
        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()
        # - End of log out

        driver_related_actions.switch_and_close_selected_window(driver, 0)

        driver_related_actions.switch_to_default_window(driver)

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
@pytest.mark.run(order=8)
def test_entitlement_remove_entitlement(request, driver, application_parameters):
    test_name = "test_entitlement_remove_entitlement"
    try:

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        GuestParameters.get_login_backdoor_phone_payment(),
                                        account_type=GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.entitlements)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(guest_object.get_user_id())

        opsui_global_search_object.click_on_submit()

        entitlements_guest_object = EntitlementsPage(driver)

        entitlements_guest_object.entitlements_page_opened_verification()

        entitlements_guest_object.remove_entitlement_to_guest()

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        driver_related_actions.delete_cookies(driver)

        phone_page_object = PhonePage(driver)

        phone_page_object.insert_phone_number_and_country_code(guest_object.get_phone(),
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

        home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)

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


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=9)
def test_entitlement_give_guest_entitlement_cart(request, driver, application_parameters):
    test_name = "test_entitlement_give_guest_entitlement_cart"
    try:
        connector_object = Connector(application_parameters=application_parameters,
                                     connector_main_path=Connector.get_connector_main_path(),
                                     media_path=Connector.get_video_path(Connector.get_connector_main_path()),
                                     uploads_path=Connector.get_uploads_path(Connector.get_connector_main_path()))

        connector_object.edit_config_file(type=DomainSetting.get_domain_type('domain_cart'))

        original_file_names = connector_object.find_media()

        connector_object.change_date_photo_file_name(original_file_names)

        connector_object.drag_and_drop_media_to_uploads_folder()

        connector_object.run_connector()

        used_email = GuestParameters.get_email_address()

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        GuestParameters.get_login_backdoor_phone_payment(),
                                        account_type=GuestParameters.get_account_type("app"))

        email_user_id = api_helpers_object.api_create_email_user_request(used_email, GuestParameters.get_random_qr(),
                                                                         type=DomainSetting.get_domain_type(
                                                                             'domain_cart'))

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.opsui_cart))

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        opsui_home_page.change_language_to_english()

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain_cart"],
                                                                                 OpsuiAppParameters.guest_search)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(email_user_id)

        opsui_global_search_object.click_on_submit()

        opsui_guest_page = GuestPage(driver)
        opsui_guest_page.go_to_add_media_by_attraction_via_guest_page()

        find_media_by_attraction_object = FindMediaByAttractionPage(driver)

        # Associate media to user
        find_media_by_attraction_object.click_on_select_multi_or_unselect_all_button()

        find_media_by_attraction_object.select_multiple_medias(number_of_media_to_be_selected=3)

        find_media_by_attraction_object.verify_multiple_medias_were_selected(number_of_photos_to_verify=3)

        find_media_by_attraction_object.click_on_preview_and_verify_popup()

        find_media_by_attraction_object.click_on_add_all_to_pass()

        find_media_by_attraction_object.popup_added_to_guest_pass_verification()

        # Add video to cart
        opsui_guest_page.add_video_to_cart()

        opsui_guest_page.verify_video_added_to_cart()

        # add Entitlements of the selected media in cart
        opsui_guest_page.add_entitlements_all_cart_items()

        opsui_guest_page.add_entitlements_all_day_photos()

        opsui_guest_page.go_to_entitlements_page_from_guest_page()

        entitlements_guest_object = EntitlementsPage(driver)

        # Verified the ticket is video
        entitlements_guest_object.entitlements_page_opened_verification()

        entitlements_guest_object.verify_entitlement_added_to_guest(OpsuiAppParameters.get_ticket_type('video'),
                                                                    OpsuiAppStaticElements.ENTITLEMENT_PAGE_TYPE_TEXT_SECOND.value)

        entitlements_guest_object.verify_entitlement_added_to_guest(OpsuiAppParameters.get_ticket_type('all_photos'),
                                                                    OpsuiAppStaticElements.ENTITLEMENT_PAGE_TYPE_TEXT_FIRST.value)

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_back_to_preview_page()

        api_helpers_object.api_delete_userid_by_domain(email_user_id, type=DomainSetting.get_domain_type('domain_cart'))

        # request.config.testrail_reporter.capture_and_report_result(
        #     get_testrail_case_id(test_name),
        #     get_result_status(result=True))
    except:
        # request.config.testrail_reporter.capture_and_report_result(
        #     get_testrail_case_id(test_name),
        #     get_result_status(result=False))

        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        assert False
