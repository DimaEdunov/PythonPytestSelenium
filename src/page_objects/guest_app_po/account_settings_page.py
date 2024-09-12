import time
import allure
from allure_commons.types import AttachmentType

from src.elements.guest_app.dynamic_elemenets.guest_app_dynemic_elements_settings import GuestAppDynemicElementsSettings
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountSettingsPage(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("FeedPage.change_guestapp_language() | Change language")
    def change_language(self, language):
        time.sleep(3)

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((
            By.XPATH, WebGuestAppStaticElements.ACCOUNT_SETTINGS_CHANGE_LANGUAGE_BUTTON.value))).click()

        click_on_language = GuestAppDynemicElementsSettings.settings_choose_language_element(self.driver, language)
        click_on_language.click()

    @allure.step("FeedPage.delete_user() | delete user")
    def delete_user(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.ACCOUNT_SETTINGS_PAGE_VIA_SIDE_MENU.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.ACCOUNT_SETTING_DELETE_ACCOUNT.value))).click()

        time.sleep(2.5)

        allure.attach(self.driver.get_screenshot_as_png(), name="test_etitlemenet_delete_guest_from_guest_app",
                      attachment_type=AttachmentType.PNG)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.CONFIRM_DELETE_ACCOUNT_POPUP.value))).click()

        time.sleep(1.5)

    @allure.step("FeedPage.new_user_verification() | new user popup verification")
    def new_user_verification(self, deleted_user_id, new_user_id):
        if deleted_user_id != new_user_id:
            assert True
        else:
            assert False
