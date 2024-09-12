import os
import time

import pyautogui
from selenium.webdriver import ActionChains
# from lib2to3.pgen2 import driver
from six.moves import urllib

import allure
from selenium import webdriver
from selenium.common import TimeoutException

from src.assistance_helper_services import driver_related_actions
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from seleniumwire import webdriver



def self(args):
    pass


class FeedPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("FeedPage.login_verification() | Verify user is logged in")
    def login_verification(self):
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.HOME_SCREEN_SIDEMENU_LOGIN_VERIFICATION.value)))

    @allure.step("FeedPage.logo_verification() | Verify there is a park logo")
    def ui_logo_verification(self):
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.PARK_LOGO.value)))
        print("the logo is appear")

    @allure.step("FeedPage.SpecialBanner_verification() | Verify there is a special offer banner")
    def ui_special_banner_verification(self):
        time.sleep(3)
        special_offer = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, WebGuestAppStaticElements.SPECIAL_OFFER_BANNER.value)))
        special_offer_text = special_offer.text.strip()
        if len(special_offer_text) > 0:
            print("the special banner appears")
            print(f'the Special Offer text is: {special_offer_text}')
            return True
        else:
            return False


    @allure.step("FeedPage.attraction_name_verification() | Verify there is a attraction name")
    def ui_attraction_name_verification(self):
        time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WebGuestAppStaticElements.ATTRACTION_NAME_NEW_FEED.value)))

        attraction_name = element.text.strip()
        if len(attraction_name) > 0:
            print("the attraction name appears")
            return True
        else:
            return False
        print(f"The attraction name is: {attraction_name}")

    @allure.step("FeedPage.attraction_location_verification() | Verify there is a location verification")
    def ui_attraction_location_verification(self):
        time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WebGuestAppStaticElements.ATTRACTION_LOCATION_NEW_FEED.value)))
        print("the attraction location appears")
        assert element.is_displayed(), "Element is found but not visible"
        assert element.text.strip(), "Element is visible but the field is empty."
        print(f"Element is visible with text: {element.text}")

    @allure.step("FeedPage.date_of_media_verification() | Verify there is a media date")
    def ui_date_of_media_verification(self):
        time.sleep(3)
        date_element = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_DATE_NEW_FEED.value)
        if len(date_element) > 0:
            print(f"the length of the date media is: {len(date_element)}")
        else:
            assert False

    @allure.step("FeedPage.media_tag_verification() | Verify there is a media TAG")
    def ui_media_tag_verification(self):
        time.sleep(3)
        elements = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_MARK.value)
        if len(elements) > 0:
            print(f"the length of the media mark is: {len(elements)}")
        else:
            assert False

    @allure.step("FeedPage.heart_button_verification() | heart_button_verification")
    def ui_heart_button_verification(self):
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_HEART_ICON.value)))
        print("the heart icon appears")

    @allure.step("FeedPage.three_dots_button_verification() | three_dots_button_verification")
    def ui_three_dots_button_verification(self):
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_THREE_DOTS_ICON.value)))
        print("the three dots icon appears")

    @allure.step("LoginPage.logout() |logout out of guest app")
    def logout(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH, WebGuestAppStaticElements.SIDE_MENU_LOGOUT.value))).click()

        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.LOGOUT_POPUP_SUBMIT_LOGOUT.value))).click()

        time.sleep(6)

        driver_related_actions.delete_cookies(self.driver)
        self.driver.refresh()
        time.sleep(6)

    @allure.step("FeedPage.verified_photo_with_watermark_or_not() | verified photo with watermark or not")
    def verify_if_photo_with_watermark_or_not(self, watermark_expected_result):
        time.sleep(2)

        get_photo_watermark_status = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.ASSOCIATED_GUEST_MEDIA_IN_GALLERY.value))).get_attribute(
            "data-is-locked")

        if get_photo_watermark_status == "true":
            watermark_actual_result = True
        elif get_photo_watermark_status == "false":
            watermark_actual_result = False
        else:
            return None

        if watermark_actual_result == watermark_expected_result:
            pass
        elif watermark_actual_result != watermark_expected_result:
            print("The photo watermark status is different from the expected")
            assert False

    @allure.step(
        "FeedPage.go_to_taxamo_payment_page_or_billing_details() | go to taxamo payment page or billing details")
    def go_to_taxamo_payment_page_or_billing_details(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.MARKETING_BANNER.value))).click()

        time.sleep(3)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.BUY_BUTTON.value))).click()

        time.sleep(2)

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

    @allure.step(
        "FeedPage.media_with_watermark_share_and_download_buttons_directed_to_payment_page() | media with watermark share and download buttons directed to payment page")
    def media_with_watermark_share_and_download_buttons_directed_to_payment_page(self, buttons_share_and_download_name):
        if buttons_share_and_download_name == "link":
            # scroll down
            time.sleep(2)
            link_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_MEDIA_LINK_BUTTON.value)))

            self.driver.execute_script("arguments[0].scrollIntoView();", link_button)
            time.sleep(2)

            # link button verification
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_MEDIA_LINK_BUTTON.value))).click()

        if buttons_share_and_download_name == "download":
            # scroll down
            link_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_MEDIA_LINK_BUTTON.value)))

            self.driver.execute_script("arguments[0].scrollIntoView();", link_button)
            time.sleep(2)

            # download button verification
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_DOWNLOAD_BUTTON.value))).click()

        if buttons_share_and_download_name == "share":
            # share button verification
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_SHARE_BUTTON.value))).click()

    @allure.step(
        "FeedPage.media_with_watermark_verify_share_and_download_buttons_directed_to_payment_page() | media with watermark verify share and download buttons directed to payment page")
    def verify_media_with_watermark_verify_share_and_download_buttons_directed_to_payment_page(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, WebGuestAppStaticElements.BUY_BUTTON.value)))
        time.sleep(2)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.GUEST_APP_GO_BACK_BUTTON.value))).click()
        time.sleep(2)

    @allure.step(
        "FeedPage.media_unwatermark_share_and_download_buttons() | media unwatermark share and download buttons")
    def media_unwatermark_share_and_download_buttons(self, buttons_share_and_download_name):

        if buttons_share_and_download_name == "link":
            time.sleep(2)
            # scroll down
            link_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_MEDIA_LINK_BUTTON.value)))

            self.driver.execute_script("arguments[0].scrollIntoView();", link_button)
            time.sleep(3)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_MEDIA_LINK_BUTTON.value))).click()

        if buttons_share_and_download_name == "download":
            # scroll down
            link_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_MEDIA_LINK_BUTTON.value)))

            self.driver.execute_script("arguments[0].scrollIntoView();", link_button)
            time.sleep(3)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_DOWNLOAD_BUTTON.value))).click()

            time.sleep(2)

    @allure.step("FeedPage.media_unwatermark_share_and_download_verify() | media unwatermark share and download verify")
    def media_unwatermark_share_and_download_verify(self, buttons_share_and_download_name):
        if buttons_share_and_download_name == "link":
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.GUEST_APP_IMAGE_LINK_COPIED_TO_YOUR_CLIPBOARD_POPUP.value)))

            time.sleep(2)

        if buttons_share_and_download_name == "download":
            path = r'c:\web-automation-downloads'
            source_dir = path
            file_names = os.listdir(source_dir)
            print(file_names)
            if len(file_names) > 0:
                assert True
                time.sleep(2)
            else:
                assert False

        if buttons_share_and_download_name == "facebook":
            time.sleep(4)
            facebook_window = self.driver.window_handles[1]
            self.driver.switch_to.window(facebook_window)

            current_url = self.driver.current_url
            print(current_url)

            if "facebook" in current_url:
                assert True
                self.driver.close()
                time.sleep(1)
                guest_app_window = self.driver.window_handles[0]
                self.driver.switch_to.window(guest_app_window)
                time.sleep(2)
            else:
                assert False

    @allure.step("FeedPage.add_photo_to_cart() | Add photo to cart")
    def add_photo_to_cart(self):
        all_photos_in_feed = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.FEED_PAGE_ALL_PHOTOS.value)

        add_to_cart_buttons = self.driver.find_elements(By.XPATH,
                                                        WebGuestAppStaticElements.FEED_PAGE_ADD_TO_CART_BUTTONS.value)

        add_to_cart_buttons_exclude_first_elements = add_to_cart_buttons[1:]

        for one_photo, add_to_cart_buttons_exclude_first_element in zip(all_photos_in_feed,
                                                                        add_to_cart_buttons_exclude_first_elements):
            self.driver.execute_script("arguments[0].scrollIntoView();", one_photo)
            time.sleep(10)
            add_to_cart_buttons_exclude_first_element.click()
            break

    @allure.step("FeedPage.add_first_video_to_cart() | Add first video to cart")
    def add_first_video_to_cart(self):
        all_videos_in_feed = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.FEED_PAGE_ALL_VIDEOS.value)

        add_to_cart_buttons = self.driver.find_elements(By.XPATH,
                                                        WebGuestAppStaticElements.FEED_PAGE_ADD_TO_CART_BUTTONS.value)

        add_to_cart_buttons_exclude_first_elements = add_to_cart_buttons[1:]

        for one_video, add_to_cart_button in zip(all_videos_in_feed, add_to_cart_buttons):
            self.driver.execute_script("arguments[0].scrollIntoView();", one_video)
            time.sleep(10)
            add_to_cart_button.click()
            break

        @allure.step("FeedPage.download_button_action_functionality() | download button should mark media as selected ")
        def download_button_action(self):
            time.sleep(3)

        @allure.step("FeedPage.share_button_action_functionality() | share button should mark media as selected ")
        def share_button_action(self):
            time.sleep(3)

    @allure.step(
        "FeedPage.three_dots_delete_content() | delete the media and sent in console event to mixpanel")
    def three_dots_delete_content(self):
        # how many media we have:
        initial_media_count = len(self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_BLOCKS.value))
        print(f'The count of the media blocks is {initial_media_count}')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_THREE_DOTS_ICON.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.DELETE_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.DELETE_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentDeletedClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        return initial_media_count

    @allure.step("FeedPage.count_media_after_delete_action() | verify the media was deleted")
    def count_media_after_delete_action(self, initial_media_count):
        time.sleep(5)
        # How media we have now
        final_media_count = len(self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_BLOCKS.value))
        time.sleep(5)
        assert final_media_count == initial_media_count - 1, "Media was not deleted successfully"
        print("Photo/video successfully deleted.")
        print(f'The count of the media blocks is {final_media_count}')

    @allure.step(
        "FeedPage.three_dots_report_content()() | report the media and sent in console event to mixpanel")
    def three_dots_report_content(self):
        time.sleep(5)
        initial_media_count = len(self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_BLOCKS.value))
        print(f'The count of the media blocks is {initial_media_count}')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_THREE_DOTS_ICON.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.REPORT_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.REPORT_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentReportedClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        return initial_media_count

    @allure.step("FeedPage.count_media_after_report_content_action() | verify the media was deleted")
    def count_media_after_report_content_action(self, initial_media_count):
        final_media_count = len(self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_BLOCKS.value))
        assert final_media_count == initial_media_count - 1, "Media was not deleted successfully"
        print("Photo/video successfully deleted.")
        print(f'The count of the media blocks is {final_media_count}')

    @allure.step(
        "FeedPage.three_dots_not_my_content | report the media is not my and sent in console event to mixpanel")
    def three_dots_not_my_content(self):
        time.sleep(5)
        initial_media_count = len(self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_BLOCKS.value))
        print(f'The count of the media blocks is {initial_media_count}')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_THREE_DOTS_ICON.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.NOT_MY_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.NOT_MY_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentNotRelevantClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        return initial_media_count

    @allure.step("FeedPage.count_media_after_not_my_content_action() | verify the media was deleted")
    def count_media_after_not_my_content_action(self, initial_media_count):
        time.sleep(5)
        final_media_count = len(self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.MEDIA_BLOCKS.value))
        assert final_media_count == initial_media_count - 1, "Media was not deleted successfully"
        print("Photo/video successfully deleted.")
        print(f'The count of the media blocks is {final_media_count}')

    @allure.step("FeedPage.two_media_in_the_row() | two_media_in_the_row_verification()")
    def ui_two_media_in_the_row(self):

        media_blocks = WebDriverWait(self.driver, timeout=20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="media-block"]')))
        first_media_block = media_blocks[0].location['y']
        second_media_block = media_blocks[1].location['y']
        third_media_block = media_blocks[2].location['y']

        assert first_media_block == second_media_block, "The first two elements are not in the same row"
        assert third_media_block != first_media_block, "More than two elements in the first row"
        print("The first row contains exactly two elements.")

    @allure.step("FeedPage.one_media_in_row() | after click the feed diaplay 1 media in the row()")
    def one_media_in_row(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.DISPLAY_ONE_MEDIA_BUTTON.value))).click()
        time.sleep(5)
        media_blocks = WebDriverWait(self.driver, timeout=20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="media-block"]')))
        first_media_block = media_blocks[0].location['y']
        second_media_block = media_blocks[1].location['y']
        assert second_media_block != first_media_block, "More than 1 element in the first row"
        print("The first row contains exactly 1 element.")
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.DISPLAY_TWO_MEDIA_BUTTON.value))).click()

    @allure.step("FeedPage.heart_on_button_verification | Like media and sent in console event to mixpanel")
    def heart_on_button_verification_functionality(self):
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_HEART_ICON.value))).click()
        time.sleep(5)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'MediaLiked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"



    @allure.step("FeedPage.heart_on_off_status | the like button is pressed")
    def verify_heart_on_off_status(self):
        time.sleep(5)
        try:
            heart_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_HEART_ICON.value))
            )
            style = heart_button.get_attribute("style")
            print(f"style: {style}")
            if '%0A%20%3Cpath%20fill-rule=%22evenodd%22%20clip-rule=%22evenodd%22%20d=%22M11.5576%' in style:
                print("the media is unliked")
                return "not liked"
            # Проверяем, содержит ли стиль данные для закрашенной иконки
            elif '3E%0A%3Cpath%20fill-rule=%22evenodd%22%20clip-rule=%22evenodd%22%20d=%22M11.5576%2018.91' in style:
                print("the media is liked")
                return "liked"
            else:
                print("unknown status")
                return "unknown"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "unknown"





    @allure.step("FeedPage.heart_off_button_verification | Unlike media and sent in console event to mixpanel")
    def heart_off_button_verification_functionality(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_HEART_ICON.value))).click()
        time.sleep(6)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'MediaUnliked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"

    @allure.step("FeedPage.no_event_heart_button_verification | Like media but no event sent to console")
    def no_event_heart_button_verification_functionality(self):
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_HEART_ICON.value))).click()
        time.sleep(2)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'MediaUnliked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
            elif 'MediaLiked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
            else:
                print("Event not found in browser logs")


    @allure.step("tags_verification | All media has tags")
    def tags_verification_functionality(self):
        tags = ["Print", "Video", "Feed", "Story"]
        media_tags = WebDriverWait(self.driver, timeout=20).until(
            EC.presence_of_all_elements_located((By.XPATH, WebGuestAppStaticElements.TAGS.value)))

        # time.sleep(2)
        for media_tag in media_tags:
            tag = media_tag.text
            print(f"Media tag found: {tag}")
            assert tag in tags, f"Unexpected media tag: {tag}"

            ## if one of asserts doesnt pass - FAIL

    @allure.step("FeedPage.three_dots_info | info popup is opened")
    def three_dots_info_functionality(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_THREE_DOTS_ICON.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.INFO_POPUP.value))).click()
        time.sleep(2)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'InfoPopupClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(By.XPATH, WebGuestAppStaticElements.INFO_POPUP_CLOSE.value))

    @allure.step(
        "FeedPage.popup_heart_on_off_button_verification | popup_ Like - unlike media and sent in console event to mixpanel")
    def popup_heart_on_off_button_verification(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_SECOND_MEDIA_POPUP.value))).click()

        time.sleep(6)
        ####Like and send the event
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))).click()
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))
        time.sleep(10)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        assert any('MediaLiked' in log['message'] for log in logs), "Event not found in browser logs"
        time.sleep(10)
        ###Unlike and send the event
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))).click()
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))
        time.sleep(10)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        assert any('MediaUnliked' in log['message'] for log in logs), "Event not found in browser logs"
        time.sleep(6)
        ### Close the popup
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.CLOSE_MEDIA_POPUP.value))).click()
        print("the Like button is fine")

    def popup_no_event_heart_button_verification(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_PAID_MEDIA_POPUP.value))).click()
        time.sleep(6)
        ####Like and don't send the event
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))).click()
        time.sleep(6)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        assert not any('MediaLiked' in log['message'] for log in logs) and not any(
            'MediaUnliked' in log['message'] for log in logs), "Unexpected event found in browser logs"
        ### Close the popup
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.CLOSE_MEDIA_POPUP.value))).click()
        print("no event for second like")

    @allure.step("FeedPage.three_dots_info_from_media_popup | info popup is opened")
    def popup_three_dots_info(self):
        time.sleep(10)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_MEDIA_POPUP.value))).click()
        time.sleep(10)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_THREE_DOTS.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.INFO_POPUP.value))).click()
        time.sleep(2)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'InfoPopupClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.INFO_POPUP_CLOSE.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.CLOSE_MEDIA_POPUP.value))).click()


    @allure.step("FeedPage.three_dots_report_content() | report the media and sent in console event to mixpanel")
    def popup_three_dots_report_content(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_THREE_DOTS.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.REPORT_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.REPORT_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentReportedClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"

    @allure.step(
        "FeedPage.three_dots_not_my_content | report the media is not my and sent in console event to mixpanel")
    def popup_three_dots_not_my_content(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_THREE_DOTS.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.NOT_MY_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.NOT_MY_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentNotRelevantClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        time.sleep(15)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.CLOSE_MEDIA_POPUP.value))).click()

    ################## Paid media
    # all_media_payment
    @allure.step(
        "FeedPage.three_dots_not_my_content | report the media is not my and sent in console event to mixpanel")
    def all_media_payment(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.SELECT_FIRST_MEDIA_BLOCK.value))).click()
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.BUY_NOW_BUTTON_FEED.value))).click()
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.BUY_NOW_BUTTON_POPUP.value))).click()
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.NEW_CART_PAGE_PROCEED_TO_PAYMENT_BUTTON.value))).click()

    @allure.step("FeedPage.banner_after_payment_verification() | Verify there is a banner after payment")
    def ui_special_banner_after_payment(self):
        time.sleep(3)
        banner_after_payment = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, WebGuestAppStaticElements.SPECIAL_OFFER_BANNER_AFTER_PAYMENT.value)))
        special_offer_text = banner_after_payment.text.strip()
        if len(special_offer_text) > 0:
            print("the banner after payment appears")
            print(special_offer_text)
            return True
        else:
            return False

    @allure.step("FeedPage.download_all_button_verification() | There is a download all button")
    def download_all_button_verification(self):
        time.sleep(3)
        WebDriverWait(self.driver, timeout=20).until(
            EC.presence_of_all_elements_located((By.XPATH, WebGuestAppStaticElements.DOWNLOAD_ALL_BUTTON.value)))

    @allure.step("FeedPage.download_button_verification() | There is a download button")
    def download_button_verification(self):
        time.sleep(3)
        WebDriverWait(self.driver, timeout=20).until(
            EC.presence_of_all_elements_located((By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_DOWNLOAD_ICON.value)))

    @allure.step("FeedPage.share_button_verification() | There is a share button")
    def share_button_verification(self):
        time.sleep(3)
        WebDriverWait(self.driver, timeout=20).until(
            EC.presence_of_all_elements_located((By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_SHARE_ICON.value)))



    @allure.step("FeedPage.download_button_functionality() | The media is downloaded and event is sent")
    def download_button_functionality(self):
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                ((By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_DOWNLOAD_ICON.value))).click()
        time.sleep(10)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'DownloadMediaClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"

    @allure.step("FeedPage.share_button_functionality() | The media is shared and event is sent")
    def share_button_functionality(self):
        try:
            time.sleep(10)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, WebGuestAppStaticElements.FIRST_MEDIA_SHARE_ICON.value))).click()
            time.sleep(10)
            logs = self.driver.get_log('browser')
            print("Browser logs collected:")
            for log in logs:
                print(log)
            event_found = False
            for log in logs:
                if 'ShareMediaClicked' in log['message']:
                    print(f"Event found in logs: {log['message']}")
                    event_found = True
                    break
            assert event_found, "Event not found in browser logs"
        except Exception as e:
            print(f"Exception in share_button_functionality: {e}")
            raise

    @allure.step("FeedPage.share_button_verification() | There is a share button")
    def download_all_button_functionality(self):
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                    ((By.XPATH, WebGuestAppStaticElements.DOWNLOAD_ALL_BUTTON.value))).click()
        time.sleep(10)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        number_of_downloaded_items = None
        for log in logs:
            if 'AllMediaDownloaded' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                # Extract the numberOfDownloadedItems value
                start_index = log['message'].find('numberOfDownloadedItems') + len('numberOfDownloadedItems": ')
                end_index = log['message'].find(',', start_index)
                number_of_downloaded_items = log['message'][start_index:end_index].strip()
                break
        assert event_found, "Event not found in browser logs"
        if number_of_downloaded_items:
            print(f"Number of downloaded items: {number_of_downloaded_items}")
        time.sleep(3)
        pyautogui.press('esc')
        time.sleep(2)






    @allure.step("FeedPage.download_button_functionality() | The media is downloaded and event is sent")
    def popup_download_button_verification(self):
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_PAID_MEDIA_POPUP.value))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.POPUP_DOWNLOAD_ICON.value))).click()
        time.sleep(10)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'DownloadMediaClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"


    @allure.step("FeedPage.share_button_functionality() | The media is share and event is sent")
    def popup_share_button_verification(self):
        time.sleep(6)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_PAID_MEDIA_POPUP.value))).click()
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH,
                                               WebGuestAppStaticElements.POPUP_SHARE_ICON.value))).click()
        time.sleep(10)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ShareMediaClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        time.sleep(3)
        pyautogui.press('esc')
        time.sleep(2)

    @allure.step("FeedPage.three_dots_info_from_media_popup | info popup is opened")
    def paid_media_popup_three_dots_info(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_PAID_MEDIA_POPUP.value))).click()
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_THREE_DOTS.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.INFO_POPUP.value))).click()
        time.sleep(2)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'InfoPopupClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.INFO_POPUP_CLOSE.value))).click()
        time.sleep(3)
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
        #     (By.XPATH, WebGuestAppStaticElements.CLOSE_MEDIA_POPUP.value))).click()

    @allure.step("FeedPage.three_dots_delete_content() | delete the media and sent in console event to mixpanel")
    def popup_three_dots_delete_content(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_MEDIA_POPUP.value))).click()
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_THREE_DOTS.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.DELETE_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.DELETE_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentDeletedClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"

    @allure.step("FeedPage.three_dots_report_content() | report the media and sent in console event to mixpanel")
    def popup_three_dots_report_content(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_THREE_DOTS.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.REPORT_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.REPORT_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentReportedClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"

    @allure.step(
        "FeedPage.three_dots_not_my_content | report the media is not my and sent in console event to mixpanel")
    def paid_media_popup_three_dots_not_my_content(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_THREE_DOTS.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.NOT_MY_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.NOT_MY_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentNotRelevantClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"
        time.sleep(15)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.CLOSE_MEDIA_POPUP.value))).click()

    @allure.step("FeedPage.three_dots_delete_content() | delete the media and sent in console event to mixpanel")
    def paid_media_popup_three_dots_delete_content(self):
        # time.sleep(6)
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
        #     (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_PAID_MEDIA_POPUP.value))).click()
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_THREE_DOTS.value))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, WebGuestAppStaticElements.DELETE_CONTENT.value))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.DELETE_CONTENT_APPROVE.value))).click()
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        event_found = False
        for log in logs:
            if 'ContentDeletedClicked' in log['message']:
                print(f"Event found in logs: {log['message']}")
                event_found = True
                break
        assert event_found, "Event not found in browser logs"

    @allure.step(
        "FeedPage.popup_heart_on_off_button_verification | popup_ Like - unlike media and sent in console event to mixpanel")
    def paid_media_popup_heart_on_off_button_verification(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_PAID_MEDIA_POPUP.value))).click()

        time.sleep(6)
        ####Like and send the event
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))).click()
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))
        time.sleep(10)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        assert any('MediaLiked' in log['message'] for log in logs), "Event not found in browser logs"
        time.sleep(10)
        ###Unlike and send the event
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))).click()
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(By.XPATH, WebGuestAppStaticElements.POPUP_HEART_ICON.value))
        time.sleep(10)
        # CHECK LOGS IN Console
        logs = self.driver.get_log('browser')
        assert any('MediaUnliked' in log['message'] for log in logs), "Event not found in browser logs"
        time.sleep(6)
        ### Close the popup
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.CLOSE_MEDIA_POPUP.value))).click()
        print("the Like button is fine")



    @allure.step(
        "FeedPage.popup_heart_on_off_button_verification | popup_ Like - unlike media and sent in console event to mixpanel")
    def go_to_feed(self):
        time.sleep(6)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, WebGuestAppStaticElements.OPEN_FIRST_PAID_MEDIA_POPUP.value))).click()





