import allure
import pytest
from allure_commons.types import AttachmentType

from src.assistance_helper_services.test_rail_helpers import get_case_id_by_automation_test_name, assign_test_result
from src.page_objects.guest_app_po.billing_details_page import BillingDetails
from src.page_objects.guest_app_po.payment_page import PaymentPage
from src.parameters.domain_settings import DomainSetting
from src.parameters.side_menu_parameters import SideMenuParameters
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from src.page_objects.guest_app_po.side_menu_page import SideMenuPage
from src.parameters.angela_parameters import get_angela_page_name
from src.assistance_helper_services import driver_related_actions
from src.assistance_helper_services.api_helpers import ApiHelpers
from src.assistance_helper_services.application_urls import ApplicationUrls
from src.assistance_helper_services.connector import Connector
from src.page_objects.angela_po.customer_information_page import CustomerInformationPage
from src.page_objects.angela_po.customer_media_page import CustomerMediaPage
from src.page_objects.angela_po.menu_page import MenuPage
from src.page_objects.angela_po.search_customer_page import SearchCustomerPage
from src.page_objects.guest_app_po.add_media_page import AddMediaPage
from src.page_objects.guest_app_po.feed_page import FeedPage
from src.page_objects.guest_app_po.phone_page import PhonePage
from src.page_objects.guest_app_po.sms_page import SmsPage
from src.page_objects.guest_app_po.taxamo_page import TaxamoPage
from src.parameters.angela_parameters import get_park_full_name
from src.parameters.guest_parameters import GuestParameters
from src.parameters.taxamo_parameters import TaxamoParameters

guest_object = GuestParameters(media_prefix=None, user_id=None, phone=None)


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
def test_new_associated_media_payment_without_tax_with_credit_card(request, driver, application_parameters):
    test_name = "test_new_associated_media_payment_without_tax_with_credit_card"
    try:
        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.angela))

        menu_page_object = MenuPage(driver)

        menu_page_object.angela_login()

        menu_page_object.go_to_customer_media()

        api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
                                        GuestParameters.get_login_backdoor_phone_payment(),
                                        account_type=GuestParameters.get_account_type("app"))

        #  get the full attraction name
        full_attraction_name = api_helpers_object.api_get_attraction_name_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))

        customer_media_object = CustomerMediaPage(driver)

        prefix_media_number = customer_media_object.angela_get_prefix_media_number(
            get_park_full_name(application_parameters["domain"]), full_attraction_name)

        guest_object.set_media_prefix(prefix_media_number)
        ######
        # registration steps

        get_user_id = api_helpers_object.api_get_userid_by_phone_request(
            type=DomainSetting.get_domain_type('non_cart_domain'))
        print(get_user_id)

        api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))

        driver_related_actions.delete_cookies(driver)

        url_manager = ApplicationUrls(application_parameters)

        driver.get(url_manager.return_url(ApplicationUrls.guestapp))

        phone_page_object = PhonePage(driver)

        phone_page_object.accept_cookies()

        phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone_payment(),
                                                               GuestParameters.get_country_code_without_plus_prefix(
                                                                   "Israel"))

        phone_page_object.submit_login_process()


        sms_page_object = SmsPage(driver)
        sms_page_object.sms_verification()

        home_page_object = FeedPage(driver)

        # Login Verification
        home_page_object.login_verification()
        #######
        # end of registration steps

        side_menu_object = SideMenuPage(driver)
        side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
        side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))

        add_media_object = AddMediaPage(driver)

        add_media_object.check_existence_of_media_number_button_and_associate(guest_object.get_media_prefix(),
                                                                              application_parameters["attraction"])

        add_media_object.confirm_media_is_mine()

        home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)

        home_page_object.go_to_taxamo_payment_page_or_billing_details()

        taxamo_page_object = TaxamoPage(driver)

        taxamo_page_object.payment_process_for_media_with_credit_card()

        home_page_object.verify_payment_success()

        home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=False)

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

        home_page_object = FeedPage(driver)
        phone_page_object = PhonePage(driver)

        # Logout & Logout verification
        home_page_object.logout()

        phone_page_object.logout_verification()

        allure.attach(driver.get_screenshot_as_png(),
                      name=test_name,
                      attachment_type=AttachmentType.PNG)

        assert False


