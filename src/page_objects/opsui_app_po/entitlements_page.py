import time
from datetime import date
from enum import Enum
import datetime

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.parameters.guest_parameters import GuestParameters
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil import parser


class EntitlementsPage(object):

    def __init__(self, driver):
        self.driver = driver

    ONE_DAY_PASS = "1 days pass"

    @allure.step("EntitlementsPage.entitlements_page_opened_verification() |  Verify entitlements page opened")
    def entitlements_page_opened_verification(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.GUEST_APP_ENTITLEMENT_PAGE_VERIFICATION.value)))

        print("Wohoooo!!!")

    @allure.step("OpsUiHomePage.entitlements_verify_phone_number() |  entitlements verify phone number")
    def entitlements_verify_phone_number(self, guest_phone_number):
        time.sleep(5)
        get_country_code_string = str(GuestParameters.get_country_code_without_plus_prefix("Israel"))
        guest_phone_number_with_country_code = get_country_code_string + guest_phone_number
        print(guest_phone_number_with_country_code)

        guest_phone_number = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ENTITLEMENT_PHONE_NUMBER.value))).text

        phone_number_only = guest_phone_number[-11:]
        print(phone_number_only)

        print(phone_number_only)
        print(guest_phone_number_with_country_code)

        if guest_phone_number_with_country_code in phone_number_only:
            assert True
        else:
            assert False

    @allure.step("OpsUiHomePage.add_entitlement_to_guest() |  add entitlement to guest")
    def add_entitlement_to_guest(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ENTITLEMENT_ADD_BUTTON.value))).click()

        entitlement = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ENTITLEMENT_ONE_DAY_PASS_BUTTON.value)))

        time.sleep(1)
        entitlement_text = entitlement.text

        entitlement.click()

        return entitlement_text

    @allure.step("OpsUiHomePage.verify_entitlement_added_to_guest() |  verify entitlement added to guest")
    def verify_entitlement_added_to_guest(self, entitlement_type_element_reference, element):
        global start_date
        entitlement_type_element_value = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, element))).text

        if entitlement_type_element_reference == entitlement_type_element_value:

            print("entitlement_type_element_reference: " + str(entitlement_type_element_reference))
            time.sleep(5)
            if entitlement_type_element_reference == "All Photos":
                start_date = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ENTITLEMENT_START_DATE_FIRST.value))).text
            elif entitlement_type_element_reference == "Video":
                start_date = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ENTITLEMENT_START_DATE_SECOND.value))).text
            else:
                print("in else - 1 day pass")
                start_date = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ENTITLEMENT_START_DATE_FIRST.value))).text

            current_date = date.today()
            current_date_and_time_raw_like_web = current_date.strftime("%d.%m.%y")
            print("current_date_and_time_raw_like_web: " + str(current_date_and_time_raw_like_web))

            if start_date == current_date_and_time_raw_like_web and entitlement_type_element_value == entitlement_type_element_reference:
                assert True
            else:
                assert False

    @allure.step("OpsUiHomePage.remove_entitlement_to_guest() |  remove entitlement to guest")
    def remove_entitlement_to_guest(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.OPSUI_GENERAL_X_BUTTON.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.REMOVE_ENTITLEMENT_YES_BUTTON_POPUP.value))).click()
        time.sleep(3)
