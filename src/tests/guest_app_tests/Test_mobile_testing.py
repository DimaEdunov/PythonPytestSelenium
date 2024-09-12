import time
import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from src.page_objects.guest_app_po.side_menu_page import SideMenuPage
from src.parameters.side_menu_parameters import SideMenuParameters
from src.page_objects.guest_app_po.mobile_guest_app_page import MobileGuestAppPage
from src.assistance_helper_services import driver_related_actions
from src.assistance_helper_services.application_urls import ApplicationUrls
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.parameters.guest_parameters import GuestParameters
from src.page_objects.guest_app_po.phone_page import PhonePage


@pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
@pytest.mark.run(order=1)
def test_positive_mobile_login(mobile_driver, application_parameters):
    try:
        driver_related_actions.delete_cookies(mobile_driver)

        url_manager = ApplicationUrls(application_parameters)

        mobile_driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(mobile_driver)

        phone_page_object.accept_terms_and_conditions()

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone(), GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(mobile_driver)
        sms_page_object.sms_verification()

        # Login Verification
        mobile_guest_app_object = MobileGuestAppPage(mobile_driver)
        mobile_guest_app_object.mobile_login_verification()

        # Logout & Logout verification
        mobile_guest_app_object.mobile_logout()

        phone_page_object = PhonePage(mobile_driver)
        phone_page_object.logout_verification()

    except:
        allure.attach(mobile_driver.get_screenshot_as_png(), name="test_positive_login",
                      attachment_type=AttachmentType.PNG)
        assert False


@pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
@pytest.mark.run(order=2)
def test_mobile_side_menu(mobile_driver, application_parameters):
    try:
        driver_related_actions.delete_cookies(mobile_driver)

        url_manager = ApplicationUrls(application_parameters)

        mobile_driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(mobile_driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone(), GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.submit_login_process()

        phone_page_object.accept_terms_and_conditions()
        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(mobile_driver)
        sms_page_object.sms_verification()

        # Login Verification
        mobile_guest_app_object = MobileGuestAppPage(mobile_driver)
        mobile_guest_app_object.mobile_login_verification()

        # Assure every item on the side menu exists and leads to the correct url
        side_menu_object = SideMenuPage(mobile_driver)
        # side_menu_object.go_to(WebGuestAppStaticElements.HOME_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Home"))

        mobile_guest_app_object.click_on_hamburger_or_back_sign()

        side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))

        mobile_guest_app_object.click_on_hamburger_or_back_sign()

        side_menu_object.go_to(WebGuestAppStaticElements.ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Account setting"))

        mobile_guest_app_object.click_on_hamburger_or_back_sign()

        side_menu_object.go_to(WebGuestAppStaticElements.HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Help and support"))

        mobile_guest_app_object.click_on_hamburger_or_back_sign()

        side_menu_object.go_to(WebGuestAppStaticElements.TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Terms and conditions"))

        mobile_guest_app_object.click_on_hamburger_or_back_sign()

        side_menu_object.go_to(WebGuestAppStaticElements.PRIVACY_POLICY_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Privacy policy"))

        # logout
        mobile_guest_app_object.mobile_logout()

        phone_page_object = PhonePage(mobile_driver)
        phone_page_object.logout_verification()


    except:
        allure.attach(mobile_driver.get_screenshot_as_png(), name="test_mobile_side_menu",
                      attachment_type=AttachmentType.PNG)
        assert False