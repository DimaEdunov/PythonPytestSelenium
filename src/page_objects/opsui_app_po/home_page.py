import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements
from src.parameters.opsui_parameters import OpsuiAppParameters


class OpsuiHomePage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("OpsuiHomePage.login() |Login to OpsUI")
    def opsui_login(self):
        self.driver.refresh()
        time.sleep(5)
        # user not logged in

        # flow A - partial login
        if len(self.driver.find_elements(By.XPATH, OpsuiAppStaticElements.OPSUI_HOMEPAGE_LOGO.value)) == 0:

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.CLOUDFLARE_PAGE_AZURE_AD_BUTTON.value))).click()

            time.sleep(4)
            # flow B - full login
            if len(self.driver.find_elements(By.XPATH, OpsuiAppStaticElements.INSERT_EMAIL_FIELD.value)) == 1:

                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.INSERT_EMAIL_FIELD.value))).click()

                time.sleep(0.5)

                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.INSERT_EMAIL_FIELD.value))).send_keys(
                    OpsuiAppParameters.get_opsui_login_credentials('user'))

                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.LOGIN_SUBMIT_BUTTON.value))).click()

                time.sleep(1.5)

                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.INSERT_PASSWORD_FIELD.value))).click()

                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.INSERT_PASSWORD_FIELD.value))) \
                    .send_keys(OpsuiAppParameters.get_opsui_login_credentials('password'))
                time.sleep(1)

                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.LOGIN_SUBMIT_BUTTON.value))).click()

                # WebDriverWait(self.driver, 20).until(
                #     EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.LOGIN_SUBMIT_BUTTON.value))).click()
            else:
                pass
        else:
            # flow C - login not required
            pass

    @allure.step("OpsUiHomePage.login_verification() |  Verification of OpsUi login")
    def login_verification(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, OpsuiAppStaticElements.OPSUI_HOMEPAGE_LOGO.value)))

        time.sleep(6)

    @allure.step("OpsUiHomePage.change_language_to_English() |  Change language to English")
    def change_language_to_english(self):
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.LANGUAGE_BUTTON.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.ENGLISH_PICKLIST.value))).click()



