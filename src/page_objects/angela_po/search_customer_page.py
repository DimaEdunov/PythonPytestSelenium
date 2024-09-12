import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.elements.angela.dynamic_elemenets.angela_dynamic_elements_picklists import AngelaDynamicElementsPicklists
from src.elements.angela.static_elemenets.angela_static_elements import AngelaStaticElements


class SearchCustomerPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("SearchCustomerPage.search_guest_in_angela_by_user_id() | search guest in angela by user id")
    def search_guest_in_angela_by_user_id(self, get_user_id, park_name):
        AngelaDynamicElementsPicklists.search_customer_park_picklist_item(self.driver, park_name)

        time.sleep(6)
        user_id_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.SEARCH_CUSTOMER_USER_ID_OR_PHONE_FIELD.value)))
        user_id_field.click()
        time.sleep(2)
        user_id_field.send_keys(get_user_id)

        time.sleep(2)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, AngelaStaticElements.SEARCH_CUSTOMER_SEARCH_BUTTON_BY_USER_ID_OR_PHONE.value))).click()

        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.SEARCH_CUSTOMER_USER_FOUND.value))).click()

        time.sleep(2)