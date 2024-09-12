from urllib import request

import allure
import pytest
from allure_commons.types import AttachmentType
import time

from assistance_helper_services import driver_related_actions
from assistance_helper_services.application_urls import ApplicationUrls
from assistance_helper_services.connector import Connector
from assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from page_objects.guest_app_po.billing_details_page import BillingDetails
from page_objects.guest_app_po.cart_page import CartPage
from page_objects.guest_app_po.payment_page import PaymentPage
from page_objects.guest_app_po.phone_page import PhonePage
from page_objects.guest_app_po.sms_page import SmsPage
from parameters.domain_settings import DomainSetting
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.parameters.guest_parameters import GuestParameters

guest_object = GuestParameters(media_prefix=None, user_id=None, phone=None)


@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=1)
@pytest.mark.usefixtures("driver", "application_parameters")
def test_add_photos_via_connector(driver, application_parameters):
    # get_media_path = "C:\\connector\\media-testing\\AV-TV-(Tatsu)\\single_photo"
    connector_object = Connector(application_parameters=application_parameters,
                                 connector_main_path=Connector.get_connector_main_path(),
                                 media_path="C:\\connector\\media-testing\\AV-XV-(X2-left)\\single_photo",
                                 uploads_path=Connector.get_uploads_path(Connector.get_connector_main_path()))

    connector_object.edit_config_file(type=DomainSetting.get_domain_type('non_cart_domain'))

    connector_object.drag_and_drop_media_to_uploads_folder()

    connector_object.run_connector()

phone_number = GuestParameters.get_login_backdoor_phone_payment()
@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=2)
@pytest.mark.usefixtures("driver", "application_parameters")
def test_cart_and_single_media(driver, application_parameters):
    test_name = "test_cart_and_single_media"
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

        new_cart_page_object = CartPage(driver)
        ###Tests:
        new_cart_page_object.add_first_and_second_media_to_cart()
        # new_cart_page_object.delete_item_from_cart_list()
        # new_cart_page_object.continue_shopping()
        # new_cart_page_object.add_third_media_to_cart()
        new_cart_page_object.proceed_to_payment()
        time.sleep(5)
        print("LALALALAL")

        billing_page_object = BillingDetails(driver)
        billing_page_object.billing_details_fill_in(phone_number, GuestParameters.get_country_name("Israel"))

        payment_page_object = PaymentPage(driver)
        payment_page_object.stripe_payment_process_with_credit_card()

        new_feed_page_object = FeedPage(driver)
        new_feed_page_object.go_to_feed()
        new_feed_page_object.verify_if_photo_with_watermark_or_not()

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

    # new_feed_page_object.verify_media_is_unwatermarked()

    #login to OPsUI and verify the payment type


@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=3)
@pytest.mark.usefixtures("driver", "application_parameters")
def test_cart_and_all_media(driver, application_parameters):
    #login
    new_feed_page_object = FeedPage(driver)
    new_feed_page_object.add_first_media_to_cart()
    new_feed_page_object.click_buy_now()
    new_feed_page_object.approve_special_offer()
    new_feed_page_object.delete_item_from_cart_list()
    #again
    new_feed_page_object.add_first_media_to_cart()
    new_feed_page_object.click_buy_now()
    new_feed_page_object.approve_special_offer()
    new_feed_page_object.finish_the_payment()
    new_feed_page_object.verify_all_media_is_unwatermarked()

    # login to OPsUI and verify the payment type


@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=4)
@pytest.mark.usefixtures("driver", "application_parameters")
def test_no_cart_all_media_google_pay(driver, application_parameters):
    #login
    new_feed_page_object = FeedPage(driver)
    new_feed_page_object.buy_all_media_button()
    new_feed_page_object.pay_with_google()
    new_feed_page_object.verify_all_media_is_unwatermarked()

    # login to OPsUI and verify the payment type


@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=5)
@pytest.mark.usefixtures("driver", "application_parameters")
#ui verificatio + apple pay sticy button + successful confirmation page
def test_ui_verification_and_success(driver, application_parameters):
    #login
    new_feed_page_object = FeedPage(driver)
    new_feed_page_object.add_first_media_to_cart()
    new_feed_page_object.click_apple_pay_sticky_button()
    new_feed_page_object.approve_special_offer()
    new_feed_page_object.finish_the_payment_with_ui_verification()
    # login to OPsUI and verify the payment type


@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=6)
@pytest.mark.usefixtures("driver", "application_parameters")
#ui verification + apple pay sticky button + payment is failed
def test_ui_verification_and_failed(driver, application_parameters):
    #login
    new_feed_page_object = FeedPage(driver)
    new_feed_page_object.add_first_media_to_cart()
    new_feed_page_object.click_apple_pay_sticky_button()
    new_feed_page_object.approve_special_offer()
    new_feed_page_object.finish_the_payment_with_failed()
    # login to OPsUI and verify the payment type


@pytest.mark.regression
# @pytest.mark.dev
@pytest.mark.run(order=7)
@pytest.mark.usefixtures("driver", "application_parameters")
#ui verification + apple pay sticky button + payment is with an error
def test_ui_verification_and_failed(driver, application_parameters):
    #login
    new_feed_page_object = FeedPage(driver)
    new_feed_page_object = FeedPage(driver)
    new_feed_page_object.add_first_media_to_cart()
    new_feed_page_object.click_apple_pay_sticky_button()
    new_feed_page_object.approve_special_offer()
    new_feed_page_object.finish_the_payment_with_error()
    # login to OPsUI and verify the payment type
