import time
import allure

from src.page_objects.guest_app_po.phone_page import PhonePage
from src.parameters import email_parameters
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BillingDetails(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("StripePage.billing_details_fill_in() | Billing details fill in")
    def billing_details_fill_in(self, phone_number, country_name):
        time.sleep(5)
        email_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.BILLING_DETAILS_EMAIL.value)))
        email_field.click()
        email_field.clear()
        email_field.send_keys(email_parameters.get_outlook_credentials("username"))
        time.sleep(1)

        phone_page_object = PhonePage(self.driver)
        phone_page_object.insert_phone_number_and_country_code(phone_number, country_name)
        time.sleep(1)

        country_name_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.BILLING_DETAILS_COUNTY_NAME.value)))
        country_name_field.click()

        search_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.BILLING_DETAILS_COUNTRY_NAME_POPUP_SEARCH_FIELD.value)))
        search_field.click()
        search_field.clear()
        search_field.send_keys(country_name)
        time.sleep(1)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.COUNTRY_CODE_POPUP_FIRST_ITEM.value))).click()
        time.sleep(0.5)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.BILLING_DETAILS_CONTINUE_TO_PAYMENT_BUTTON.value))).click()

