# import time
# import allure
# import pytest
# from allure_commons.types import AttachmentType
#
# from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
# from src.assistance_helper_services import time_calculation
# from src.assistance_helper_services.connector import Connector
# from src.page_objects.guest_app_po.cart_page import CartPage
# from src.page_objects.guest_app_po.taxamo_page import TaxamoPage
# from src.parameters import email_parameters
# from src.parameters.domain_settings import DomainSetting
# from src.parameters.opsui_parameters import OpsuiAppParameters
# from src.parameters.domains import get_attraction_code
# from src.assistance_helper_services import driver_related_actions
# from src.assistance_helper_services.api_helpers import ApiHelpers
# from src.assistance_helper_services.application_urls import ApplicationUrls
# from src.page_objects.guest_app_po.feed_page import FeedPage
# from src.page_objects.guest_app_po.phone_page import PhonePage
# from src.parameters.guest_parameters import GuestParameters
# #
# #
# @pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
# @pytest.mark.dev
# @pytest.mark.run(order=1)
# def test_associate_photos_add_to_cart(request, driver, application_parameters):
#     test_name = "test_associate_photos_add_to_cart"
#     try:
#         connector_object = Connector(application_parameters=application_parameters,
#                                      connector_main_path=Connector.get_connector_main_path(),
#                                      media_path=Connector.get_video_path(Connector.get_connector_main_path()),
#                                      uploads_path=Connector.get_uploads_path(Connector.get_connector_main_path()))
#
#         connector_object.edit_config_file(type=DomainSetting.get_domain_type('domain_cart'))
#
#         connector_object.drag_and_drop_media_to_uploads_folder()
#
#         connector_object.run_connector()
#
#
#
#         ###### קריאה ליוזר של אוטומציה והוצאה איי די של היוזר
#         user_email = email_parameters.get_outlook_credentials("username")
#         print("user_email 1: " + str(user_email))
#
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         user_email, GuestParameters.get_account_type("app"))
#
#         get_user_id = api_helpers_object.api_get_userid_by_email_request(user_email, type=DomainSetting.get_domain_type(
#             'domain_cart'))
#         print("get_user_id 1: " + str(get_user_id))
#
#
#
#
#         # Delete user for clean user
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('domain_cart'))
#
#         new_user_email = email_parameters.get_outlook_credentials("username")
#
#         new_email_user_id = api_helpers_object.api_create_email_user_request(new_user_email,
#                                                                              GuestParameters.get_random_qr(),
#                                                                              type=DomainSetting.get_domain_type(
#                                                                                  'domain_cart'))
#         print("new_email_user_id 2: " + str(new_email_user_id))
#
#         # Calculate current GMT time, add buffer for : from, to
#         time_filter_values_for_get_media = time_calculation.media_testing_from_to_time_calculation_in_seconds(
#             application_parameters['from_to_api_time_buffer_seconds'])
#
#         list_of_media_ids = []
#
#         # GET, mediaId's of the server
#         media_id_output_data = api_helpers_object.api_get_media_id_by_date(
#             get_attraction_code(application_parameters['domain_cart']),
#             epoch_from_time=
#             time_filter_values_for_get_media[
#                 'from'],
#             epoch_to_time=time_filter_values_for_get_media[
#                 'to'],
#             list_of_media_ids=list_of_media_ids, type=DomainSetting.get_domain_type('domain_cart'))
#
#         print("Media IDs - Full list : " + str(list_of_media_ids))
#
#         api_helpers_object.api_post_associate_media_to_user_id(user_id=new_email_user_id,
#                                                                media_ids=list_of_media_ids,
#                                                                type=DomainSetting.get_domain_type(
#                                                                    'domain_cart'))
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         url = url_manager.return_url(ApplicationUrls.guestapp_cart)
#
#         driver.get(url)
#         time.sleep(5)
#
#         driver_related_actions.delete_cookies(driver)
#         time.sleep(5)
#         driver.get(url)
#
#         driver.refresh()
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.accept_cookies()
#
#         phone_page_object.register_with_gmail_address(email_parameters.get_outlook_credentials("username"),
#                                                       email_parameters.get_outlook_credentials("password"))
#
#         phone_page_object.accept_terms_and_conditions()
#
#         feed_page_object = FeedPage(driver)
#
#         feed_page_object.login_verification()
#
#         feed_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         feed_page_object.add_photo_to_cart()
#
#         cart_page_object = CartPage(driver)
#
#         cart_page_object.verify_all_media_added_to_cart(number_or_item_type_expected="2")
#
#         feed_page_object.logout()
#
#         phone_page_object.logout_verification()
#
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=True))
#
#     except:
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=False))
#
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         assert False
# #
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=2)
# def test_associate_videos_cart(request, driver, application_parameters):
#     test_name = "test_associate_videos_cart"
#     try:
#         connector_object = Connector(application_parameters=application_parameters,
#                                      connector_main_path=Connector.get_connector_main_path(),
#                                      media_path=Connector.get_video_path(Connector.get_connector_main_path()),
#                                      uploads_path=Connector.get_uploads_path(Connector.get_connector_main_path()))
#
#         connector_object.edit_config_file(type=DomainSetting.get_domain_type('domain_cart'))
#
#         connector_object.drag_and_drop_media_to_uploads_folder()
#
#         connector_object.run_connector()
#
#         user_email = email_parameters.get_outlook_credentials("username")
#         print("user_email 1: " + str(user_email))
#
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         user_email, GuestParameters.get_account_type("app"))
#
#         get_user_id = api_helpers_object.api_get_userid_by_email_request(user_email, type=DomainSetting.get_domain_type(
#             'domain_cart'))
#         print("get_user_id 1: " + str(get_user_id))
#
#         # Delete user for clean user
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('domain_cart'))
#
#         new_user_email = email_parameters.get_outlook_credentials("username")
#
#         new_email_user_id = api_helpers_object.api_create_email_user_request(new_user_email,
#                                                                              GuestParameters.get_random_qr(),
#                                                                              type=DomainSetting.get_domain_type(
#                                                                                  'domain_cart'))
#         print("new_email_user_id 2: " + str(new_email_user_id))
#
#         # Calculate current GMT time, add buffer for : from, to
#         time_filter_values_for_get_media = time_calculation.media_testing_from_to_time_calculation_in_seconds(
#             application_parameters['from_to_api_time_buffer_seconds'])
#
#         list_of_media_ids = []
#
#         # GET, mediaId's of the server
#         media_id_output_data = api_helpers_object.api_get_media_id_by_date(
#             get_attraction_code(application_parameters['domain_cart']),
#             epoch_from_time=
#             time_filter_values_for_get_media[
#                 'from'],
#             epoch_to_time=time_filter_values_for_get_media[
#                 'to'],
#             list_of_media_ids=list_of_media_ids, type=DomainSetting.get_domain_type('domain_cart'))
#
#         print("Media IDs - Full list : " + str(list_of_media_ids))
#
#         api_helpers_object.api_post_associate_media_to_user_id(user_id=new_email_user_id,
#                                                                media_ids=list_of_media_ids,
#                                                                type=DomainSetting.get_domain_type(
#                                                                    'domain_cart'))
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         url = url_manager.return_url(ApplicationUrls.guestapp_cart)
#         print("url: " + str(url))
#
#         driver.get(url)
#
#         driver.refresh()
#
#         driver_related_actions.delete_cookies(driver)
#
#         driver.refresh()
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.accept_cookies()
#
#         phone_page_object.register_with_gmail_address(email_parameters.get_outlook_credentials("username"),
#                                                       email_parameters.get_outlook_credentials("password"))
#
#         phone_page_object.accept_terms_and_conditions()
#
#         feed_page_object = FeedPage(driver)
#
#         feed_page_object.login_verification()
#
#         feed_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         feed_page_object.add_first_video_to_cart()
#
#         cart_page_object = CartPage(driver)
#
#         cart_page_object.verify_all_media_added_to_cart(
#             number_or_item_type_expected=OpsuiAppParameters.get_ticket_type('video'))
#
#         feed_page_object.logout()
#
#         phone_page_object.logout_verification()
#
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=True))
#
#     except:
#
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=False))
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#         assert False
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=3)
# def test_payment_for_photo_cart(request, driver, application_parameters):
#     test_name = "test_payment_for_photo_cart"
#     try:
#         connector_object = Connector(application_parameters=application_parameters,
#                                      connector_main_path=Connector.get_connector_main_path(),
#                                      media_path=Connector.get_video_path(Connector.get_connector_main_path()),
#                                      uploads_path=Connector.get_uploads_path(Connector.get_connector_main_path()))
#
#         connector_object.edit_config_file(type=DomainSetting.get_domain_type('domain_cart'))
#
#         connector_object.drag_and_drop_media_to_uploads_folder()
#
#         connector_object.run_connector()
#
#         user_email = email_parameters.get_outlook_credentials("username")
#         print("user_email 1: " + str(user_email))
#
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         user_email, GuestParameters.get_account_type("app"))
#
#         get_user_id = api_helpers_object.api_get_userid_by_email_request(user_email, type=DomainSetting.get_domain_type(
#             'domain_cart'))
#         print("get_user_id 1: " + str(get_user_id))
#
#         # Delete user for clean user
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('domain_cart'))
#
#         new_user_email = email_parameters.get_outlook_credentials("username")
#
#         new_email_user_id = api_helpers_object.api_create_email_user_request(new_user_email,
#                                                                              GuestParameters.get_random_qr(),
#                                                                              type=DomainSetting.get_domain_type(
#                                                                                  'domain_cart'))
#
#         # Calculate current GMT time, add buffer for : from, to
#         time_filter_values_for_get_media = time_calculation.media_testing_from_to_time_calculation_in_seconds(
#             application_parameters['from_to_api_time_buffer_seconds'])
#
#         list_of_media_ids = []
#
#         # GET, mediaId's of the server
#         media_id_output_data = api_helpers_object.api_get_media_id_by_date(
#             get_attraction_code(application_parameters['domain_cart']),
#             epoch_from_time=
#             time_filter_values_for_get_media[
#                 'from'],
#             epoch_to_time=time_filter_values_for_get_media[
#                 'to'],
#             list_of_media_ids=list_of_media_ids, type=DomainSetting.get_domain_type('domain_cart'))
#
#         print("Media IDs - Full list : " + str(list_of_media_ids))
#
#         api_helpers_object.api_post_associate_media_to_user_id(user_id=new_email_user_id,
#                                                                media_ids=list_of_media_ids,
#                                                                type=DomainSetting.get_domain_type(
#                                                                    'domain_cart'))
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         url = url_manager.return_url(ApplicationUrls.guestapp_cart)
#         print("url: " + str(url))
#
#         driver.get(url)
#
#         driver_related_actions.delete_cookies(driver)
#
#         driver.refresh()
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.accept_cookies()
#
#         phone_page_object.register_with_gmail_address(email_parameters.get_outlook_credentials("username"),
#                                                       email_parameters.get_outlook_credentials("password"))
#
#         feed_page_object = FeedPage(driver)
#
#         feed_page_object.login_verification()
#
#         feed_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         feed_page_object.add_photo_to_cart()
#
#         cart_page_object = CartPage(driver)
#
#         cart_page_object.verify_all_media_added_to_cart(number_or_item_type_expected="2")
#
        # cart_page_object.proceed_to_payment()
#
#         taxamo_page_object = TaxamoPage(driver)
#
#         taxamo_page_object.payment_process_for_media_with_credit_card()
#
#         feed_page_object.verify_payment_success()
#
#         feed_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=False)
#
#         feed_page_object.logout()
#
#         phone_page_object.logout_verification()
#
#         # request.config.testrail_reporter.capture_and_report_result(
#         #     get_testrail_case_id(test_name),
#         #     get_result_status(result=True))
#
#     except:
#
#         # request.config.testrail_reporter.capture_and_report_result(
#         #     get_testrail_case_id(test_name),
#         #     get_result_status(result=False))
#
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#         assert False
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# # @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=1)
# def test_landing_qr_page_cart(driver, application_parameters):
#     pass
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# # @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=1)
# def test_share_and_download_button_cart(driver, application_parameters):
#     pass
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# # @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=1)
# def test_popup_recommendation_cart(driver, application_parameters):
#     pass
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# # @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=1)
# def test_review_cart_page_cart(driver, application_parameters):
#     pass
