import time

from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.elements.angela.static_elemenets.angela_static_elements import AngelaStaticElements
from src.parameters.angela_parameters import get_angela_login_credentials
class MenuPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("MenuPage.angela_login() | Login to angela")
    def angela_login(self):
        time.sleep(3)
        if len(self.driver.find_elements(By.XPATH, '//div[@class="flex justify-center items-center"]')) > 0:
            pass

        elif len(self.driver.find_elements(By.XPATH, AngelaStaticElements.ANGELA_LOGIN_REFFERANCE_ELEMENT.value)) > 0:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'(//button[@type="button"])[2]'))).click()
            time.sleep(2)

            azure_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//input[@value='Azure'])[2]")))
            time.sleep(3)
            azure_button.click()

        # login 2nd time
        elif len(self.driver.find_elements(By.XPATH,'//button[@class="button button button--rounded button--login button--secondary button--outline"]')) > 0:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="button button button--rounded button--login button--secondary button--outline"]'))).click()
        else:
        # Full login
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Azure AD ・ Pomvom Microsoft Account"]'))).click()

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="email"]'))).click()

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]'))).send_keys(get_angela_login_credentials('user'))

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]'))).click()
            time.sleep(5)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="password"]'))).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))).send_keys(get_angela_login_credentials('password'))
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]'))).click()

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="button button button--rounded button--login button--secondary button--outline"]'))).click()
            time.sleep(2)
            azure_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//input[@value='Azure'])[2]")))
            azure_button.click()


    @allure.step("MenuPage.go_to_customer_media() | go to customer media")
    def go_to_customer_media(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.CUSTOMER_MEDIA_BUTTON.value))).click()
        time.sleep(6)

    @allure.step("MenuPage.go_to_search_customer() | go to search customer")
    def go_to_search_customer(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.SEARCH_CUSTOMER_BUTTON.value))).click()
        time.sleep(6)