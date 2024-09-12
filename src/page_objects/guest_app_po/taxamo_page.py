import re
import time
import allure


from src.elements.guest_app.dynamic_elemenets.guest_app_dynamic_elements_login_process import \
    GuestAppDynamicElementsLoginProcess
from src.parameters.paypal_parameters import PaypalParameters
from src.parameters.taxamo_parameters import TaxamoParameters
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaxamoPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("TaxamoPage.select_country_of_residence() | select country of residence")
    def select_country_of_residence(self, country):
        time.sleep(3)

        GuestAppDynamicElementsLoginProcess.select_taxamo_country_of_residence_picklist(self.driver, country)

        time.sleep(4)

    @allure.step("TaxamoPage.payment_process_for_media_with_credit_card() | payment process for media with credit card")
    def payment_process_for_media_with_credit_card(self):
        total_price = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, WebGuestAppStaticElements.TAXAMO_TOTAL_PRICE.value))).text
        total_price_list = re.findall(r'[\d\.\d]+', total_price)
        total_price_float = float(total_price_list[0])

        time.sleep(3)

        email_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.TAXAMO_EMAIL_FIELD.value)))
        email_field.click()

        time.sleep(1)

        email_field.send_keys(TaxamoParameters.get_credit_card_credentials("email"))

        time.sleep(1)

        credit_card_radio_button = self.driver.find_element(By.XPATH, WebGuestAppStaticElements.TAXAMO_CREDIT_CARD_RADIOBUTTON.value)
        credit_card_radio_button.click()

        # iframe_card_number
        iframe_card_number = self.driver.find_elements(By.TAG_NAME, WebGuestAppStaticElements.TAXAMO_IFAME_ELEMENTS.value)

        self.driver.switch_to.frame(iframe_card_number[0])

        card_number_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.TAXAMO_CARD_NUMBER_FIELD.value)))

        card_number_field.click()

        time.sleep(1)

        card_number_field.send_keys(TaxamoParameters.get_credit_card_credentials("card_number"))

        time.sleep(1)
        self.driver.switch_to.default_content()

        # iframe_card_number
        iframe_card_number = self.driver.find_elements(By.TAG_NAME, WebGuestAppStaticElements.TAXAMO_IFAME_ELEMENTS.value)

        self.driver.switch_to.frame(iframe_card_number[1])

        expire_date_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.TAXAMO_EXPIRE_DATE_FIELD.value)))
        expire_date_field.click()
        expire_date_field.send_keys(TaxamoParameters.get_credit_card_credentials("expire_date"))

        time.sleep(1)
        self.driver.switch_to.default_content()

        # iframe_cvc
        iframe_card_number = self.driver.find_elements(By.TAG_NAME, WebGuestAppStaticElements.TAXAMO_IFAME_ELEMENTS.value)
        self.driver.switch_to.frame(iframe_card_number[2])

        cvc_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.TAXAMO_CVC_FIELD.value)))
        cvc_field.click()
        cvc_field.send_keys(TaxamoParameters.get_credit_card_credentials("cvc_number"))

        time.sleep(5)
        self.driver.switch_to.default_content()

        time.sleep(2)

        status = self.driver.find_element(By.XPATH, WebGuestAppStaticElements.TAXAMO_I_SELF_DECLARE_BUTTON.value).is_displayed()
        print("status is: " + str(status))
        if status == True:
            self.driver.find_element(By.XPATH, WebGuestAppStaticElements.TAXAMO_I_SELF_DECLARE_BUTTON.value).click()

        time.sleep(3)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.TAXAMO_PROCEED_BUTTON.value))).click()
        time.sleep(20)

        return total_price_float

    @allure.step("TaxamoPage.payment_process_for_media_with_paypal() | payment process for media with paypal")
    def payment_process_for_media_with_paypal(self):
        taxamo_email = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.TAXAMO_EMAIL_FIELD.value)))

        taxamo_email.click()
        time.sleep(1)

        taxamo_email.send_keys(TaxamoParameters.get_credit_card_credentials("email"))

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.TAXAMO_PAYPAL_RADIOBUTTON.value))).click()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.TAXAMO_PROCEED_BUTTON.value))).click()
        time.sleep(10)

        paypal_email = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_EMAIL_FIELD.value)))
        paypal_email.send_keys(PaypalParameters.get_paypal_account_credentials("email"))

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_NEXT_BUTTON.value))).click()

        paypal_password = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_PASSWORD_FIELD.value)))
        paypal_password.send_keys(PaypalParameters.get_paypal_account_credentials("password"))

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_LOGIN_BUTTON.value))).click()

        submit_payment = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_PAY_NOW_BUTTON.value)))

        self.driver.execute_script("arguments[0].scrollIntoView();", submit_payment)
        time.sleep(5)
        submit_payment.click()
        time.sleep(5)
