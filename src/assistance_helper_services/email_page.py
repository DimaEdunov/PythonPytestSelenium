import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.parameters import email_parameters
from src.elements.gmail.gmail_static_elements import GmailStaticElements


class EmailPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("EmailPage.email_login() | Email_login")
    def email_login(self):
        time.sleep(1)

        login_email_box = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, GmailStaticElements.INSERT_EMAIL_FIELD.value)))
        login_email_box.click()
        login_email_box.send_keys(email_parameters.get_outlook_credentials("username"))

        next_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, GmailStaticElements.LOGIN_SUBMIT_BUTTON.value)))
        next_button.click()

        time.sleep(2)

        password_box = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, GmailStaticElements.INSERT_PASSWORD_FIELD.value)))
        password_box.send_keys(email_parameters.get_outlook_credentials("password"))

        next_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, GmailStaticElements.LOGIN_SUBMIT_BUTTON.value)))
        next_button.click()

        time.sleep(15)
        print('Login to Gmail Successful...!!')

    @allure.step("EmailPage.confirm_email_received() | Confirm_email_received")
    def confirm_email_received(self):
        amount_of_tickets = len(self.driver.find_elements(By.XPATH, GmailStaticElements.FIRST_EMAIL_ITEM_IN_LIST.value))
        if amount_of_tickets > 0:
            assert True
        else:
            assert False

    @allure.step("EmailPage.delete_email() | Delete_email")
    def delete_email(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, GmailStaticElements.OPEN_SELECT_ALL_BUTTON_SELECTION.value))).click()

        time.sleep(1)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, GmailStaticElements.SELECT_ALL_BUTTON.value))).click()

        time.sleep(1)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, GmailStaticElements.DELETE_ALL.value))).click()

        time.sleep(2)

        delete_popup = len(self.driver.find_elements(By.XPATH, GmailStaticElements.DELETE_ITEMS_CONFIRM.value))
        print("Delete all item element - LEN : " + str(delete_popup))

        self.driver.find_element(By.XPATH, GmailStaticElements.DELETE_ITEMS_CONFIRM.value).send_keys(Keys.ENTER)

        time.sleep(20)



