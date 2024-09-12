import os
import time
import allure
from selenium.webdriver.common.action_chains import ActionChains
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("FeedPage.verify_all_photos_added_to_cart() | Verify all photos added to cart")
    def verify_all_media_added_to_cart(self, number_or_item_type_expected):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FEED_PAGE_NAVIGATION_BAR_CART_BUTTON.value))).click()
        time.sleep(1)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FEED_PAGE_PROCEED_TO_CART_BUTTON.value))).click()
        time.sleep(1)

        number_of_items_and_type_item = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.CART_PAGE_ITEM_TYPE_AND_NUMBER_OF_ITEMS.value)))

        number_of_items_text = number_of_items_and_type_item.text

        if number_or_item_type_expected in number_of_items_text:
            assert True
        else:
            assert False

    @allure.step("FeedPage.verify_all_photos_added_to_cart() | Verify all photos added to cart")
    def proceed_to_payment(self):
        print("proceed_to_payment method")


        time.sleep(5)
        # Wait for the button to be clickable
        proceed_to_payment = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.CART_PAGE_PROCEED_TO_PAYMENT_BUTTON.value)))

        proceed_to_payment.click()

        # # Coordinates relative to the top-left corner of the button
        # # Use ActionChains to move to the specific coordinates and click
        # actions1 = ActionChains(self.driver)
        # actions1.move_to_element_with_offset(proceed_to_payment, 257, 10).click().perform()
        # print("1")
        # time.sleep(4)
        #
        # actions2 = ActionChains(self.driver)
        # actions2.move_to_element_with_offset(proceed_to_payment, 257, 20).click().perform()
        # print("1")
        # time.sleep(4)
        #
        # actions3 = ActionChains(self.driver)
        # actions3.move_to_element_with_offset(proceed_to_payment, 257, 30).click().perform()
        # print("1")
        # time.sleep(4)
        #
        # actions4 = ActionChains(self.driver)
        # actions4.move_to_element_with_offset(proceed_to_payment, 257, 40).click().perform()
        # print("1")
        #
        # actions5 = ActionChains(self.driver)
        # actions5.move_to_element_with_offset(proceed_to_payment, 257, 50).click().perform()
        # print("1")
        time.sleep(6)

        print("Proceed to payment button found")








    @allure.step("FeedPage.add_first_media_to_cart | the first and second media were added to the cart")
    def add_first_and_second_media_to_cart(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FIRST_UNPAID_MEDIA_BLOCK.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.SECOND_UNPAID_MEDIA_BLOCK.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.BUY_NOW_BUTTON_FEED.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.SPECIAL_OFFER_NO_THANKS.value))).click()
        time.sleep(2)
        # verify the user redirect to the cart and there are 2 items
        assert self.driver.current_url.endswith("/cart"), \
            f"Expected URL to end with '/cart' but got '{self.driver.current_url}'"

        media_items = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_IN_THE_CART.value)
        print(f"The number of media in the cart {len(media_items)}")
        assert len(media_items) == 2, f"Expected 2 media items in the cart but found {len(media_items)}"


    @allure.step("FeedPage.delete_item_from_cart_list() | Verify all photos added to cart")
    def delete_item_from_cart_list(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.DELETE_FIRST_MEDIA_FROM_CART.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.APPROVE_DELETE_MEDIA_FROM_CART.value))).click()
        media_items = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_IN_THE_CART.value)
        print(f"The number of media in the cart {len(media_items)}")
        assert len(media_items) == 1, f"Expected 1 media items in the cart but found {len(media_items)}"

    @allure.step("FeedPage.verify_all_photos_added_to_cart() | Verify all photos added to cart")
    def continue_shopping(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.CONTINUE_SHOPPING.value))).click()
        assert self.driver.current_url.endswith("/feed"), \
            f"Expected URL to end with '/feed' but got '{self.driver.current_url}'"



    @allure.step("FeedPage.verify_all_photos_added_to_cart() | Verify all photos added to cart")
    def add_third_media_to_cart(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.THIRD_UNPAID_MEDIA_BLOCK.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.BUY_NOW_BUTTON_FEED.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.SPECIAL_OFFER_NO_THANKS.value))).click()
        time.sleep(2)
        # verify the user redirect to the cart and there are 2 items
        assert self.driver.current_url.endswith("/cart"), \
            f"Expected URL to end with '/cart' but got '{self.driver.current_url}'"

        media_items = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_IN_THE_CART.value)
        print(f"The number of media in the cart {len(media_items)}")
        assert len(media_items) == 2, f"Expected 2 media items in the cart but found {len(media_items)}"



#     @allure.step("FeedPage.verify_all_photos_added_to_cart() | Verify all photos added to cart")
#     def proceed_to_payment(self):
#         pass
# #     new_feed_page_object.finish_the_payment()
#     @allure.step("FeedPage.verify_all_photos_added_to_cart() | Verify all photos added to cart")
#     def proceed_to_payment(self):
#         pass
# #     new_feed_page_object.verify_media_is_unwatermarked()

