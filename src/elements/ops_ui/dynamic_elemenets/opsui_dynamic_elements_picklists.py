import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements


class OpsuiDynamicElementsPicklists:

    @staticmethod
    @allure.step("OpsuiDynamicElementsPicklists.OpsuiDynamicElementsPicklists() | Choose attraction from picklist")
    def media_by_number_choose_attraction_picklist_item(driver, attraction_name):
        select_attraction = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'%s')]" % attraction_name)))
        actions = ActionChains(driver)
        actions.move_to_element(select_attraction).perform()
        time.sleep(1)
        select_attraction.click()


    @staticmethod
    @allure.step("OpsuiDynamicElementsPicklists.opsui_go_to_feature() | Navigate to a page on OpsUI")
    def opsui_go_to_feature(driver, expected_feature_name_text):
        time.sleep(2)
        selected_feature_element = driver.find_elements(By.XPATH, OpsuiAppStaticElements.MAIN_PAGE_FEATURES_BUTTONS.value)

        feature_button_element = driver.find_elements(By.XPATH, OpsuiAppStaticElements.MAIN_PAGE_FEATURES.value)

        for selected_feature_element, attraction_click_element in zip(selected_feature_element, feature_button_element):
            button_text = selected_feature_element.text
            time.sleep(1)
            if button_text == expected_feature_name_text:
                time.sleep(0.5)
                attraction_click_element.click()
                break
