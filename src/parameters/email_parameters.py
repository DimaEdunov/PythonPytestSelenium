import os


@staticmethod
def get_outlook_url():
    google_url = r'https://outlook.office.com/mail/qa.serviceaccount_automation@pomvom.com/'
    return google_url

@staticmethod
def get_outlook_credentials(key):
    country_of_residence = {"username": "qa.serviceaccount_automation@pomvom.com", "password": os.environ.get('selenium_qa_email_service_account_password')}

    return country_of_residence[key]

@staticmethod
def get_contact_us_url():
    google_url = r'https://support.pomvom.com/hc/en-us/requests/new?'
    return google_url