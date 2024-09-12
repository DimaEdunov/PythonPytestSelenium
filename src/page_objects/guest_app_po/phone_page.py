import time
import allure
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PhonePage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("PhonePage.accept_cookies() | Accept Cookies of the webpage")
    def accept_cookies(self):
        time.sleep(4)
        # Locate 'accept' button, on cookies popup
        if len(self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_ACCEPT_COOKIES_BUTTON.value)) > 0:

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_ACCEPT_COOKIES_BUTTON.value))).click()
        else:
            pass

    @allure.step("PhonePage.insert_phone_number() | Insert phone number")
    def insert_phone_number_and_country_code(self, phone_number, country_code):

        time.sleep(2)
        # Locate country code and phone field element on login page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_NUMBER_FIELD.value))).click()

        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_POPUP_SEARCH_FIELD.value)))
        search_field.click()
        time.sleep(1)
        search_field.clear()
        search_field.send_keys(country_code)
        time.sleep(1)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_POPUP_FIRST_ITEM.value))).click()

        phone_number_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.PHONE_NUMBER_FIELD.value)))

        phone_number_field.click()
        time.sleep(0.5)
        phone_number_field.clear()
        time.sleep(0.5)
        phone_number_field.click()
        time.sleep(0.5)
        phone_number_field.clear()
        phone_number_field.send_keys(phone_number)

    @allure.step("PhonePage.accept_terms_and_conditions() | Accept terms and conditions")
    def accept_terms_and_conditions(self):
        # Added if to distinguish between with or without date of birth flows
        time.sleep(4)
        if len(self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.LOGIN_AGREE_TERMS_BUTTON.value)) > 0:
            terms_and_conditions_checkbox = self.driver.find_element(By.XPATH,
                                                                     WebGuestAppStaticElements.LOGIN_AGREE_TERMS_BUTTON.value)
            terms_and_conditions_checkbox.click()
            time.sleep(1)
        else:
            pass

    @allure.step("PhonePage.submit_login_process() | Submit the login process ")
    def submit_login_process(self):
        time.sleep(3)
        try:
            #  Locate 'next' field element on login page
            next_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.LOGIN_NEXT_BUTTON.value)))

            next_button.click()

            time.sleep(7)

        except:
            assert False

    @allure.step("PhonePage.logout_verification() | logout verification")
    def logout_verification(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, WebGuestAppStaticElements.LOGIN_VIEW_YOUR_CONTENT.value)))
        except:
            assert False

    @allure.step(
        "PhonePage.insert_invalid_phone_number_get_error_message() | Insert invalid phone number and get error mssage")
    def insert_invalid_phone_number(self, invalid_phone_number):
        # insert invalid phone number in phone field element and get an error message
        phone_number_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.PHONE_NUMBER_FIELD.value)))

        phone_number_field.click()
        phone_number_field.send_keys(invalid_phone_number)

        self.submit_login_process()

    @allure.step(
        "PhonePage.invalid_phone_number_verification() | Verified popup error message appears after typing a ""wrong phone number")
    def invalid_phone_number_verification(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_ERROR_MESSAGE_INVALID_PHONE.value)))

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.PHONE_NUMBER_FIELD.value))).clear()

    @allure.step("go_to_terms_and_conditions_page() | click on terms and conditions if exists")
    def go_to_terms_and_conditions_page(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.LOGIN_TERMS_AND_CONDITIONS_LINK.value))).click()

    @allure.step("go_to_terms_and_conditions_page_verification() | terms and conditions verification")
    def terms_and_conditions_page_verification(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.TERMS_AND_CONDITIONS_VERIFICATION_PAGE.value)))

    @allure.step("click_on_go_back_button_in_terms_and_conditions_page() | click on go back button in terms and conditions page")
    def click_on_go_back_button_in_terms_and_conditions_page(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_GO_BACK_BUTTON.value))).click()

    @allure.step("PhonePage.insert_email_address() | Insert email address")
    def register_with_gmail_address(self, email, password):
        time.sleep(2)
        # Google iframe gives the ability to access google popup
        google_iframe = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.GOOGLE_BUTTON_IFRAME.value)))

        self.driver.switch_to.frame(google_iframe)

        google_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_GOOGLE_BUTTON.value)))
        google_button.click()

        self.driver.switch_to.default_content()

        google_popup = self.driver.window_handles[1]
        self.driver.switch_to.window(google_popup)

        time.sleep(4)

        if len(self.driver.find_elements(By.XPATH,
                                         WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_EMAIL_FIELD.value)) > 0:

            email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_EMAIL_FIELD.value)))
            email_field.click()
            time.sleep(2)

            email_field.send_keys(email)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_NEXT_BUTTON.value))).click()

            time.sleep(4)

            second_email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_EMAIL_FIELD.value)))

            second_email_field.send_keys(email)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH,
                 WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_NEXT_BUTTON_SECOND_PAGE.value))).click()

            time.sleep(2)

            password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_PASSWORD_FIELD.value)))

            password_field.send_keys(password)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_SUBMIT_BUTTON.value))).click()

            time.sleep(3)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (
                By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_CONTINUE_BUTTON.value))).click()

            google_popup = self.driver.window_handles[1]
            self.driver.switch_to.window(google_popup)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (
                By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_LOGGED_IN_EMAIL.value))).click()

        else:
            if len(self.driver.find_elements(By.XPATH,
                                             WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_LOGGED_IN_EMAIL.value)) > 0:
                time.sleep(4)

                # choose an account page in popup google login
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                    (
                    By.XPATH, WebGuestAppStaticElements.LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_LOGGED_IN_EMAIL.value))).click()
                time.sleep(4)

        guest_app_window = self.driver.window_handles[0]
        self.driver.switch_to.window(guest_app_window)

    @allure.step("PhonePage.insert_phone_number() | Insert phone number")
    def insert_phone_number_with_unpaid_media(self, country_code):

        time.sleep(2)
        # Locate country code and phone field element on login page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_NUMBER_FIELD.value))).click()

        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_POPUP_SEARCH_FIELD.value)))
        search_field.click()
        time.sleep(1)
        search_field.clear()
        search_field.send_keys(country_code)
        time.sleep(1)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_POPUP_FIRST_ITEM.value))).click()

        phone_number_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.PHONE_NUMBER_FIELD.value)))

        phone_number_field.click()
        time.sleep(0.5)
        phone_number_field.clear()
        time.sleep(0.5)
        phone_number_field.click()
        time.sleep(0.5)
        phone_number_field.clear()
        phone_number_field.send_keys('99996669')

    @allure.step("PhonePage.insert_phone_number() | Insert phone number")
    def insert_phone_number_with_paid_media(self, country_code):

        time.sleep(2)
        # Locate country code and phone field element on login page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_NUMBER_FIELD.value))).click()

        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_POPUP_SEARCH_FIELD.value)))
        search_field.click()
        time.sleep(1)
        search_field.clear()
        search_field.send_keys(country_code)
        time.sleep(1)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_POPUP_FIRST_ITEM.value))).click()

        phone_number_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.PHONE_NUMBER_FIELD.value)))

        phone_number_field.click()
        time.sleep(0.5)
        phone_number_field.clear()
        time.sleep(0.5)
        phone_number_field.click()
        time.sleep(0.5)
        phone_number_field.clear()
        phone_number_field.send_keys('99996668')
