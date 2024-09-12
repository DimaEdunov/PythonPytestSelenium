import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from src.elements.ops_ui.dynamic_elemenets.opsui_dynamic_elements_picklists import OpsuiDynamicElementsPicklists
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements


class OpsUISearchByNumber(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("OpsUISearchByNumber.search_media_by_number() | Search media by number")
    def search_media_by_number(self, media_number, attraction_name):
        time.sleep(4)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_NUMBER_ATTRACTION_PICKLIST_FIELD.value))).click()

        OpsuiDynamicElementsPicklists.media_by_number_choose_attraction_picklist_item(self.driver, attraction_name)

        media_number_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_NUMBER_MEDIA_NUMBER_FIELD.value)))

        media_number_field.click()

        time.sleep(0.5)

        media_number_field.send_keys(media_number)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_NUMBER_SUBMIT_BUTTON.value))).click()

    @allure.step("OpsUISearchByNumber.search_media_negative_verification() | Verify invalid photo number in search field")
    def search_media_negative_verification(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, OpsuiAppStaticElements.GUEST_OR_MEDIA_DOES_NOT_EXIST_ERROR_POPUP.value)))

        print("debug - Media not found - test PASSED")
