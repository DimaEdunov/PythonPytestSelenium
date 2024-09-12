import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements


class GlobalOpsuiActions(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("GlobalOpsuiActions.get_guest_id() |  Get guest id from guest page")
    def get_guest_id(self):
        time.sleep(1)
        guest_page_guest_id_field = WebDriverWait(self.driver, 20) \
            .until(EC.visibility_of_element_located
                   ((By.XPATH, OpsuiAppStaticElements
                     .OPSUI_GUEST_ID_FIELD.value)))
        guest_id_number_expended = guest_page_guest_id_field.text
        string_to_get_id_from = ": "
        only_guest_id_number = (guest_id_number_expended
        [guest_id_number_expended.index(string_to_get_id_from) + len(string_to_get_id_from):])
        return only_guest_id_number

    @allure.step("GlobalOpsuiActions.go_to_home_page() |  go to home page")
    def go_to_home_page(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.HOME_BUTTON.value))).click()
        time.sleep(2)

    @allure.step("GlobalOpsuiActions.add_photo_to_guest() |  Add photo to guest")
    def add_photo_to_guest(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.ADD_TO_PASS_BUTTON.value))).click()

    @allure.step("GlobalOpsuiActions.verify_add_photo_to_guest() |  verify add photo to guest")
    def verify_add_photo_to_guest(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.PHOTO_DETAILS_VERIFICATION_POPUP.value)))

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OK_BUTTON_VERIFICATION_POPUP.value))).click()

    @allure.step("GlobalOpsuiActions.open_photo_details() |  Open photo details page, find media by number/attraction")
    def open_photo_details(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_FIRST_PHOTO.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.GUEST_PAGE_PREVIEW_BUTTON.value))).click()

    @allure.step("GlobalOpsuiActions.select_multiple_medias() |  select multiple medias")
    def count_how_many_photos_in_feed(self):
        time.sleep(1)
        photos_in_by_attraction = self.driver.find_elements(By.XPATH,
                                                            OpsuiAppStaticElements.PHOTOS_IN_FEED.value)
        photos_in_by_attraction_len = len(photos_in_by_attraction)

        return photos_in_by_attraction_len

    @allure.step("GlobalOpsuiActions.go_back_to_preview_page() |  go back to preview page")
    def go_back_to_preview_page(self):
        back_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, OpsuiAppStaticElements.BACK_BUTTON.value)))
        actions = ActionChains(self.driver)
        actions.move_to_element(back_button).click().perform()
