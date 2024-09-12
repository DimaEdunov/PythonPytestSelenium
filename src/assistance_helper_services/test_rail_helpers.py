import requests
import base64
import json
from src.parameters.testrail_parameters import get_testrail_url, get_testrail_pomvom_project_id, \
    get_testrail_regression_suite_id, get_testrail_user_name, get_testrail_api_key


@staticmethod
def get_case_id_by_automation_test_name(key) -> object:
    TEST_CASE_MAPPING = {'test_associate_photos_add_to_cart': 264,
                         'test_associate_videos_cart': 301,
                         'test_payment_for_photo_cart':"",
                         'test_landing_qr_page_cart':"",
                         'test_share_and_download_button_cart':"",
                         'test_popup_recommendation_cart':"",
                         'test_review_cart_page_cart':"",
                         "test_wrong_media_number_blocked_after_6_times": 58,
                         'test_new_associated_media_payment_without_tax_with_credit_card': 18,
                         'test_new_associated_media_payment_without_tax_with_paypal': 45,
                         'test_payment_with_tax_and_ticket_id_number_verification': 19,
                         'test_new_associated_media_stripe_payment_without_tax_with_credit_card': 302,
                         'test_new_associated_media_stripe_payment_with_tax_with_paypal': 303,
                         'test_share_and_download_media_watermarked': 46,
                         'test_share_and_download_media_unwatermarked': 21,
                         'test_positive_mobile_login':"",
                         'test_mobile_side_menu': "",
                         'test_logout': 304,
                         'test_negative_login': 15,
                         'test_positive_login': 17,
                         'test_delete_user_and_register_with_a_new_user': 16,
                         'test_terms_and_conditions_page_verification': 299,
                         'test_side_menu_items': 22,
                         'test_translation': 23,
                         'test_terms_and_conditions_login_page_verification': 57,
                         'test_contact_us_form_verification': 282,
                         'test_entitlement_search_a_non_existing_guest_by_guest_id': 27,
                         'test_entitlement_search_an_existing_guest_by_guest_id': 28,
                         'test_entitlement_search_a_non_existing_guest_by_phone': 29,
                         'test_entitlement_search_an_existing_guest_by_phone': 30,
                         'test_entitlement_search_a_non_existing_guest_by_qr': 31,
                         'test_entitlement_search_an_existing_guest_by_qr': 32,
                         'test_entitlement_give_guest_entitlement': 33,
                         'test_entitlement_remove_entitlement': 34,
                         'test_entitlement_give_guest_entitlement_cart':"",
                         'test_find_media_by_attraction_click_negative': 47,
                         'test_find_media_by_attraction_click_positive': 48,
                         'test_verify_ui': 300,
                         'test_by_attraction_add_to_pass_search_an_existing_guest_by_qr': 50,
                         'test_by_attraction_add_to_pass_search_a_non_existing_guest_by_phone': 51,
                         'test_by_attraction_add_to_pass_search_a_non_existing_guest_by_guest_id': 52,
                         'test_by_attraction_add_to_pass_search_an_existing_guest_by_guest_id': 53,
                         'test_by_attraction_add_to_pass_search_multiple_photos_and_associate': 55,
                         'test_guest_media_search_a_non_existing_guest_by_qr': 178,
                         'test_guest_media_search_an_existing_guest_by_guest_id': 183,
                         'test_guest_media_search_a_non_existing_guest_by_phone': 180,
                         'test_guest_media_search_an_existing_guest_by_phone': 181,
                         'test_guest_media_search_a_non_existing_guest_by_guest_id': 182,
                         'test_find_media_by_number_negative': 35,
                         'test_find_media_by_number_print': 36,
                         'test_media_by_number_search_a_non_existing_guest_by_qr': 37,
                         'test_media_by_number_search_an_existing_guest_by_qr': 38,
                         'test_media_by_number_search_a_non_existing_guest_by_phone': 39,
                         'test_media_by_number_search_a_non_existing_guest_by_guest_id': 40,
                         'test_media_by_number_search_an_existing_guest_by_guest_id': 41,
                         'test_new_feed_elements_verification_including_UI_and_Mixpanel': 383,
                         'test_paid_media_ui_and_mix_panel_popup': 384,
                         'test_paid_media_ui_and_mix_panel_feed': 385,
                         'test_unpaid_media_ui_and_mix_panel_popup': 434,
                         'test_cart_and_single_media': 399
                         }

    return TEST_CASE_MAPPING [key]

@staticmethod
def assign_test_result(result):
    if result:
        return "passed"
    else:
        return "failed"


def get_case_id_from_testrail():
    # TestRail API Endpoint for getting test cases in a suite
    get_cases_endpoint = f"{get_testrail_url()}/get_cases/{get_testrail_pomvom_project_id()}&suite_id={get_testrail_regression_suite_id()}"

    # Prepare headers for authentication
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {base64.b64encode(f'{get_testrail_user_name()}:{get_testrail_api_key()}'.encode()).decode()}"
    }

    # Make the API request to get test cases
    response = requests.get(get_cases_endpoint, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            response_data = response.json()

            # Extract the 'cases' array from the response
            test_cases = response_data.get("cases", [])

            # Extract case_id and title from each test case
            case_info = {case["id"]: case["title"] for case in test_cases}
            print("case_info: " + str(case_info))

            print(f"Successfully retrieved test cases for TestRail project {get_testrail_pomvom_project_id()} and suite {get_testrail_regression_suite_id()}:")
            for case_id, title in case_info.items():
                print(f"{case_id}={title}")

        except Exception as e:
            print(f"Error parsing JSON response: {e}")
    else:
        print(
            f"Failed to retrieve test cases for TestRail project {get_testrail_pomvom_project_id()} and suite {get_testrail_regression_suite_id()}. Status Code: {response.status_code}")
        print("Response content:", response.text)


def create_test_run_in_testrail(run_name):
    try:
        end_point = f"{get_testrail_url()}/add_run/{get_testrail_pomvom_project_id()}"
        print("end_point: " + str(end_point))
        headers = {"Content-Type": "application/json", "Authorization": f"Basic {base64.b64encode(f'{get_testrail_user_name()}:{get_testrail_api_key()}'.encode()).decode()}"}
        data = {
            "suite_id": get_testrail_regression_suite_id(),
            "name": str(run_name),
            "include_all": True
        }
        get_test_run = requests.post(end_point, data=json.dumps(data), headers=headers)
        response = json.loads(get_test_run.content)
        if 'error' in response or None in response:
            print(f"Failed to create Test Run: {response['error']}")
        else:
            created_run_id = response['id']
            print(f"Test Run created successfully. Run ID: {created_run_id}")
            return created_run_id
    except requests.exceptions.RequestException as e:
        print(f"Error creating Test Run: {e}")
