from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.ops_ui.static_elemenets.opsui_app_static_elements import OpsuiAppStaticElements


class OpsuiByAttractionHelpers:

    @staticmethod
    def calculate_number_of_clicks_in_hour_field(current_time_in_time_zone, time_in_hour_button_text_final_datetime):

        current_time_in_time_zone_str = str(current_time_in_time_zone)
        current_time_in_time_zone_hour = current_time_in_time_zone_str[11:13]
        current_time_in_time_zone_hour_int = int(current_time_in_time_zone_hour)

        time_in_hour_button_str = str(time_in_hour_button_text_final_datetime)
        time_in_hour_button_hour = time_in_hour_button_str[11:13]
        time_in_hour_button_hour_int = int(time_in_hour_button_hour)

        count_how_many_time_click_arrow_button = current_time_in_time_zone_hour_int - time_in_hour_button_hour_int

        if "-" in str(count_how_many_time_click_arrow_button):
            count_how_many_time_click_arrow_button_str = str(count_how_many_time_click_arrow_button)
            count_how_many_time_click = count_how_many_time_click_arrow_button_str[1:]
            count_how_many_time_click_positive_int = int(count_how_many_time_click)

            return count_how_many_time_click_positive_int

        else:
            return count_how_many_time_click_arrow_button

    @staticmethod
    def get_on_what_arrow_button_to_click(self, current_time_in_time_zone, time_in_hour_button_text_final_datetime, test_status,buffer):
        arrow_button = None
        if test_status == "negative":
            arrow_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_UP_HOUR_ARROW_IN_FROM.value)))

            buffer = +3

        elif current_time_in_time_zone > time_in_hour_button_text_final_datetime:
            arrow_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_UP_HOUR_ARROW_IN_FROM.value)))
            buffer = -1

        elif current_time_in_time_zone <= time_in_hour_button_text_final_datetime:
            arrow_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, OpsuiAppStaticElements.FIND_MEDIA_BY_ATTRACTION_DOWN_HOUR_ARROW_IN_FROM.value)))

            buffer = 1

        return {"arrow" : arrow_button,"buffer" : buffer}
