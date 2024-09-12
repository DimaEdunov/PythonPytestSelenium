import json
import requests
import base64
from src.parameters.testrail_parameters import get_testrail_user_name, get_testrail_api_key


class TestRailReporter:
    def __init__(self):
        self.test_results = []

    def capture_and_report_result(self, case_id, test_result_status):
        print("case_id: " + str(case_id))
        status_id = 1 if test_result_status == 'passed' else 5
        result = {"case_id": case_id, "status_id": status_id}
        self.test_results.append(result)

    def update_test_results(self, testrail_url, test_run_id):
        try:
            # Concatenate results and create the data payload for updating TestRail
            data = {"results": self.test_results}
            print("data: " + str(data))
            # Prepare headers for authentication
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Basic {base64.b64encode(f'{get_testrail_user_name()}:{get_testrail_api_key()}'.encode()).decode()}",
            }

            # Make the request to update the test results
            end_point = f"{testrail_url}/add_results_for_cases/{test_run_id}"
            print("end_point: " + str(end_point))
            response = requests.post(end_point, data=json.dumps(data), headers=headers)

            if response.status_code == 200:
                print(f"Successfully updated test results for TestRail run {test_run_id}.")
            else:
                print(
                    f"Failed to update test results for TestRail run {test_run_id}. Status Code: {response.status_code}")
                print("Response content:", response.text)
        except Exception as e:
            print(f"Error finalizing test run in TestRail: {e}")
