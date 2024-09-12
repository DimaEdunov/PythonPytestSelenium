import os

class PaypalParameters():

    @staticmethod
    def get_paypal_account_credentials(key):
        paypal_account_credentials = {"email" : "QA@pomvom.com" , "password" : os.environ.get('selenium_qa_paypal_account_password')}

        return paypal_account_credentials[key]
