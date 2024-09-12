from src.parameters.guest_parameters import GuestParameters
import os


class OpsuiAppParameters():

    entitlements = "Entitlements"
    find_media_by_number = "Find Media By Number"
    find_media_by_attraction = "Find Media By Attraction"
    find_media_by_qr = "Find Media By QR"
    guest_search = "Guest Search"
    print_photo = "Print Photo"

    @staticmethod
    def get_opsui_login_credentials(key):
        credentials = {"user": "qa.serviceaccount_automation@pomvom.com",
                       "password": os.environ.get('selenium_qa_email_service_account_password')
                       }
        return credentials[key]

    @staticmethod
    def get_opsui_qr(key):
        qr_list = {"existing_qr_string": "used_qr_1231",
                   "non_existing_qr_string": "not_used_qr2",
                   "random_qr": GuestParameters.get_random_qr()
                   }
        return qr_list[key]

    @staticmethod
    def get_too_short_userid():
        too_short_userid = "63723270eee477306d"
        return too_short_userid

    @staticmethod
    def get_opsui_page_name_english(key):
        credentials = {"Entitlements": "Entitlements",
                       "Find Media By Number": "Find Media By Number",
                       "Find Media By Attraction": "Find Media By Attraction",
                       "Find Media By QR": "Find Media By QR",
                       "Guest Search": "Guest Search",
                       "Print Photo": "Print Photo"
                       }
        return credentials[key]

    @staticmethod
    def get_opsui_page_name_spanish(key):
        credentials = {"Entitlements": "Derechos",
                       "Find Media By Number": "Buscar medio por número",
                       "Find Media By Attraction": "Buscar medio por atracción",
                       "Guest Search": "Búsqueda de invitado",
                       }
        return credentials[key]

    @staticmethod
    def get_ticket_type(key):
        qr_list = {"video": "Video",
                   "all_photos": "All Photos",
                   "all_media": "All Media"
                   }
        return qr_list[key]

    @staticmethod
    def get_opsui_entitlements(key):
        credentials = {"2_week_pass": "2 Week Pass",
                       "annual_pass": "Annual Pass",
                       "2_day_pass": "2 Day Pass",
                       "VIP_pass": "VIP Pass",
                       "season_pass": "Season Pass",
                       "1_day_pass": "1 Day Pass",
                       }
        return credentials[key]

    @staticmethod
    def get_opsui_entitlements_days_expected(key):
        credentials = {"2_week_pass_total": "28",
                       "2_week_pass_forward": "14",
                       "2_week_pass_backward": "14",
                       "annual_pass_total": "372",
                       "annual_pass_forward": "365",
                       "annual_pass_backward": "7",
                       "2_day_pass_total": "4",
                       "2_day_pass_forward": "2",
                       "2_day_pass_backward": "2",
                       "VIP_pass_total": "180",
                       "VIP_pass_forward": "90",
                       "VIP_pass_backward": "90",
                       "1_day_pass_total": "1",
                       "1_day_pass_forward": "1",
                       "1_day_pass_backward": "0"
                       }
        return credentials[key]



