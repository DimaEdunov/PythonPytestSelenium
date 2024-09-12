import time
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements


class GlobalGuestSearchOpsui(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("GlobalGuestSearchOpsui.type_qr_or_userid() | Insert QR or UserID")
    def type_qr_or_userid(self, guest_to_search):

        time.sleep(2)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ID_QR_INSERT_FIELD.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ID_QR_INSERT_FIELD.value))).clear()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.GUEST_ID_QR_INSERT_FIELD.value))).send_keys(
            guest_to_search)

    @allure.step("GlobalGuestSearchOpsui.type_guest_phone() | Type guest phone number")
    def type_guest_phone(self, area_code_phone, guest_phone_number):
        phone_number_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.OPSUI_INSERT_PHONE_NUMBER_FIELD.value)))

        phone_number_field.click()
        time.sleep(1)

        phone_number_field.clear()
        time.sleep(1)

        phone_number_field.send_keys(area_code_phone + guest_phone_number)
        time.sleep(0.5)

    @allure.step("GlobalGuestSearchOpsui.click_on_create() | Create new guest")
    def click_on_create(self):

        time.sleep(6)

        verification_of_create_button1 = "Create"
        verification_of_create_button2 = "Crear"

        submit_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_SUBMIT_CREATE_BUTTON.value))).text

        if verification_of_create_button1 or verification_of_create_button2 in submit_button:
            time.sleep(1.5)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                                 ((By.XPATH,
                                                   OpsuiAppStaticElements.OPSUI_GUEST_SUBMIT_CREATE_BUTTON.value))).click()

            WebDriverWait(self.driver, 20) \
                .until(EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_SEARCH_CONFIRM_QR_CREATION_POPUP.value)))
        else:
            assert False

    @allure.step("GlobalGuestSearchOpsui.click_on_submit() | Click on Submit search")
    def click_on_submit(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20) \
            .until(EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements
                                               .OPSUI_GUEST_SUBMIT_CREATE_BUTTON.value))).click()
