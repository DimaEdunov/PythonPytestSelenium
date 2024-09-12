class TaxamoParameters():

    @staticmethod
    def get_credit_card_credentials(key):
        credit_card_credentials = {"email": "qa.serviceaccount_automation@pomvom.com", "card_number": "4242424242424242", "expire_date": "0952",
                                   "cvc_number": "699"}

        return credit_card_credentials[key]

    @staticmethod
    def get_country_of_residence(key):
        country_of_residence = {"israel": "IL", "italy": "IT", "IM": "IM"}

        return country_of_residence[key]
