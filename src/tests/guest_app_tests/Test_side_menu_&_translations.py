import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.assistance_helper_services import driver_related_actions
from src.assistance_helper_services.application_urls import ApplicationUrls
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from src.page_objects.guest_app_po.account_settings_page import AccountSettingsPage
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.phone_page import PhonePage
from src.page_objects.guest_app_po.side_menu_page import SideMenuPage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.parameters.domain_settings import DomainSetting
from src.parameters.guest_parameters import GuestParameters
from src.parameters.side_menu_parameters import SideMenuParameters


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
@pytest.mark.run(order=1)
def test_side_menu_items(request, driver, application_parameters):
    test_name = "test_side_menu_items"
    try:
        side_menu_object = SideMenuPage(driver)

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

        # Assure every item on the side menu exists and leads to the correct url

        side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Home"))

        side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))

        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Account setting"))

        side_menu_object.go_to(WebGuestAppStaticElements.HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Help and support"))

        side_menu_object.go_to(WebGuestAppStaticElements.TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Terms and conditions"))

        side_menu_object.go_to(WebGuestAppStaticElements.PRIVACY_POLICY_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Privacy policy"))

        # logout
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
@pytest.mark.run(order=2)
def test_translation(request, driver, application_parameters):
    test_name = "test_translation"
    try:
        side_menu_object = SideMenuPage(driver)
        account_settings_object = AccountSettingsPage(driver)

        # Log in to Guest App

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

        # Change language and assure every tab is translated

        # - Portuguese
        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        account_settings_object.change_language(DomainSetting.get_languages("Portuguese"))

        side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Portuguese"),
                                                     SideMenuParameters.get_url_verification_string("Home"))

        side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Portuguese"),
                                                     SideMenuParameters.get_url_verification_string("Add media"))

        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Portuguese"),
                                                     SideMenuParameters.get_url_verification_string("Account setting"))

        side_menu_object.go_to(WebGuestAppStaticElements.HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Portuguese"),
                                                     SideMenuParameters.get_url_verification_string("Help and support"))

        side_menu_object.go_to(WebGuestAppStaticElements.TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Portuguese"),
                                                     SideMenuParameters.
                                                     get_url_verification_string("Terms and conditions"))

        side_menu_object.go_to(WebGuestAppStaticElements.PRIVACY_POLICY_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Portuguese"),
                                                     SideMenuParameters.get_url_verification_string("Privacy policy"))

        # - German
        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        account_settings_object.change_language(DomainSetting.get_languages("German"))

        side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("German"),
                                                     SideMenuParameters.get_url_verification_string("Home"))

        side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("German"),
                                                     SideMenuParameters.get_url_verification_string("Add media"))

        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("German"),
                                                     SideMenuParameters.get_url_verification_string("Account setting"))

        side_menu_object.go_to(WebGuestAppStaticElements.HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("German"),
                                                     SideMenuParameters.get_url_verification_string("Help and support"))

        side_menu_object.go_to(WebGuestAppStaticElements.TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("German"),
                                                     SideMenuParameters.
                                                     get_url_verification_string("Terms and conditions"))

        side_menu_object.go_to(WebGuestAppStaticElements.PRIVACY_POLICY_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("German"),
                                                     SideMenuParameters.get_url_verification_string("Privacy policy"))

        # - Spanish
        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        account_settings_object.change_language(DomainSetting.get_languages("Spanish"))

        side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Spanish"),
                                                     SideMenuParameters.get_url_verification_string("Home"))

        side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Spanish"),
                                                     SideMenuParameters.get_url_verification_string("Add media"))

        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Spanish"),
                                                     SideMenuParameters.get_url_verification_string("Account setting"))

        side_menu_object.go_to(WebGuestAppStaticElements.HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Spanish"),
                                                     SideMenuParameters.get_url_verification_string("Help and support"))

        side_menu_object.go_to(WebGuestAppStaticElements.TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Spanish"),
                                                     SideMenuParameters.
                                                     get_url_verification_string("Terms and conditions"))

        side_menu_object.go_to(WebGuestAppStaticElements.PRIVACY_POLICY_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Spanish"),
                                                     SideMenuParameters.get_url_verification_string("Privacy policy"))

        # - Polish
        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        account_settings_object.change_language(DomainSetting.get_languages("Polish"))

        side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Polish"),
                                                     SideMenuParameters.get_url_verification_string("Home"))

        side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Polish"),
                                                     SideMenuParameters.get_url_verification_string("Add media"))

        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Polish"),
                                                     SideMenuParameters.get_url_verification_string("Account setting"))

        side_menu_object.go_to(WebGuestAppStaticElements.HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Polish"),
                                                     SideMenuParameters.get_url_verification_string("Help and support"))

        side_menu_object.go_to(WebGuestAppStaticElements.TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Polish"),
                                                     SideMenuParameters.
                                                     get_url_verification_string("Terms and conditions"))

        side_menu_object.go_to(WebGuestAppStaticElements.PRIVACY_POLICY_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("Polish"),
                                                     SideMenuParameters.get_url_verification_string("Privacy policy"))

        # - English
        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        account_settings_object.change_language(DomainSetting.get_languages("English"))

        side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("English"),
                                                     SideMenuParameters.get_url_verification_string("Home"))

        side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("English"),
                                                     SideMenuParameters.get_url_verification_string("Add media"))

        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("English"),
                                                     SideMenuParameters.get_url_verification_string("Account setting"))

        side_menu_object.go_to(WebGuestAppStaticElements.HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("English"),
                                                     SideMenuParameters.get_url_verification_string("Help and support"))

        side_menu_object.go_to(WebGuestAppStaticElements.TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("English"),
                                                     SideMenuParameters.
                                                     get_url_verification_string("Terms and conditions"))

        side_menu_object.go_to(WebGuestAppStaticElements.PRIVACY_POLICY_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_language_verification(DomainSetting.get_languages("English"),
                                                     SideMenuParameters.get_url_verification_string("Privacy policy"))

        # logout
        home_page_object = FeedPage(driver)

        home_page_object.logout()

        phone_page_object = PhonePage(driver)
        phone_page_object.logout_verification()

    except:
        allure.attach(driver.get_screenshot_as_png(), name="test_translation", attachment_type=AttachmentType.PNG)
        assert False
