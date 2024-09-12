import os



def get_angela_login_credentials(key):
    credentials = {"user": "qa.serviceaccount_automation@pomvom.com", "password": os.environ.get('selenium_qa_email_service_account_password')}
    print(credentials[key])
    return credentials[key]


def get_angela_page_name(key):
    page_name = {"search_customer": "Search Customer", "customer_information": "Customer Information",
                 "customer_media": "Customer Media", "PDES": "PDES"}
    return page_name[key]


@staticmethod
def get_park_full_name(park_short_name):
    get_park_full_name_dictionary = {"mt": "Madame Tussauds London",
                                     "at": "Alton Towers Resort",
                                     "ht": "Warner Bros. Studio Tour London",
                                     "wb": "Warner Bros. Hollywood",
                                     "ps": "Park of Poland - Suntago",
                                     "ub": "Butlins Skegness Holiday Park",
                                     "pp": "Paultons Park and Peppa Pig World",
                                     "tp": "Thorpe Park Resort",
                                     "nw": "LEGOLAND New York",
                                     "sdsp": "San Diego Zoo Safari Park",
                                     "totr": "Top Of The Rock",
                                     "bp": "Blackpool Pleasure Beach",
                                     "llfl": "LEGOLAND Florida",
                                     "sdz": "San Diego Zoo",
                                     "ef": "Efteling",
                                     "av": "Six Flags Magic Mountain"
                                     }

    return get_park_full_name_dictionary[park_short_name]
