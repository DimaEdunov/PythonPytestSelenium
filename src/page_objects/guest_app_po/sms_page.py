import time
import allure

from src.elements.guest_app.dynamic_elemenets.guest_app_dynamic_elements_login_process import \
    GuestAppDynamicElementsLoginProcess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements


class SmsPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("LoginPage.sms_verification() | Insert sms verification code ")
    def sms_verification(self):
        time.sleep(4)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.SMS_INPUT_FIRST_CELL_WAIT_ELEMENT.value)))

        for cell_number in range(4):
            sms_cell = GuestAppDynamicElementsLoginProcess.sms_cells(self.driver, cell_number)

            sms_cell.send_keys("8")

        time.sleep(3)

