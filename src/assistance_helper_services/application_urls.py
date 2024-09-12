import time
import pyautogui

class ApplicationUrls:
    # Global variables, of app names (useage example is in 'focus tab' method below)
    guestapp = "guestapp"
    angela = "angela"
    opsui = "opsui"
    guestapp_cart = "guestapp_cart"
    opsui_cart = "opsui_cart"

    def __init__(self, application_parameters):
        self.domain = application_parameters["domain"]
        self.attraction = application_parameters["attraction"]
        self.site_code = application_parameters["site_code"]
        self.environment = application_parameters["environment"]
        self.domain_cart = application_parameters["domain_cart"]
        self.attraction_cart = application_parameters["attraction_cart"]
        self.site_code_cart = application_parameters["site_code_cart"]

    # Apps URL's (helper)

    def return_url(self, app_name):
        if app_name == "guestapp":
            return "https://photos-%s.pomvom.com/%s/" % (self.environment, self.domain)

        elif app_name == "guestapp_cart":
            return "https://photos-%s.pomvom.com/%s/" % (self.environment, self.domain_cart)

        elif app_name == "opsui":
            print("https://operatorui-%s.pomvom.com/#/%s/%s/1/" % (
            self.environment, self.site_code.upper(), self.attraction.upper()))
            return "https://operatorui-%s.pomvom.com/#/%s/%s/1/" % (
            self.environment, self.site_code.upper(), self.attraction.upper())

        elif app_name == "opsui_cart":
            return "https://operatorui-%s.pomvom.com/#/%s/%s/1/" % (
            self.environment, self.site_code_cart.upper(), self.attraction_cart.upper())

        elif app_name == "angela":
            return "https://angela-%s.pomvom.com/" % self.environment

        else:
            assert False

    def return_opsui_url(self, get_site_code, get_attraction_code):
        return "https://operatorui-%s.pomvom.com/#/%s/%s/1/menu" % (
            self.environment, get_site_code.upper(), get_attraction_code.upper())

    @staticmethod
    def enter_url_in_address_bar(url):
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)
        pyautogui.typewrite(url)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(2)
        pyautogui.press('enter')

    @staticmethod
    def enter_url_with_qr_in_address_bar(url):
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)
        pyautogui.typewrite(url)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
