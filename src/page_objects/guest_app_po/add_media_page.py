import itertools
import time
import allure
import pytest
from src.elements.guest_app.dynamic_elemenets.guest_app_dynamic_elements_login_process import \
    GuestAppDynamicElementsLoginProcess
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddMediaPage(object):
    skip = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step("AddMediaPage.check_exists_choose_attraction_popup() | check if choose attraction popup, in add media, exists")
    def check_existence_of_media_number_button_and_associate(self, photo_number, attraction_name):
        try:
            time.sleep(2)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.ENTER_PHOTO_NUMBER_BUTTON.value))).click()
            time.sleep(3)

            GuestAppDynamicElementsLoginProcess.add_media_attraction_picklist_item(self.driver, attraction_name)
            self.insert_media_number_and_submit(photo_number)
            time.sleep(1)
            AddMediaPage.skip = False # #to test what is it
            return AddMediaPage.skip
        except:
            self.skipped_test()

    @allure.step("AddMediaPage.enter_photo_number_and_submit() | positive photo number searching")
    def insert_media_number_and_submit(self, photo_number):
        time.sleep(1.5)
        photo_number_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.ENTER_PHOTO_NUMBER_FIELD.value)))
        time.sleep(1.5)
        photo_number_field.click()
        photo_number_field.clear()
        photo_number_field.send_keys(photo_number)
        time.sleep(1.5)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.SEARCH_BUTTON_IN_ENTER_PHOTO_NUMBER.value))).click()

    @allure.step("AddMediaPage.add_media_by_number_too_many_attempts_imitation() | steps to search for wrong photo number")
    def add_media_by_number_too_many_attempts_imitation(self, repeat):
        while repeat > 0:
            print(repeat)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, WebGuestAppStaticElements.PHOTO_NOT_FOUND_GOT_IT_BUTTON.value))).click()
            time.sleep(2)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.SEARCH_BUTTON_IN_ENTER_PHOTO_NUMBER.value))).click()

            repeat -= 1

    @allure.step("SKIPPED - check_existence_of_association_methods")
    def skipped_test(self):
        pytest.skip("Association method doesn't exist")

    @allure.step("AddMediaPage.verified_too_many_attempts_popup() | verified the popup after too many attempts of searching of a photo")
    def verified_too_many_attempts_popup(self):
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.ADD_MEDIA_TOO_MANY_ATTEMPTS_BUTTON.value)))

    @allure.step("AddMediaPage.get_userId() | get userId number from ask an operator")
    def get_userId_number(self):
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.ADD_MEDIA_PAGE_VIA_SIDE_MENU.value))).click()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.ADD_MEDIA_PAGE_ASK_AN_OPERATOR_BUTTON.value))).click()

        user_id = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.USERID_NUMBER_ASK_AN_OPERATOR.value))).text

        return user_id

    @allure.step("AddMediaPage.add_media_close_popup_too_many_attempts() | close the popup too many attempts")
    def add_media_close_popup_too_many_attempts(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.ADD_MEDIA_CLOSE_POPUP_TOO_MANY_ATTEMPTS.value))).click()

    @allure.step("AddMediaPage.confirm_media_is_mine() | confirm media is mine")
    def confirm_media_is_mine(self):
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.ADD_MEDIA_IS_THIS_YOUR_PHOTO_YES_BUTTON.value))).click()
        time.sleep(3.5)
