import time
import allure
import pytest
from allure_commons.types import AttachmentType

from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.parameters.domain_settings import DomainSetting
from src.assistance_helper_services import driver_related_actions
from src.assistance_helper_services.api_helpers import ApiHelpers
from src.assistance_helper_services.application_urls import ApplicationUrls
from src.page_objects.guest_app_po.add_media_page import AddMediaPage
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.phone_page import PhonePage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.parameters.guest_parameters import GuestParameters


@pytest.mark.usefixtures("driver", "application_parameters")
@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=1)
def test_wrong_media_number_blocked_after_6_times(request, driver, application_parameters):
    test_name = "test_wrong_media_number_blocked_after_6_times"
    try:
        #####
        # registration
        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        GuestParameters.get_login_backdoor_phone_wrong_media(), account_type= GuestParameters.get_account_type("app"))

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        time.sleep(2)

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        # phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone_wrong_media(), GuestParameters.get_country_code_without_plus_prefix("Israel"))

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

        add_media_object = AddMediaPage(driver)

        # This method call enter_photo_number() function or skipped_test() function
        skip_status = add_media_object.check_existence_of_media_number_button_and_associate(
            GuestParameters.get_photo_number(), application_parameters["attraction"])

        if skip_status == False:
            add_media_object.add_media_by_number_too_many_attempts_imitation(repeat=5)
            time.sleep(3)
            print("in false- after too many")
            add_media_object.verified_too_many_attempts_popup()
            print("in false- after verification")

            add_media_object.add_media_close_popup_too_many_attempts()
        else:
            pass

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

