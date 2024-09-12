class DomainSetting():

    @staticmethod
    def get_languages(key):
        languages = {
            "English": "en",
            "Portuguese": "pt",
            "German": "de",
            "Spanish": "es",
            "Polish": "pl"
        }
        return languages[key]

    @staticmethod
    def get_domain_type(key):
        domain_type = {
            "domain_cart": "cart_domain",
            "non_cart_domain": "non_cart_domain",
        }
        return domain_type[key]