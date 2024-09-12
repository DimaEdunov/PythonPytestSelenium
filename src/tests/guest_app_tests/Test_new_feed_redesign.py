import allure
import pytest
from allure_commons.types import AttachmentType
import time

from assistance_helper_services.application_urls import ApplicationUrls
from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.assistance_helper_services import driver_related_actions
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.phone_page import PhonePage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.parameters.angela_parameters import get_park_full_name
from src.parameters.guest_parameters import GuestParameters


guest_object = GuestParameters(media_prefix=None, user_id=None, phone=None)


# @pytest.mark.dev
@pytest.mark.run(order=1)
@pytest.mark.usefixtures("driver", "application_parameters")
def test_elements_verification(request, driver, application_parameters):
    test_name = "test_new_feed_elements_verification_including_UI_and_Mixpanel"

    ##[login]
    try:

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))
        # driver.get("https://photos-se1.pomvom.com/av")

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()
        time.sleep(5)

        phone_page_object.insert_phone_number_with_unpaid_media(
                                            GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        # Login Verification
        home_page_object.login_verification()
        #####
        # end of registration steps

        new_feed_page_object = FeedPage(driver)
        #UI:
        new_feed_page_object.ui_logo_verification()
        new_feed_page_object.ui_special_banner_verification()
        new_feed_page_object.ui_attraction_name_verification()
        new_feed_page_object.ui_attraction_location_verification()
        new_feed_page_object.ui_two_media_in_the_row()
        # new_feed_page_object.ui_media_tag_verification()
        new_feed_page_object.ui_three_dots_button_verification()
        # func:
        new_feed_page_object.one_media_in_row()

        new_feed_page_object.heart_on_button_verification_functionality()
        heart_status = new_feed_page_object.verify_heart_on_off_status()
        print(f"Heart status is: {heart_status}")

        new_feed_page_object.heart_off_button_verification_functionality()
        heart_status = new_feed_page_object.verify_heart_on_off_status()
        print(f"Heart status is: {heart_status}")

        new_feed_page_object.no_event_heart_button_verification_functionality()

        # new_feed_page_object.tags_verification_functionality()

        new_feed_page_object.three_dots_info_functionality()

        initial_media_count = new_feed_page_object.three_dots_delete_content()
        new_feed_page_object.count_media_after_delete_action(initial_media_count)

        initial_media_count = new_feed_page_object.three_dots_report_content()
        new_feed_page_object.count_media_after_report_content_action(initial_media_count)

        initial_media_count = new_feed_page_object.three_dots_not_my_content()
        new_feed_page_object.count_media_after_not_my_content_action(initial_media_count)

              # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()
                # - End of log out
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
                    assign_test_result(result=True))
    except:
        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=False))

        home_page_object = FeedPage(driver)
        phone_page_object = PhonePage(driver)

        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()

        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                        attachment_type=AttachmentType.PNG)
        assert False




# @pytest.mark.dev
@pytest.mark.run(order=2)
@pytest.mark.usefixtures("driver", "application_parameters")
def test_unpaid_media_ui_and_mix_panel_popup(request, driver, application_parameters):
    test_name = "test_unpaid_media_ui_and_mix_panel_popup"

    ##[login]
    try:

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))
        # driver.get("https://photos-se1.pomvom.com/av")

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()
        time.sleep(5)

        phone_page_object.insert_phone_number_with_unpaid_media(
                                            GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        # Login Verification
        home_page_object.login_verification()
        #####
        # end of registration steps

        new_feed_page_object = FeedPage(driver)


        new_feed_page_object.popup_heart_on_off_button_verification()
        new_feed_page_object.popup_three_dots_info()
        new_feed_page_object.popup_three_dots_delete_content()
        new_feed_page_object.popup_three_dots_report_content()
        new_feed_page_object.popup_three_dots_not_my_content()

              # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()
                # - End of log out
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
                    assign_test_result(result=True))
    except:
        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=False))

        home_page_object = FeedPage(driver)
        phone_page_object = PhonePage(driver)

        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()

        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                        attachment_type=AttachmentType.PNG)
        assert False