# @pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
# @pytest.mark.run(order=3)
# def test_new_associated_media_payment_without_tax_with_paypal(request, driver, application_parameters):
#     test_name = "test_new_associated_media_payment_without_tax_with_paypal"
#     try:
#
#         driver.refresh()
#
#         driver_related_actions.delete_cookies(driver)
#
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         GuestParameters.get_login_backdoor_phone_payment(),
#                                         account_type=GuestParameters.get_account_type("app"))
#
#         ######
#         # registration steps
#         get_user_id = api_helpers_object.api_get_userid_by_phone_request(
#             type=DomainSetting.get_domain_type('non_cart_domain'))
#         print(get_user_id)
#
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver.get(url_manager.return_url(ApplicationUrls.guestapp))
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.accept_cookies()
#
#         phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone_payment(),
#                                                                GuestParameters.get_country_code_without_plus_prefix(
#                                                                    "Israel"))
#
#         phone_page_object.submit_login_process()
#
#         phone_page_object.accept_terms_and_conditions()
#         phone_page_object.submit_login_process()
#
#         sms_page_object = SmsPage(driver)
#         sms_page_object.sms_verification()
#
#         home_page_object = FeedPage(driver)
#
#         # Login Verification
#         home_page_object.login_verification()
#         #######
#         # end of registration steps
#
#         side_menu_object = SideMenuPage(driver)
#         side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
#         side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))
#
#         add_media_object = AddMediaPage(driver)
#
#         add_media_object.check_existence_of_media_number_button_and_associate(guest_object.get_media_prefix(),
#                                                                               application_parameters["attraction"])
#
#         add_media_object.confirm_media_is_mine()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         home_page_object.go_to_taxamo_payment_page_or_billing_details()
#
#         taxamo_page_object = TaxamoPage(driver)
#
#         taxamo_page_object.payment_process_for_media_with_paypal()
#
#         home_page_object.verify_payment_success()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=False)
#
#         #######
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#         # - End of log out
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=True))
#     except:
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=False))
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         home_page_object = FeedPage(driver)
#         phone_page_object = PhonePage(driver)
#
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#         assert False
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=4)
# def test_payment_with_tax_and_ticket_id_number_verification(request, driver, application_parameters):
#     test_name = "test_payment_with_tax_and_ticket_id_number_verification"
#     try:
#         ######
#         # registration steps
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         GuestParameters.get_login_backdoor_phone_payment(),
#                                         account_type=GuestParameters.get_account_type("app"))
#
#         get_user_id = api_helpers_object.api_get_userid_by_phone_request(
#             type=DomainSetting.get_domain_type('non_cart_domain'))
#         print(get_user_id)
#
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver.get(url_manager.return_url(ApplicationUrls.guestapp))
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.accept_cookies()
#
#         phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone_payment(),
#                                                                GuestParameters.get_country_code_without_plus_prefix(
#                                                                    "Israel"))
#
#         phone_page_object.submit_login_process()
#
#         phone_page_object.accept_terms_and_conditions()
#         phone_page_object.submit_login_process()
#
#         sms_page_object = SmsPage(driver)
#         sms_page_object.sms_verification()
#
#         home_page_object = FeedPage(driver)
#
#         # Login Verification
#         home_page_object.login_verification()
#         #######
#         # end of registration steps
#
#         side_menu_object = SideMenuPage(driver)
#         side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
#         side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))
#
#         add_media_object = AddMediaPage(driver)
#
#         add_media_object.check_existence_of_media_number_button_and_associate(guest_object.get_media_prefix(),
#                                                                               application_parameters["attraction"])
#
#         add_media_object.confirm_media_is_mine()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         home_page_object.go_to_taxamo_payment_page_or_billing_details()
#
#         taxamo_page_object = TaxamoPage(driver)
#
#         taxamo_page_object.select_country_of_residence(TaxamoParameters.get_country_of_residence("italy"))
#
#         total_price_in_guest_app = taxamo_page_object.payment_process_for_media_with_credit_card()
#
#         home_page_object.verify_payment_success()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=False)
#
#         add_media_object = AddMediaPage(driver)
#
#         get_new_user_id = add_media_object.get_userId_number()
#
#         #######
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#         # - End of log out
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver.get(url_manager.return_url(ApplicationUrls.angela))
#
#         menu_page_object = MenuPage(driver)
#
#         menu_page_object.angela_login()
#
#         menu_page_object.go_to_search_customer()
#
#         search_customer_page_object = SearchCustomerPage(driver)
#
#         search_customer_page_object.search_guest_in_angela_by_user_id(get_new_user_id, get_park_full_name(
#             application_parameters["domain"]))
#
#         customer_information_page_object = CustomerInformationPage(driver)
#
#         ticket_price_in_angela = customer_information_page_object.get_price_of_ticket_in_angela()
#
#         customer_information_page_object.verify_price_of_ticket_in_angela_equals_to_price_in_guest_app(
#             total_price_in_guest_app, ticket_price_in_angela)
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=True))
#     except:
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=False))
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         home_page_object = FeedPage(driver)
#         phone_page_object = PhonePage(driver)
#
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         assert False
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# # @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=5)
# def test_new_associated_media_stripe_payment_without_tax_with_credit_card(request, driver, application_parameters):
#     test_name = "test_new_associated_media_stripe_payment_without_tax_with_credit_card"
#     try:
#         driver_related_actions.delete_cookies(driver)
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver.get(url_manager.return_url(ApplicationUrls.angela))
#
#         menu_page_object = MenuPage(driver)
#
#         menu_page_object.angela_login()
#
#         menu_page_object.go_to_customer_media()
#
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         GuestParameters.get_login_backdoor_phone_payment(),
#                                         account_type=GuestParameters.get_account_type("app"))
#
#         #  get the full attraction name
#         full_attraction_name = api_helpers_object.api_get_attraction_name_request(
#             type=DomainSetting.get_domain_type('non_cart_domain'))
#
#         customer_media_object = CustomerMediaPage(driver)
#
#         prefix_media_number = customer_media_object.angela_get_prefix_media_number(
#             get_park_full_name(application_parameters["domain"]), full_attraction_name)
#
#         guest_object.set_media_prefix(prefix_media_number)
#         ######
#         # registration steps
#
#         get_user_id = api_helpers_object.api_get_userid_by_phone_request(
#             type=DomainSetting.get_domain_type('non_cart_domain'))
#         print(get_user_id)
#
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))
#
#         driver_related_actions.delete_cookies(driver)
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver.get(url_manager.return_url(ApplicationUrls.guestapp))
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.accept_cookies()
#
#         phone_number = GuestParameters.get_login_backdoor_phone_payment()
#
#         phone_page_object.insert_phone_number_and_country_code(phone_number,
#                                                                GuestParameters.get_country_code_without_plus_prefix(
#                                                                    "Israel"))
#
#         phone_page_object.submit_login_process()
#
#         phone_page_object.accept_terms_and_conditions()
#         phone_page_object.submit_login_process()
#
#         sms_page_object = SmsPage(driver)
#         sms_page_object.sms_verification()
#
#         home_page_object = FeedPage(driver)
#
#         # Login Verification
#         home_page_object.login_verification()
#         #######
#         # end of registration steps
#
#         side_menu_object = SideMenuPage(driver)
#         side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
#         side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))
#
#         add_media_object = AddMediaPage(driver)
#
#         add_media_object.check_existence_of_media_number_button_and_associate(guest_object.get_media_prefix(),
#                                                                               application_parameters["attraction"])
#
#         add_media_object.confirm_media_is_mine()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         home_page_object.go_to_taxamo_payment_page_or_billing_details()
#
#         billing_details_page_object = BillingDetails(driver)
#
#         # No tax in UI test
#         billing_details_page_object.billing_details_fill_in(phone_number, GuestParameters.get_country_name("Israel"))
#
#         payment_page_object = PaymentPage(driver)
#
        # payment_page_object.verify_tax_calculation_includes_in_page(GuestParameters.get_country_name("Israel"))
