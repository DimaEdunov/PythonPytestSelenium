import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.angela.static_elemenets.angela_static_elements import AngelaStaticElements


class AngelaDynamicElementsPicklists:

    @staticmethod
    def customer_media_choose_park_picklist_item(driver, domain_name):
        select_park = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'%s')]" % domain_name)))
        actions = ActionChains(driver)
        actions.move_to_element(select_park).perform()
        time.sleep(1)
        select_park.click()

    @staticmethod
    def customer_media_choose_attraction_picklist_item(driver, attraction_name):
        select_attraction = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'%s')]" % attraction_name)))
        actions = ActionChains(driver)
        actions.move_to_element(select_attraction).perform()
        time.sleep(1)
        select_attraction.click()

    @staticmethod
    def search_customer_park_picklist_item(driver, domain_name):
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.OPEN_SEARCH_CUSTOMER_PARK_PICKLIST.value))).click()

        select_attraction = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'%s') and contains(@class,'q-item')]" % domain_name)))
        actions = ActionChains(driver)
        actions.move_to_element(select_attraction).perform()
        time.sleep(1)
        select_attraction.click()

    @staticmethod
    def customer_media_park_picklist_item(driver, domain_name):
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.CUSTOMER_MEDIA_PARK_PICKLIST.value))).click()

        select_attraction = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'%s') and contains(@class,'q-item')]" % domain_name)))
        actions = ActionChains(driver)
        actions.move_to_element(select_attraction).perform()
        time.sleep(1)
        select_attraction.click()

    @staticmethod
    def select_page_from_tool_bar(driver, page_name):
        tool_bar_pages = driver.find_elements(By.XPATH, AngelaStaticElements.TOOL_BAR_NAVIGATION.value)
        for one_page in tool_bar_pages:
            one_page_text = one_page.text
            if one_page_text == page_name:
                one_page.click()
                break