# @pytest.mark.dev
@pytest.mark.run(order=3)
@pytest.mark.usefixtures("driver", "application_parameters")
def test_paid_media_ui_and_mix_panel_feed(request, driver, application_parameters):
    test_name = "test_paid_media_ui_and_mix_panel_feed"

    ##[login]
    try:

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))
        # driver.get("https://photos-se1.pomvom.com/av")

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()
        time.sleep(5)

        phone_page_object.insert_phone_number_with_paid_media(
            GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        # Login Verification
        home_page_object.login_verification()
        #####
        # end of registration steps

        new_feed_page_object = FeedPage(driver)

        new_feed_page_object.ui_logo_verification()
        new_feed_page_object.ui_special_banner_after_payment()
        new_feed_page_object.ui_attraction_name_verification()
        new_feed_page_object.ui_attraction_location_verification()
        new_feed_page_object.ui_two_media_in_the_row()
        new_feed_page_object.one_media_in_row()
        # new_feed_page_object.ui_heart_button_verification()
        new_feed_page_object.ui_three_dots_button_verification()
        new_feed_page_object.download_button_verification()
        new_feed_page_object.share_button_verification()
        new_feed_page_object.download_all_button_verification()

        ### like / download / share button func + mixpanel
        new_feed_page_object.download_all_button_functionality()
        new_feed_page_object.download_button_functionality()
        new_feed_page_object.heart_on_button_verification_functionality()
        new_feed_page_object.verify_heart_on_off_status()
        new_feed_page_object.heart_off_button_verification_functionality()
        new_feed_page_object.verify_heart_on_off_status()
        new_feed_page_object.no_event_heart_button_verification_functionality()

        ####three dots functionality includind the mixpanel events: done
        initial_media_count = new_feed_page_object.three_dots_delete_content()
        new_feed_page_object.count_media_after_delete_action(initial_media_count)

        initial_media_count = new_feed_page_object.three_dots_report_content()
        new_feed_page_object.count_media_after_report_content_action(initial_media_count)

        initial_media_count = new_feed_page_object.three_dots_not_my_content()
        new_feed_page_object.count_media_after_not_my_content_action(initial_media_count)
        new_feed_page_object.share_button_functionality()
        driver.refresh()

        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()
        # - End of log out
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=True))
    except:
        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=False))

        home_page_object = FeedPage(driver)
        phone_page_object = PhonePage(driver)

        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()

        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        assert False


@pytest.mark.dev
@pytest.mark.run(order=4)
@pytest.mark.usefixtures("driver", "application_parameters")
def test_paid_media_ui_and_mix_panel_popup(request, driver, application_parameters):
    test_name = "test_paid_media_ui_and_mix_panel_popup"

    ##[login]
    try:

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))
        # driver.get("https://photos-se1.pomvom.com/av")

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()
        time.sleep(5)

        phone_page_object.insert_phone_number_with_paid_media(
            GuestParameters.get_country_code_without_plus_prefix("Israel"))

        phone_page_object.submit_login_process()

        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        # Login Verification
        home_page_object.login_verification()
        #####
        # end of registration steps

        new_feed_page_object = FeedPage(driver)
        # new_feed_page_object.popup_download_button_verification()
        # new_feed_page_object.paid_media_popup_heart_on_off_button_verification()
        # new_feed_page_object.popup_no_event_heart_button_verification()
        # new_feed_page_object.paid_media_popup_three_dots_info()
        # new_feed_page_object.paid_media_popup_three_dots_delete_content()
        # new_feed_page_object.popup_three_dots_report_content()
        # new_feed_page_object.popup_three_dots_not_my_content()
        new_feed_page_object.popup_share_button_verification()


        # Refresh the page


        # Simulate pressing the Escape key

        time.sleep(15)





        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()
        # - End of log out
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=True))
    except:
        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        request.config.testrail_reporter.capture_and_report_result(
            get_case_id_by_automation_test_name(test_name),
            assign_test_result(result=False))

        home_page_object = FeedPage(driver)
        phone_page_object = PhonePage(driver)

        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()

        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)
        assert False

