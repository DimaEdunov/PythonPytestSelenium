import os


def get_testrail_url():
    testrail_url = "https://pomvom.testrail.io/index.php?/api/v2"
    return testrail_url


def get_testrail_api_key():
    testrail_api_key = os.environ.get("testrail_api_key")
    return testrail_api_key


def get_testrail_user_name():
    testrail_user_name = "qa.serviceaccount_automation@pomvom.com"
    return testrail_user_name


def get_testrail_pomvom_project_id():
    testrail_pomvom_project_id = 1
    return testrail_pomvom_project_id


def get_testrail_regression_suite_id():
    testrail_regression_suite_id = 3
    return testrail_regression_suite_id