#
#         payment_page_object.stripe_payment_process_with_credit_card()
#
        # home_page_object.verify_payment_success()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=False)
#
#         #######
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#         # - End of log out
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=True))
#     except:
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=False))
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         home_page_object = FeedPage(driver)
#         phone_page_object = PhonePage(driver)
#
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#
#         allure.attach(driver.get_screenshot_as_png(),
#                       name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         assert False
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# # @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=6)
# def test_new_associated_media_stripe_payment_with_tax_with_paypal(request, driver, application_parameters):
#     test_name = "test_new_associated_media_stripe_payment_with_tax_with_paypal"
#     try:
#         driver_related_actions.delete_cookies(driver)
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver.get(url_manager.return_url(ApplicationUrls.angela))
#
#         menu_page_object = MenuPage(driver)
#
#         menu_page_object.angela_login()
#
#         menu_page_object.go_to_customer_media()
#
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         GuestParameters.get_login_backdoor_phone_payment(),
#                                         account_type=GuestParameters.get_account_type("app"))
#
#         #  get the full attraction name
#         full_attraction_name = api_helpers_object.api_get_attraction_name_request(
#             type=DomainSetting.get_domain_type('non_cart_domain'))
#
#         customer_media_object = CustomerMediaPage(driver)
#
#         prefix_media_number = customer_media_object.angela_get_prefix_media_number(
#             get_park_full_name(application_parameters["domain"]), full_attraction_name)
#
#         guest_object.set_media_prefix(prefix_media_number)
#         ######
#         # registration steps
#
#         get_user_id = api_helpers_object.api_get_userid_by_phone_request(
#             type=DomainSetting.get_domain_type('non_cart_domain'))
#         print(get_user_id)
#
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))
#
#         driver_related_actions.delete_cookies(driver)
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver.get(url_manager.return_url(ApplicationUrls.guestapp))
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.accept_cookies()
#
#         phone_number = GuestParameters.get_login_backdoor_phone_payment()
#
#         phone_page_object.insert_phone_number_and_country_code(phone_number,
#                                                                GuestParameters.get_country_code_without_plus_prefix(
#                                                                    "Israel"))
#
#         phone_page_object.submit_login_process()
#
#         phone_page_object.accept_terms_and_conditions()
#         phone_page_object.submit_login_process()
#
#         sms_page_object = SmsPage(driver)
#         sms_page_object.sms_verification()
#
#         home_page_object = FeedPage(driver)
#
#         # Login Verification
#         home_page_object.login_verification()
#         #######
#         # end of registration steps
#
#         side_menu_object = SideMenuPage(driver)
#         side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
#         side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))
#
#         add_media_object = AddMediaPage(driver)
#
#         add_media_object.check_existence_of_media_number_button_and_associate(guest_object.get_media_prefix(),
#                                                                               application_parameters["attraction"])
#
#         add_media_object.confirm_media_is_mine()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         home_page_object.go_to_taxamo_payment_page_or_billing_details()
#
#         billing_details_page_object = BillingDetails(driver)
#
#         # No tax in UI test
#         billing_details_page_object.billing_details_fill_in(GuestParameters.get_germany_phone(),
#                                                             GuestParameters.get_country_name("Germany"))
#
#         payment_page_object = PaymentPage(driver)
#
#         payment_page_object.verify_tax_calculation_includes_in_page(GuestParameters.get_country_name("Germany"))
#
#         payment_page_object.stripe_payment_process_with_paypal()
#
#         home_page_object.verify_payment_success()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=False)
#
#         #######
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#         # - End of log out
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=True))
#     except:
#         request.config.testrail_reporter.capture_and_report_result(
#             get_case_id_by_automation_test_name(test_name),
#             assign_test_result(result=False))
#         allure.attach(driver.get_screenshot_as_png(), name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         home_page_object = FeedPage(driver)
#         phone_page_object = PhonePage(driver)
#
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#
#         allure.attach(driver.get_screenshot_as_png(),
#                       name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         assert False
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=7)
# def test_share_and_download_media_watermarked(request, driver, application_parameters):
#     test_name = "test_share_and_download_media_watermarked"
#     try:
#         ######
#         # registration steps
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         GuestParameters.get_login_backdoor_phone_payment(),
#                                         account_type=GuestParameters.get_account_type("app"))
#
#         get_user_id = api_helpers_object.api_get_userid_by_phone_request(
#             type=DomainSetting.get_domain_type('non_cart_domain'))
#         print(get_user_id)
#
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver_related_actions.delete_cookies(driver)
#
#         driver.get(url_manager.return_url(ApplicationUrls.guestapp))
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.accept_cookies()
#
#         phone_page_object.insert_phone_number_and_country_code(GuestParameters.get_login_backdoor_phone_payment(),
#                                                                GuestParameters.get_country_code_without_plus_prefix(
#                                                                    "Israel"))
#
#         phone_page_object.submit_login_process()
#
#         phone_page_object.accept_terms_and_conditions()
#         phone_page_object.submit_login_process()
#
#         sms_page_object = SmsPage(driver)
#         sms_page_object.sms_verification()
#
#         home_page_object = FeedPage(driver)
#
#         # Login Verification
#         home_page_object.login_verification()
#         #######
#         # end of registration steps
#
#         side_menu_object = SideMenuPage(driver)
#         side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
#         side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))
#
#         add_media_object = AddMediaPage(driver)
#
#         add_media_object.check_existence_of_media_number_button_and_associate(guest_object.get_media_prefix(),
#                                                                               application_parameters["attraction"])
#
#         add_media_object.confirm_media_is_mine()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         home_page_object.media_with_watermark_share_and_download_buttons_directed_to_payment_page("link")
#
#         home_page_object.verify_media_with_watermark_verify_share_and_download_buttons_directed_to_payment_page()
#
#         home_page_object.media_with_watermark_share_and_download_buttons_directed_to_payment_page("download")
#
#         home_page_object.verify_media_with_watermark_verify_share_and_download_buttons_directed_to_payment_page()
#
#         home_page_object.media_with_watermark_share_and_download_buttons_directed_to_payment_page("share")
#
#         home_page_object.verify_media_with_watermark_verify_share_and_download_buttons_directed_to_payment_page()
#
#         #######
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#         # - End of log out
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
#         allure.attach(driver.get_screenshot_as_png(),
#                       name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         home_page_object = FeedPage(driver)
#
#         home_page_object.logout()
#
#         phone_page_object = PhonePage(driver)
#         phone_page_object.logout_verification()
#
#         assert False
#
#
# @pytest.mark.usefixtures("driver", "application_parameters")
# @pytest.mark.regression
# # @pytest.mark.dev
# @pytest.mark.run(order=8)
# def test_share_and_download_media_unwatermarked(request, driver, application_parameters):
#     test_name = "test_share_and_download_media_unwatermarked"
#     try:
#         ######
#         # registration steps
#         api_helpers_object = ApiHelpers(application_parameters, GuestParameters.israel,
#                                         GuestParameters.get_login_backdoor_phone_payment(),
#                                         account_type=GuestParameters.get_account_type("app"))
#
#         get_user_id = api_helpers_object.api_get_userid_by_phone_request(
#             type=DomainSetting.get_domain_type('non_cart_domain'))
#         print(get_user_id)
#
#         api_helpers_object.api_delete_userid_request(get_user_id, type=DomainSetting.get_domain_type('non_cart_domain'))
#
#         url_manager = ApplicationUrls(application_parameters)
#
#         driver_related_actions.delete_cookies(driver)
#
#         driver.get(url_manager.return_url(ApplicationUrls.guestapp))
#
#         phone_page_object = PhonePage(driver)
#
#         phone_page_object.insert_phone_number_and_country_code(
#             GuestParameters.get_login_backdoor_phone_payment(),
#             GuestParameters.get_country_code_without_plus_prefix("Israel"))
#
#         phone_page_object.accept_cookies()
#
#         phone_page_object.submit_login_process()
#
#         phone_page_object.accept_terms_and_conditions()
#         phone_page_object.submit_login_process()
#
#         sms_page_object = SmsPage(driver)
#         sms_page_object.sms_verification()
#         #
#         home_page_object = FeedPage(driver)
#
#         # Login Verification
#         home_page_object.login_verification()
#         ######
#         # end of registration steps
#
#         side_menu_object = SideMenuPage(driver)
#         side_menu_object.go_to(WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value)
#         side_menu_object.go_to_page_verification(SideMenuParameters.get_url_verification_string("Add media"))
#
#         add_media_object = AddMediaPage(driver)
#
#         add_media_object.check_existence_of_media_number_button_and_associate(guest_object.get_media_prefix(),
#                                                                               application_parameters["attraction"])
#
#         add_media_object.confirm_media_is_mine()
#
#         home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=True)
#
#         home_page_object.go_to_taxamo_payment_page_or_billing_details()
#
#         taxamo_page_object = TaxamoPage(driver)
#
#         taxamo_page_object.payment_process_for_media_with_credit_card()
#
#         home_page_object.verify_payment_success()
#
        home_page_object.verify_if_photo_with_watermark_or_not(watermark_expected_result=False)
#
#         # verify link button
#
#         home_page_object.media_unwatermark_share_and_download_buttons(
#             GuestParameters.get_button_share_and_download_type("link"))
#
#         home_page_object.media_unwatermark_share_and_download_verify(
#             GuestParameters.get_button_share_and_download_type("link"))
#
#         # verify download button
#
#         home_page_object.media_unwatermark_share_and_download_buttons(
#             GuestParameters.get_button_share_and_download_type("download"))
#
#         home_page_object.media_unwatermark_share_and_download_verify(
#             GuestParameters.get_button_share_and_download_type("download"))
#
#         #######
#         # Logout & Logout verification
#         home_page_object.logout()
#
#         phone_page_object.logout_verification()
#         # - End of log out
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
#
#         allure.attach(driver.get_screenshot_as_png(),
#                       name=test_name,
#                       attachment_type=AttachmentType.PNG)
#
#         home_page_object = FeedPage(driver)
#         home_page_object.logout()
#
#         phone_page_object = PhonePage(driver)
#         phone_page_object.logout_verification()
#
#         assert False
