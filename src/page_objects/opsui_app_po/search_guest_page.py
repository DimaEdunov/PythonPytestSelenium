import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements
from selenium.webdriver.support import expected_conditions as EC


class SearchGuestPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("SearchGuestPage.search_guest_by_qr_or_userid() |  Enter 'Guest Search' page")
    def search_guest_by_qr_or_userid(self, guest_to_search):

        time.sleep(1.5)

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               OpsuiAppStaticElements
                                               .GUEST_ID_QR_INSERT_FIELD.value))).click()

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               OpsuiAppStaticElements
                                               .GUEST_ID_QR_INSERT_FIELD.value))).clear()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ID_QR_INSERT_FIELD.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ID_QR_INSERT_FIELD.value))).send_keys(
            guest_to_search)

    @allure.step(
        "SearchGuestPage.guest_does_not_exist_verification() | Verify guest does not exist with deleted UserID inserted")
    def guest_does_not_exist_popup_verification(self):

        WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.GUEST_OR_MEDIA_DOES_NOT_EXIST_ERROR_POPUP.value)))

    @allure.step("SearchGuestPage.guest_search_verification() |  guest search verification")
    def guest_search_phone_verification(self, guest_phone_to_search):

        # A - Too short phone number, Negative test verification
        if len(guest_phone_to_search) <= len("9999123"):

            invalid_input_verification = self.driver.find_elements(By.XPATH, OpsuiAppStaticElements
                                                                   .PHONE_TEXT_FIELD_INVALID_INPUT_RED_INDICATION.value)

            if len(invalid_input_verification) == 1:
                print("Too short phone verification is on")
                pass
            else:
                assert False

        # B -  Valid non existing guest phone number
        else:
            time.sleep(1.5)
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                                 ((By.XPATH,
                                                   OpsuiAppStaticElements
                                                   .OPSUI_GUEST_SEARCH_CONFIRM_QR_CREATION_POPUP.value)))


            guest_creation_popup = self.driver.find_elements(By.XPATH, OpsuiAppStaticElements
                                                             .OPSUI_GUEST_SEARCH_CONFIRM_QR_CREATION_POPUP
                                                             .value)

            valid_input_verification = self.driver.find_elements(By.XPATH, OpsuiAppStaticElements
                                                                 .PHONE_TEXT_FIELD_VALID_INPUT_GREEN_INDICATION.value)

            if len(guest_creation_popup) == 1 and len(valid_input_verification) == 1:
                pass

            else:
                assert False

    @allure.step("SearchGuestPage.userid_verification() | UserId verification")
    def userid_too_short_verification(self):
        invalid_input_verification = self.driver.find_elements(By.XPATH, OpsuiAppStaticElements
                                                               .OPSUI_QR_USERID_INVALID_INPUT_VERIFICATION.value)
        no_submit_button_verification = self.driver.find_elements(By.XPATH, OpsuiAppStaticElements
                                                                  .OPSUI_GUEST_SUBMIT_CREATE_BUTTON.value)

        if len(invalid_input_verification) == 1 and len(no_submit_button_verification) == 0:
            print("Too short userid verification is on")
            pass