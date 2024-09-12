import time
import allure

from src.assistance_helper_services import driver_related_actions
from src.elements.guest_app.static_elemenets.mobile_guest_app_static_elements import MobileGuestAppStaticElements
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MobileGuestAppPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("MobileGuestAppPage.login_verification() | Verify user is logged in")
    def mobile_login_verification(self):
        time.sleep(3)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, MobileGuestAppStaticElements.HAMBURGER_BUTTON.value)))

        time.sleep(1)

    @allure.step("MobileGuestAppPage.close_menu_in_mobile_by_clicking_on_background() | Close_menu")
    def mobile_close_menu_by_clicking_on_background(self):
        action = ActionChains(self.driver)
        action.move_by_offset(0, 8).perform()
        action.click()

    @allure.step("MobileGuestAppPage.logout() |logout out of guest app")
    def mobile_logout(self):
        time.sleep(5)
        hamburger_or_back_sign = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, MobileGuestAppStaticElements.HAMBURGER_BUTTON.value)))

        hamburger_or_back_sing_differance = hamburger_or_back_sign.get_attribute("style")
        if "364%205.63599L15.778%207.04999L10" in hamburger_or_back_sing_differance:
            hamburger_or_back_sign.click()
            time.sleep(2)
            hamburger_or_back_sign.click()

        else:
            hamburger_or_back_sign.click()

        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH, WebGuestAppStaticElements.SIDE_MENU_LOGOUT_BUTTON.value))).click()

        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.LOGOUT_POPUP_SUBMIT_LOGOUT.value))).click()

        driver_related_actions.delete_cookies(self.driver)
        self.driver.refresh()

    @allure.step("MobileGuestAppPage.click_on_hamburger_or_back_sign() | Click on hamburger or back sign")
    def click_on_hamburger_or_back_sign(self):
        time.sleep(3)
        hamburger_or_back_sign = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, MobileGuestAppStaticElements.HAMBURGER_BUTTON.value)))
        time.sleep(2)

        hamburger_or_back_sing_differance = hamburger_or_back_sign.get_attribute("style")
        if "364%205.63599L15.778%207.04999L10" in hamburger_or_back_sing_differance:
            hamburger_or_back_sign.click()
            time.sleep(2)
            hamburger_or_back_sign.click()

        else:
            time.sleep(1)
            hamburger_or_back_sign.click()

        time.sleep(1)

