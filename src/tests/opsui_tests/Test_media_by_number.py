import allure
import pytest
from allure_commons.types import AttachmentType

from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.parameters.domain_settings import DomainSetting
from src.assistance_helper_services import driver_related_actions, application_helpers
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from src.elements.ops_ui.dynamic_elemenets.opsui_dynamic_elements_picklists import OpsuiDynamicElementsPicklists
from src.page_objects.guest_app_po.account_settings_page import AccountSettingsPage
from src.page_objects.guest_app_po.add_media_page import AddMediaPage
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.phone_page import PhonePage
from src.page_objects.guest_app_po.side_menu_page import SideMenuPage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.page_objects.opsui_app_po.search_guest_page import SearchGuestPage
from src.parameters.side_menu_parameters import SideMenuParameters
from src.assistance_helper_services.api_helpers import ApiHelpers
from src.page_objects.opsui_app_po.global_guest_search_opsui import GlobalGuestSearchOpsui
from src.parameters.opsui_parameters import OpsuiAppParameters
from src.assistance_helper_services.connector import Connector
from src.page_objects.opsui_app_po.find_media_by_attraction_page import FindMediaByAttractionPage
from src.page_objects.opsui_app_po.global_opsui_actions import GlobalOpsuiActions
from src.assistance_helper_services.application_urls import ApplicationUrls
from src.page_objects.opsui_app_po.home_page import OpsuiHomePage
from src.page_objects.opsui_app_po.search_by_number_page import OpsUISearchByNumber
from src.parameters.guest_parameters import GuestParameters


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=1)
def test_add_photos_via_connector(driver, application_parameters):
    connector_object = Connector(application_parameters=application_parameters,
                                 connector_main_path=Connector.get_connector_main_path(),
                                 media_path=Connector.get_media_path(Connector.get_connector_main_path()),
                                 uploads_path=Connector.get_uploads_path(Connector.get_connector_main_path()))

    connector_object.edit_config_file(type=DomainSetting.get_domain_type('non_cart_domain'))

    connector_object.drag_and_drop_media_to_uploads_folder()

    connector_object.run_connector()


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=2)
def test_find_media_by_number_negative(request, driver, application_parameters):
    test_name = "test_find_media_by_number_negative"
    try:
        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_number)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        search_by_number_screen = OpsUISearchByNumber(driver)

        api_helpers_object = ApiHelpers(application_parameters, key=None,
                                        phone_or_qr=None,
                                        account_type=GuestParameters.get_account_type("qr"))

        full_attraction_name = api_helpers_object.api_get_attraction_name_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        search_by_number_screen.search_media_by_number(GuestParameters.get_photo_number(), full_attraction_name)

        search_by_number_screen.search_media_negative_verification()
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
def test_find_media_by_number_print(request, driver, application_parameters):
    test_name = "test_find_media_by_number_print"
    try:
        url_manager = ApplicationUrls(application_parameters)
        url = url_manager.return_url(ApplicationUrls.opsui)
        url_manager.enter_url_in_address_bar(url)

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_attraction)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_attraction_object = FindMediaByAttractionPage(driver)

        find_media_by_attraction_object.find_media_by_attraction_page_opened_verification()

        find_media_by_attraction_object.search_photos()

        global_opsui_actions = GlobalOpsuiActions(driver)

        global_opsui_actions.open_photo_details()

        find_media_by_attraction_object.print_photo()

        find_media_by_attraction_object.print_photo_popup_verification()

        find_media_by_attraction_object.close_photo_popup_and_photo_details()

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
# @pytest.mark.dev
@pytest.mark.run(order=4)
def test_media_by_number_search_a_non_existing_guest_by_qr(request, driver, application_parameters):
    test_name = "test_media_by_number_search_a_non_existing_guest_by_qr"
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
                                                                                 OpsuiAppParameters.find_media_by_attraction)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_attraction_object = FindMediaByAttractionPage(driver)

        find_media_by_attraction_object.find_media_by_attraction_page_opened_verification()

        find_media_by_attraction_object.search_photos()

        photo_number = find_media_by_attraction_object.get_photo_number()

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_number)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_number_object = OpsUISearchByNumber(driver)

        api_helpers_object = ApiHelpers(application_parameters, key=None,
                                        phone_or_qr=None,
                                        account_type=GuestParameters.get_account_type("qr"))

        full_attraction_name = api_helpers_object.api_get_attraction_name_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        find_media_by_number_object.search_media_by_number(photo_number, full_attraction_name)

        global_opsui_actions = GlobalOpsuiActions(driver)

        global_opsui_actions.add_photo_to_guest()

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(qr_number)

        opsui_global_search_object.click_on_submit()

        opsui_global_search_object.click_on_create()

        global_opsui_actions.verify_add_photo_to_guest()

        qr_user_id = global_opsui_actions.get_guest_id()

        api_helpers_object = ApiHelpers(application_parameters, key = None,
                                        phone_or_qr= None,
                                        account_type=GuestParameters.get_account_type("qr"))

        api_helpers_object.api_delete_userid_request(qr_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

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
# @pytest.mark.dev
@pytest.mark.run(order=5)
def test_media_by_number_search_an_existing_guest_by_qr(request, driver, application_parameters):
    test_name = "test_media_by_number_search_an_existing_guest_by_qr"
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
                                                                                 OpsuiAppParameters.find_media_by_attraction)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_attraction_object = FindMediaByAttractionPage(driver)

        find_media_by_attraction_object.find_media_by_attraction_page_opened_verification()

        find_media_by_attraction_object.search_photos()

        photo_number = find_media_by_attraction_object.get_photo_number()

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_number)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_number_object = OpsUISearchByNumber(driver)

        full_attraction_name = api_helpers_object.api_get_attraction_name_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        find_media_by_number_object.search_media_by_number(photo_number, full_attraction_name)

        global_opsui_actions = GlobalOpsuiActions(driver)

        global_opsui_actions.add_photo_to_guest()

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(existing_qr)

        opsui_global_search_object.click_on_submit()

        global_opsui_actions.verify_add_photo_to_guest()

        qr_user_id = global_opsui_actions.get_guest_id()

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        api_helpers_object = ApiHelpers(application_parameters, key=None,
                                        phone_or_qr=None,
                                        account_type=GuestParameters.get_account_type("qr"))

        api_helpers_object.api_delete_userid_request(qr_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))
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
@pytest.mark.run(order=6)
def test_media_by_number_search_a_non_existing_guest_by_phone(request, driver, application_parameters):
    test_name = "test_media_by_number_search_a_non_existing_guest_by_phone"
    try:
        used_phone_number = GuestParameters.get_random_backdoor_phone()

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        used_phone_number, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

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
                                                                                 OpsuiAppParameters.find_media_by_attraction)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_attraction_object = FindMediaByAttractionPage(driver)

        find_media_by_attraction_object.find_media_by_attraction_page_opened_verification()

        find_media_by_attraction_object.search_photos()

        photo_number = find_media_by_attraction_object.get_photo_number()

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_number)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_number_object = OpsUISearchByNumber(driver)

        full_attraction_name = api_helpers_object.api_get_attraction_name_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        find_media_by_number_object.search_media_by_number(photo_number, full_attraction_name)

        global_opsui_actions = GlobalOpsuiActions(driver)

        global_opsui_actions.add_photo_to_guest()

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_guest_phone(GuestParameters.get_country_code_without_plus_prefix("Israel"),
                                                    used_phone_number)

        opsui_global_search_object.click_on_submit()

        opsui_global_search_object.click_on_create()

        global_opsui_actions.verify_add_photo_to_guest()

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
# @pytest.mark.dev
@pytest.mark.run(order=7)
def test_media_by_number_search_a_non_existing_guest_by_guest_id(request, driver, application_parameters):
    test_name = "test_media_by_number_search_a_non_existing_guest_by_guest_id"
    try:
        user_phone_number = GuestParameters.get_random_backdoor_phone()

        ######
        # Registration to app & login
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        user_phone_number, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.insert_phone_number_and_country_code(user_phone_number, GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.accept_cookies()

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

        get_user_id = add_media.get_userId_number()

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

        find_media_by_attraction_object = FindMediaByAttractionPage(driver)

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_attraction)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_attraction_object.find_media_by_attraction_page_opened_verification()

        find_media_by_attraction_object.search_photos()

        photo_number = find_media_by_attraction_object.get_photo_number()

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_number)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_number_object = OpsUISearchByNumber(driver)

        full_attraction_name = api_helpers_object.api_get_attraction_name_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        find_media_by_number_object.search_media_by_number(photo_number, full_attraction_name)

        global_opsui_actions = GlobalOpsuiActions(driver)

        global_opsui_actions.add_photo_to_guest()

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(get_user_id)

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
# @pytest.mark.dev
@pytest.mark.run(order=8)
def test_media_by_number_search_an_existing_guest_by_guest_id(request, driver, application_parameters):
    test_name = "test_media_by_number_search_an_existing_guest_by_guest_id"
    try:
        user_phone_number = GuestParameters.get_random_backdoor_phone()

        ######
        # Registration to app & login
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        user_phone_number, GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.insert_phone_number_and_country_code(user_phone_number, GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.accept_cookies()

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

        get_user_id = add_media.get_userId_number()

        ########
        #### - Navigate to OpsUI & Login
        driver_related_actions.open_and_switch_to_new_url_in_new_window(driver,
                                                                        url_manager.return_url(ApplicationUrls.opsui))

        opsui_home_page = OpsuiHomePage(driver)

        opsui_home_page.opsui_login()

        opsui_home_page.login_verification()

        ########
        #### - End of - Navigate to OpsUI & Login

        find_media_by_attraction_object = FindMediaByAttractionPage(driver)

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_attraction)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_attraction_object.find_media_by_attraction_page_opened_verification()

        find_media_by_attraction_object.search_photos()

        photo_number = find_media_by_attraction_object.get_photo_number()

        global_opsui_actions = GlobalOpsuiActions(driver)
        global_opsui_actions.go_to_home_page()

        feature_text_in_selected_park = application_helpers.opsui_choose_feature(application_parameters["domain"],
                                                                                 OpsuiAppParameters.find_media_by_number)

        OpsuiDynamicElementsPicklists.opsui_go_to_feature(driver, feature_text_in_selected_park)

        find_media_by_number_object = OpsUISearchByNumber(driver)

        full_attraction_name = api_helpers_object.api_get_attraction_name_request(type=DomainSetting.get_domain_type('non_cart_domain'))

        find_media_by_number_object.search_media_by_number(photo_number, full_attraction_name)

        global_opsui_actions = GlobalOpsuiActions(driver)

        global_opsui_actions.add_photo_to_guest()

        opsui_global_search_object = GlobalGuestSearchOpsui(driver)

        opsui_global_search_object.type_qr_or_userid(get_user_id)

        opsui_global_search_object.click_on_submit()

        global_opsui_actions.verify_add_photo_to_guest()

        global_opsui_actions.go_to_home_page()

        # go to guest app tab
        driver_related_actions.switch_to_default_window(driver)

        # go to home page and refresh
        guest_app_side_menu_object = SideMenuPage(driver)

        guest_app_side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        guest_app_side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Home"))

        driver.refresh()

        home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)

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