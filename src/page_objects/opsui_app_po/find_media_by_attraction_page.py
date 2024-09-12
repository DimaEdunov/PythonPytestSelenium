import time
from datetime import date
from dateutil import parser
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.assistance_helper_services.opsui_by_attraction_helpers import OpsuiByAttractionHelpers
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements


class FindMediaByAttractionPage(object):
    negative = "negative"
    positive = "positive"

    def __init__(self, driver):
        self.driver = driver

    @allure.step("FindMediaByAttractionPage.find_media_by_attraction_page_opened_verification() |  Verify media by attraction page opened")
    def find_media_by_attraction_page_opened_verification(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_PAGE_VERIFICATION.value)))

    @allure.step("FindMediaByAttractionPage.add_photo_to_guest() |  Add photo to guest")
    def search_photos(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_FROM_HOUR_BUTTON.value))).click()

        arrow_button_in_time_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DOWN_HOUR_ARROW_IN_FROM.value)))

        click_counter = 8
        expected_hour = 1
        while expected_hour <= click_counter:
            arrow_button_in_time_field.click()
            expected_hour += 1

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_SEARCH_BUTTON.value))).click()

        time.sleep(3)

    @allure.step("FindMediaByAttractionPage.popup_added_to_guest_pass_verification() |  Popup added to guest pass verification")
    def popup_added_to_guest_pass_verification(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_ADDED_TO_GUEST_PASS_POPUP.value)))

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_ADDED_TO_GUEST_PASS_OK_BUTTON.value))).click()

    @allure.step("FindMediaByAttractionPage.print_photo() | print photo")
    def print_photo(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_PRINT_BUTTON.value))).click()

    @allure.step("FindMediaByAttractionPage.print_photo_popup_verification() |  print photo popup verification")
    def print_photo_popup_verification(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_VERIFICATION_POPUP.value)))

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OK_BUTTON_VERIFICATION_POPUP.value))).click()

    @allure.step("FindMediaByAttractionPage.close_photo_popup_and_photo_details() |  close photo popup and photo details")
    def close_photo_popup_and_photo_details(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.OPSUI_GENERAL_X_BUTTON.value))).click()

    @allure.step("FindMediaByAttractionPage.get_photo_number() |  get photo number")
    def get_photo_number(self):
        time.sleep(1)
        photo_number = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_PHOTO_NUMBER.value))).text
        return photo_number

    @allure.step("FindMediaByAttractionPage.select_time_according_to_time_zone() |  select time according to time zone")
    def select_time_according_to_time_zone(self, current_time_in_time_zone, region_name, test_status):
        buffer = None

        time.sleep(1)

        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_SEARCH_BUTTON.value)))
        search_button.click()

        if region_name == "ap":
            time_in_hour_button_to = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DISPLAY_NUMBER_IN_TO_HOUR.value)))
            time_in_hour_button_to_text = time_in_hour_button_to.text

            time_in_hour_button_text_final_datetime = parser.parse(time_in_hour_button_to_text)

            count_how_many_time_click_arrow_button_hour_int = OpsuiByAttractionHelpers.calculate_number_of_clicks_in_hour_field(
                current_time_in_time_zone, time_in_hour_button_text_final_datetime)

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_TO_HOUR_BUTTON.value))).click()

            down_arrow_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DOWN_HOUR_ARROW_IN_TO.value)))

            click_counter = count_how_many_time_click_arrow_button_hour_int + buffer

            expected_hour = 1
            while expected_hour <= click_counter:
                down_arrow_button.click()
                expected_hour += 1
            time.sleep(1.5)  # A necessary sleep
            search_button.click()

            time.sleep(3)

        else:
            time_in_hour_button_from = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DISPLAY_NUMBER_IN_FROM_HOUR.value)))
            time_in_hour_button_from_text = time_in_hour_button_from.text

            time_in_hour_button_text_final_datetime = parser.parse(time_in_hour_button_from_text)

            count_how_many_time_click_arrow_button_hour_int = OpsuiByAttractionHelpers.calculate_number_of_clicks_in_hour_field(
                current_time_in_time_zone, time_in_hour_button_text_final_datetime)

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_FROM_HOUR_BUTTON.value))).click()
            time.sleep(1)

            print("current_time_in_time_zone : " +str(current_time_in_time_zone))
            print("time_in_hour_button_text_final_datetime : " +str(time_in_hour_button_text_final_datetime))
            print("test_status : " +str(test_status))


            arrow_buffer_data = OpsuiByAttractionHelpers.get_on_what_arrow_button_to_click(self,
                                                                                          current_time_in_time_zone,
                                                                                          time_in_hour_button_text_final_datetime, test_status,buffer)


            click_counter = count_how_many_time_click_arrow_button_hour_int + arrow_buffer_data["buffer"]

            expected_hour = 1
            while expected_hour <= click_counter:
                arrow_buffer_data["arrow"].click()
                expected_hour += 1
            time.sleep(1.5)  # A necessary sleep
            search_button.click()

            time.sleep(3)

    @allure.step("FindMediaByAttractionPage.select_wrong_time_in_time_field() |  select wrong time in time field")
    def select_wrong_time_in_time_field(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_FROM_HOUR_BUTTON.value))).click()

        down_button_in_time_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DOWN_HOUR_ARROW_IN_FROM.value)))

        click_counter = 9
        expected_hour = 1
        while expected_hour <= click_counter:
            down_button_in_time_field.click()
            expected_hour += 1

    @allure.step("FindMediaByAttractionPage.verify_time_fields_are_in_red() |  verify time fields are in red")
    def verify_time_fields_are_in_red(self):
        time.sleep(2)
        from_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_FROM_HOUR_BUTTON.value)))

        to_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_TO_HOUR_BUTTON.value)))

        color_rgba = from_field.value_of_css_property("color")

        color_rgba1 = to_field.value_of_css_property("color")

        expected_color = "rgba(220, 53, 69, 1)"

        if color_rgba == expected_color and color_rgba1 == expected_color:
            assert True
        else:
            assert False

    @allure.step("FindMediaByAttractionPage.page_validation() |  page validation")
    def page_validation(self, attraction_name):
        # Attraction name in web as runTest
        attraction_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_ATTRACTION_BUTTON.value)))
        attraction_name_on_web = attraction_field.text

        # Date in web as current today
        day_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DATE_BUTTON.value)))
        day_in_web_text = day_field.text

        today = date.today()
        current_day = today.strftime("%a %d %b %Y")

        # Date picklist have 14 days
        amount_of_days_in_day_picklist = len(
            self.driver.find_elements(By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DATE_PICKLIST.value))

        # Hours are 08:00 & 23:00
        time_in_hour_button_to = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DISPLAY_NUMBER_IN_TO_HOUR.value)))
        time_in_hour_button_to_text = time_in_hour_button_to.text

        time_in_hour_button_from = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DISPLAY_NUMBER_IN_FROM_HOUR.value)))
        time_in_hour_button_from_text = time_in_hour_button_from.text

        expected_from_hour = "08:00"
        expected_to_hour = "23:00"

        if attraction_name_on_web == attraction_name and amount_of_days_in_day_picklist == 14 and \
                current_day == day_in_web_text and time_in_hour_button_to_text == expected_to_hour and \
                time_in_hour_button_from_text == expected_from_hour:
            assert True
        else:
            print("attraction_name_on_web: " + attraction_name_on_web)
            print("attraction_name: " + attraction_name)
            print("current_day: " + current_day)
            print("day_in_web_text: " + day_in_web_text)
            assert False

    @allure.step("FindMediaByAttractionPage.media_item_validation() |  media item validation")
    def media_item_validation(self, attraction_name):
        time.sleep(2.5)
        # Attraction mane as runTest
        attraction_name_in_web = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.PHOTO_DETAILS_POPUP_ATTRACTION_NAME.value)))
        attraction_name_in_web_text = attraction_name_in_web.text
        attraction_code_name_in_web = attraction_name_in_web_text[12:]

        photo_number = len(
            self.driver.find_elements(By.XPATH, OpsuiAppStaticElements.PHOTO_DETAILS_POPUP_PHOTO_NUMBER.value))

        date_of_photo = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, OpsuiAppStaticElements.PHOTO_DETAILS_POPUP_DATE.value)))
        date_of_photo_text = date_of_photo.text

        today = date.today()
        current_month = today.strftime("%B")

        if attraction_name.upper() == attraction_code_name_in_web and photo_number > 0 and \
                current_month in date_of_photo_text:
            assert True
        else:
            print("attraction_name: " + attraction_name.upper())
            print("attraction_name_in_web_text: " + attraction_code_name_in_web)
            print("date_of_photo_month: " + date_of_photo_text)
            print("current_month_as_web_format: " + current_month)
            assert False

    @allure.step("FindMediaByAttractionPage.click_on_select_multi_or_unselect_all_button() |  click on select multi or unselect all button")
    def click_on_select_multi_or_unselect_all_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_MULTI_PHOTOS_BUTTON.value))).click()

    @allure.step("FindMediaByAttractionPage.select_multiple_medias() |  select multiple medias")
    def select_multiple_medias(self, number_of_media_to_be_selected):
        time.sleep(2)
        photos_in_by_attraction = self.driver.find_elements(By.XPATH,
                                                            OpsuiAppStaticElements.PHOTOS_IN_FEED.value)

        for counter, one_photo in enumerate(photos_in_by_attraction, start=1):
            if counter <= number_of_media_to_be_selected:
                one_photo.click()
            else:
                break

    @allure.step("FindMediaByAttractionPage.verify_multiple_medias_were_selected() |  verify multiple medias were selected")
    def verify_multiple_medias_were_selected(self, number_of_photos_to_verify):
        photo_selected_sign = self.driver.find_elements(By.XPATH,
                                                            OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_PHOTO_SELECTED_SIGN.value)

        photo_selected_sign_len = len(photo_selected_sign)
        if photo_selected_sign_len == number_of_photos_to_verify:
            assert True
        else:
            assert False

    @allure.step("FindMediaByAttractionPage.click_on_preview_and_verify_popup() |  click on preview and verify popup")
    def click_on_preview_and_verify_popup(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_PREVIEW_BUTTON.value))).click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_PREVIEW_POPUP.value)))

    @allure.step("FindMediaByAttractionPage.go_back_to_media_by_attraction_by_clicking_on_edit_selection() |  go back to media by attraction")
    def go_back_to_media_by_attraction_by_clicking_on_edit_selection(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_EDIT_SELECTION_BUTTON.value))).click()

    @allure.step("FindMediaByAttractionPage.click_on_add_all_to_pass() |  click on add all to pass")
    def click_on_add_all_to_pass(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_ADD_ALL_TO_PASS_BUTTON.value))).click()
        time.sleep(1.5)