import time
import allure

from src.parameters.paypal_parameters import PaypalParameters
from src.parameters.taxamo_parameters import TaxamoParameters
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step(
        "StripePage.stripe_payment_process_with_credit_card() | Stripe payment process with credit card")
    def stripe_payment_process_with_credit_card(self):
        time.sleep(16)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_CREDIT_CARD_BUTTON.value))).click()
        time.sleep(6)
        iframe_card = self.driver.find_elements(By.XPATH,
                                                WebGuestAppStaticElements.PAYMENT_PAGE_IFRAME_CREDIT_CARD.value)
        time.sleep(6)
        self.driver.switch_to.frame(iframe_card[0])

        card_number_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_CARD_NUMBER_STRIPE.value)))

        self.driver.execute_script("arguments[0].scrollIntoView();", card_number_field)

        card_number_field.click()

        time.sleep(5)

        card_number_field.send_keys(TaxamoParameters.get_credit_card_credentials("card_number"))

        expire_date_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_EXPIRATION_DATE_STRIPE.value)))
        expire_date_field.click()
        expire_date_field.send_keys(TaxamoParameters.get_credit_card_credentials("expire_date"))

        cvc_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_CVC_STRIPE.value)))
        cvc_field.click()
        cvc_field.send_keys(TaxamoParameters.get_credit_card_credentials("cvc_number"))

        time.sleep(5)
        self.driver.switch_to.default_content()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_PAY_BUTTON.value))).click()

    @allure.step(
        "StripePage.stripe_payment_process_with_paypal() | Stripe payment process with paypal")
    def stripe_payment_process_with_paypal(self):
        self.driver.refresh()
        time.sleep(10)
        card_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_CREDIT_CARD_BUTTON.value)))

        self.driver.execute_script("arguments[0].scrollIntoView();", card_field)

        paypal_outer_iframe = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_PAYPAL_BUTTON_IFRAME.value)))

        self.driver.switch_to.frame(paypal_outer_iframe)

        paypal_inner_iframe = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_PAYPAL_BUTTON_IFRAME_2.value)))

        self.driver.switch_to.frame(paypal_inner_iframe)

        paypal_inner_iframe_2 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_PAYPAL_BUTTON_IFRAME_3.value)))

        self.driver.switch_to.frame(paypal_inner_iframe_2)
        time.sleep(3)

        paypal_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.PAYMENT_PAGE_PAYPAL_BUTTON.value)))

        self.driver.execute_script("arguments[0].scrollIntoView();", paypal_button)
        paypal_button.click()
        time.sleep(1)

        paypal_popup = self.driver.window_handles[1]
        self.driver.switch_to.window(paypal_popup)

        paypal_email = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_EMAIL_FIELD.value)))

        paypal_email.send_keys(PaypalParameters.get_paypal_account_credentials("email"))

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_NEXT_BUTTON.value))).click()

        paypal_password = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_PASSWORD_FIELD.value)))
        paypal_password.send_keys(PaypalParameters.get_paypal_account_credentials("password"))

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_LOGIN_BUTTON.value))).click()

        submit_payment = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.PAYPAL_PAGE_PAY_NOW_BUTTON.value)))

        self.driver.execute_script("arguments[0].scrollIntoView();", submit_payment)
        time.sleep(5)
        submit_payment.click()
        time.sleep(15)

        guest_app_window = self.driver.window_handles[0]
        self.driver.switch_to.window(guest_app_window)

    @allure.step("StripePage.verify_tax_calculation() | Verify tax calculation")
    def verify_tax_calculation_includes_in_page(self, country_name):
        time.sleep(20)
        checkout_details = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.CHECKOUT_SUMMERY_DETAILS.value)
        len_checkout_details = len(checkout_details)

        if country_name == "Israel" and len_checkout_details == 1:
            assert True
        elif country_name == "Germany" and len_checkout_details == 3:
            assert True
        else:
            print("len_checkout_details" + str(len_checkout_details))
            assert False




#############
    @allure.step("FeedPage.verify_payment_success() | verify payment success")
    def verify_payment_success(self):
        time.sleep(15)
        go_to_feed_button = self.driver.find_elements(By.XPATH,
                                                      WebGuestAppStaticElements.PAYMENT_SUCCESS_FEED_BUTTON.value)

        if len(go_to_feed_button) > 0:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.PAYMENT_SUCCESS_FEED_BUTTON.value))).click()
            time.sleep(1)
        else:
            assert False



    @allure.step("FeedPage.add_email() | add my email to the billing page")
    def add_email_and_continue_to_payment(self):
        time.sleep(6)
        my_email = "feigin.nast@gmail.com"
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, WebGuestAppStaticElements.BILLING_DETAILS_EMAIL.value))
        )
        email_input.send_keys(my_email)
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.BILLING_DETAILS_CONTINUE_TO_PAYMENT_BUTTON.value))).click()
        time.sleep(6)

    @allure.step("FeedPage.back_to_the_feed() | back to the feed after payment")
    def back_to_the_feed(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.SHARE_YOUR_MOMENTS_BUTTON.value))).click()




        pass