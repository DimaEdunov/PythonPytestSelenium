from random import randint
import random
import string

import allure


class GuestParameters():
    israel = "Israel"
    United_Kingdom = "United Kingdom"
    Germany = "Germany"

    def __init__(self, media_prefix, user_id, phone):
        self.media_prefix = media_prefix
        self.user_id = user_id
        self.phone = phone

    # Is used in multiple tests, therefore create an object for it
    def set_media_prefix(self, media_prefix):
        self.media_prefix = media_prefix

    def get_media_prefix(self):
        return self.media_prefix

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    @staticmethod
    def get_random_qr():
        generate_random_qr = str(randint(1000000000, 9999999999)) + str(2 * random.choice(string.ascii_letters))
        return generate_random_qr

    # For Registration
    @staticmethod
    def get_registration_tests_backdoor_phone():
        back_door_phone_number_registration = "99999431"
        return back_door_phone_number_registration

    # For Login test
    @staticmethod
    def get_login_backdoor_phone():
        back_door_phone_number_login = "99992911"

        return back_door_phone_number_login

    @staticmethod
    def get_country_code_without_plus_prefix(key):
        if key == None:
            pass
        else:
            country_codes = {"Israel": "972", "United Kingdom": "44"}

            return country_codes[key]

    @staticmethod
    def get_country_name(key):
        country_name = {"Israel": "Israel", "Germany": "Germany"}

        return country_name[key]

    @staticmethod
    def get_random_backdoor_phone():
        generate_random_phone = "9999" + str(randint(1000, 9999))
        return generate_random_phone

    @staticmethod
    def get_invalid_login_phone():
        invalid_phone_number = "05067854561"

        return invalid_phone_number

    @staticmethod
    @allure.step("get_too_short_phone() | Use a 'Too Short' phone")
    def get_too_short_phone():
        too_short_phone_number = "9999123"

        return too_short_phone_number

    @staticmethod
    def get_valid_existing_phone():
        valid_new_phone_number = "99993733"

        return valid_new_phone_number

    @staticmethod
    def get_photo_number():
        photo_number = "U0179"

        return photo_number

    # for associated media tests
    @staticmethod
    def get_login_backdoor_phone_payment():
        login_backdoor_phone_wrong_media_number = "99991998"

        return login_backdoor_phone_wrong_media_number

    # for test_wrong_media_number_blocked_after_6_times
    @staticmethod
    def get_login_backdoor_phone_wrong_media():
        login_backdoor_phone_wrong_media_number = "99991996"

        return login_backdoor_phone_wrong_media_number

    @staticmethod
    def get_germany_phone():
        germany_phone = "30997869"

        return germany_phone

    @staticmethod
    def get_account_type(key):
        account_type = {"qr": "qr", "app": "app"}
        return account_type[key]

    @staticmethod
    def get_button_share_and_download_type(key):
        account_type = {"link": "link", "download": "download", "facebook": "facebook"}
        return account_type[key]

    @staticmethod
    def get_qr_for_url(qr_number):
        qr_for_url = "qr/" + qr_number

        return qr_for_url

    @staticmethod
    def get_contact_us_form_credentials(key):
        contact_us_form_credentials = {"subject": "Test - Ignore",
                                       "comments": "Test - Ignore"}

        return contact_us_form_credentials[key]

    @staticmethod
    def get_email_address():
        login_backdoor_phone_wrong_media_number = "qa.serviceaccount_automation@pomvom.com"

        return login_backdoor_phone_wrong_media_number
