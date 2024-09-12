import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait
from src.elements.angela.dynamic_elemenets.angela_dynamic_elements_picklists import AngelaDynamicElementsPicklists
from src.elements.angela.static_elemenets.angela_static_elements import AngelaStaticElements
from datetime import datetime, timedelta
from dateutil import parser


class CustomerMediaPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("CustomerMediaPage.angela_get_prefix_media_number() | angela get prefix media number")
    def angela_get_prefix_media_number(self, domain_name, attraction_name):
        # select park steps
        self.driver.refresh()
        time.sleep(12)
        customer_media_park_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.CUSTOMER_MEDIA_SELECT_PARK_PICKLIST.value)))
        customer_media_park_field.click()

        AngelaDynamicElementsPicklists.customer_media_choose_park_picklist_item(self.driver, domain_name)

        time.sleep(4)

        # select attraction steps
        customer_media_attraction_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, AngelaStaticElements.CUSTOMER_MEDIA_SELECT_ATTRACTION_PICKLIST.value)))
        customer_media_attraction_field.click()

        time.sleep(2)

        AngelaDynamicElementsPicklists.customer_media_choose_attraction_picklist_item(self.driver, attraction_name)

        time.sleep(2)

        # click on search button step
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.CUSTOMER_MEDIA_SEARCH_BUTTON.value))).click()

        time.sleep(5)

        # click on photo step
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.CUSTOMER_MEDIA_FIRST_PHOTO.value))).click()

        # get prefix media number steps
        get_prefix_media_number = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, AngelaStaticElements.MEDIA_DETAILS_PREFIX_PLUS_MEDIA_NUMBER.value)))
        full_prefix_media_number = get_prefix_media_number.text
        prefix_media_number_without_dash = full_prefix_media_number.replace("-", "")
        return prefix_media_number_without_dash
