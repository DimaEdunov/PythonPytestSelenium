import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements


class GuestPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("GuestPage.verify_new_guest_was_created_correctly() |  Verify new guest was created correctly")
    def new_qr_creation_verification(self):
        not_paid_guest_button_indication = self.driver.find_elements \
            (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_ACTIVATED_NOT_PAID_BUTTON.value)

        add_media_by_number_button_indication = self.driver.find_elements(By
                                                                          .XPATH, OpsuiAppStaticElements
                                                                          .OPSUI_GUEST_PAGE_FIND_MEDIA_BY_NUMBER.value)

        add_media_by_attraction_button_indication = self.driver.find_elements \
            (By.XPATH, OpsuiAppStaticElements.
             OPSUI_GUEST_PAGE_FIND_MEDIA_BY_ATTRACTION.value)

        add_media_by_qr_button_indication = self.driver.find_elements \
            (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_FIND_MEDIA_BY_BY_QR.value)

        send_sms_button_indication = self.driver.find_elements \
            (By.XPATH, OpsuiAppStaticElements.
             OPSUI_GUEST_PAGE_SEND_SMS_BUTTON.value)

        if len(self.driver.find_elements(By.XPATH, OpsuiAppStaticElements.OPSUI_CREATE_USER_VERIFICATION.value)):
            pass
        else:
            assert False

    @allure.step("GuestPage.guest_exists_verification() | Verify guest exists with UserID inserted")
    def guest_exist_and_has_correct_id_verification(self, expected_guest_id, actual_guest_id):
        time.sleep(4)

        if expected_guest_id == actual_guest_id:
            pass
        else:
            assert False

    @allure.step("GuestPage.count_if_there_are_photos_in_attraction_page_positive_verefication() |  count if there are photos in attraction page positive verefication")
    def photos_in_guest_page_verification(self, test_status):
        time.sleep(1)
        photos_in_by_attraction = len(
            self.driver.find_elements(By.XPATH, OpsuiAppStaticElements.PHOTOS_IN_FEED.value))

        if test_status == "positive" and photos_in_by_attraction > 0 or test_status == "negative" and photos_in_by_attraction == 0:
            assert True
        else:
            print("Amount of photos in OpsUI gallery is not as expected")
            assert False

    @allure.step("GuestPage.remove_photo() | remove photo")
    def remove_photo(self, amount_of_photos_to_delete):
        for _ in range(amount_of_photos_to_delete):
            time.sleep(1)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, OpsuiAppStaticElements.GUEST_PAGE_PREVIEW_BUTTON.value))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   OpsuiAppStaticElements.REMOVE_FROM_PASS_BUTTON.value))).click()

    @allure.step("GuestPage.verify_photo_was_removed() | verify photo was removed")
    def verify_photo_was_removed(self, number_of_photos_before_remove, number_of_photos_after_remove):
        if number_of_photos_after_remove < number_of_photos_before_remove and number_of_photos_before_remove - number_of_photos_after_remove == 1:
            assert True
        else:
            assert False

    @allure.step("GuestPage.add_video_to_cart() | Add video to cart")
    def add_video_to_cart(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_VIDEO_THUMBNAIL.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_PREVIEW_BUTTON.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_ADD_TO_CART_BUTTON.value))).click()

    @allure.step("GuestPage.verify_video_added_to_cart() | Verify video added to cart")
    def verify_video_added_to_cart(self):
        remove_from_cart = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_REMOVE_FROM_CART.value)))

        time.sleep(1)

        if remove_from_cart:
            pass
        else:
            assert False

        time.sleep(1)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_PREVIEW_CLOSE_ICON.value))).click()

    @allure.step("GuestPage.add_entitlements_all_cart_items() | Add entitlements all cart items")
    def add_entitlements_all_cart_items(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_ENTITLEMENT_BUTTON.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_ENTITLEMENT_POPUP_ALL_CART_ITEMS.value))).click()

        time.sleep(2)

    @allure.step("GuestPage.add_entitlements_all_day_photos() | Add entitlements all day photos")
    def add_entitlements_all_day_photos(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_ENTITLEMENT_BUTTON.value))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_ENTITLEMENT_POPUP_ALL_PHOTOS.value))).click()

        time.sleep(2)

    @allure.step("GuestPage.go_to_entitlements_page_from_guest_page() | Go to entitlements page")
    def go_to_entitlements_page_from_guest_page(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_ENTITLEMENT_BUTTON.value))).click()

        time.sleep(2)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_ENTITLEMENT_POPUP_EDIT_ENTITLEMENT.value))).click()

    @allure.step("OpsUiSearchGuestPage.go_to_add_media_by_attraction_via_guest_page | Go to add media by attraction via guest page")
    def go_to_add_media_by_attraction_via_guest_page(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH, OpsuiAppStaticElements.OPSUI_GUEST_PAGE_FIND_MEDIA_BY_ATTRACTION.value))).click()
        time.sleep(1)
