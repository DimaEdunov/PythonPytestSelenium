import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from src.parameters import email_parameters
from src.parameters.guest_parameters import GuestParameters
from src.assistance_helper_services import driver_related_actions


class HelpAndSupportPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("HelpAndSupportPage.send_contact_us_form() | Send contact us form")
    def send_contact_us_form(self):
        time.sleep(1)

        email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                                           ((By.XPATH,
                                                             WebGuestAppStaticElements.CONTACT_US_EMAIL.value)))

        self.driver.execute_script("arguments[0].scrollIntoView();", email_field)
        time.sleep(1)
        email_field.click()
        email_field.send_keys(email_parameters.get_outlook_credentials("username"))

        location_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                                              ((By.XPATH,
                                                                WebGuestAppStaticElements.CONTACT_US_LOCATION.value)))
        self.driver.execute_script("arguments[0].scrollIntoView();", location_field)
        time.sleep(1)
        location_field.click()

        location_field_first_item = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                                                         ((By.XPATH,
                                                                           WebGuestAppStaticElements.CONTACT_US_LOCATION_FIRST_ITEM.value)))
        location_field_first_item.click()
        time.sleep(1)
        location_field_first_item.click()

        rides_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                                           ((By.XPATH,
                                                             WebGuestAppStaticElements.CONTACT_US_RIDES_FIELD.value)))

        self.driver.execute_script("arguments[0].scrollIntoView();", rides_field)
        time.sleep(1)

        rides_field.click()

        rides_field_first_item = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                                                      ((By.XPATH,
                                                                        WebGuestAppStaticElements.CONTACT_US_RIDES_FIELD_FIRST_ITEM.value)))
        rides_field_first_item.click()

        subject_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                                           ((By.XPATH,
                                                             WebGuestAppStaticElements.CONTACT_US_SUBJECT.value)))

        self.driver.execute_script("arguments[0].scrollIntoView();", subject_field)
        time.sleep(1)
        subject_field.click()
        subject_field.send_keys(GuestParameters.get_contact_us_form_credentials("subject"))

        iframe = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                                                      ((By.XPATH,
                                                                        WebGuestAppStaticElements.CONTACT_US_DESCRIPTION_IFRAME.value)))
        self.driver.switch_to.frame(iframe)

        description = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.CONTACT_US_BODY_DESCRIPTION.value)))

        description.send_keys(GuestParameters.get_contact_us_form_credentials("comments"))

        self.driver.switch_to.default_content()

        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.CONTACT_US_SUBMIT_BUTTON.value)))
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)

        submit_button.click()

    @allure.step("HelpAndSupportPage.contact_us_verification() | Contact us verification")
    def contact_us_verification(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.CONTACT_US_SENT_VERIFICATION.value)))

    @allure.step("HelpAndSupportPage.contact_us_open_verification() | Contact us open verification")
    def contact_us_form_open_verification(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.HELP_AND_SUPPORT_CONTACT_US_BUTTON.value))).click()

        time.sleep(2)
        contact_window = self.driver.window_handles[1]
        self.driver.switch_to.window(contact_window)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.CONTACT_US_HEADER.value)))

        self.driver.close()

        self.driver.switch_to.window(self.driver.window_handles[0])
