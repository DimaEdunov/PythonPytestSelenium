import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements


class GuestAppDynamicElementsLoginProcess:

    @staticmethod
    def sms_cells(driver, cell_number):
        SMS_VERIFICATION_CELL = driver.find_element(By.XPATH, '//input[@id="code-%s"]' % cell_number)

        return SMS_VERIFICATION_CELL

    @staticmethod
    def add_media_attraction_picklist_item(driver, attraction_name):
        get_attractions_code = driver.find_elements(By.XPATH, WebGuestAppStaticElements.ATTRACTIONS_IN_CHOOSE_ATTRACTION_POPUP_GET_ID.value)
        attraction_click_elements = driver.find_elements(By.XPATH, WebGuestAppStaticElements.ATTRACTIONS_IN_CHOOSE_ATTRACTION_POPUP_CHOOSE_ATTRACTION.value)

        for attraction, attraction_click_element in zip(get_attractions_code, attraction_click_elements):
            print("attraction: " + str(attraction))
            attraction_code = attraction.get_attribute("id")
            if attraction_code == attraction_name.upper():
                attraction_click_element.click()
                time.sleep(1)
                break

    @staticmethod
    def select_taxamo_country_of_residence_picklist(driver, country):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='billingCountry']"))).click()
        time.sleep(1)
        select_country_of_residence = Select(driver.find_element(By.XPATH, "//select[@id='billingCountry']"))
        select_country_of_residence.select_by_value(country)


