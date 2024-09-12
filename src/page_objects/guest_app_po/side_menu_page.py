import time
import allure
from langdetect import DetectorFactory, detect
from src.elements.guest_app.static_elemenets.web_guest_app_static_elements import WebGuestAppStaticElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SideMenuPage(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("FeedPage.enter_a_tab() | Enter a tab inside side menu")
    def go_to(self, side_menu_button_xpath):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                       ((By.XPATH, side_menu_button_xpath)))
        time.sleep(1.5)
        element.click()

    @allure.step("FeedPage.enter_home_page() | Assure you're on the correct tab")
    def go_to_page_verification(self, expected_url):

        if expected_url == "feed":

            current_url = self.driver.current_url

            time.sleep(2)

            WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located
                                                 ((By.XPATH, WebGuestAppStaticElements.
                                                   ALL_SCREENS_TITLE_ELEMENT.value)))
            association_method_buttons = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.
                                                                   ADD_MEDIA_RANDOM_ASSOCIATION_METHOD.value)

            media_number = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.ASSOCIATED_GUEST_MEDIA_IN_GALLERY.value)

            if expected_url in current_url and (len(media_number) or len(association_method_buttons) != 0):
                pass
            else:
                assert False


        #Nastia:

        elif expected_url == "cart":
            pass

        elif expected_url == "collect-media":

            current_url = self.driver.current_url

            WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located
                                                 ((By.XPATH, WebGuestAppStaticElements.
                                                   ALL_SCREENS_TITLE_ELEMENT.value)))

            association_method_buttons = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.
                                                                   ADD_MEDIA_RANDOM_ASSOCIATION_METHOD.value)

            if expected_url in current_url and len(association_method_buttons) != 0:
                pass
            else:
                assert False

        elif expected_url == "settings":

            current_url = self.driver.current_url

            WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located
                                                 ((By.XPATH, WebGuestAppStaticElements.
                                                   ALL_SCREENS_TITLE_ELEMENT.value)))

            delete_account_button = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.
                                                              ACCOUNT_PAGE_DELETE_ACCOUNT_BUTTON.value)

            if expected_url in current_url and len(delete_account_button) != 0:
                pass
            else:
                assert False

        elif expected_url == "faq":

            current_url = self.driver.current_url

            WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located
                                                 ((By.XPATH, WebGuestAppStaticElements.
                                                   ALL_SCREENS_TITLE_ELEMENT.value)))

            help_and_support_sections = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.
                                                                  HELP_AND_SUPPORT_SECTIONS.value)
            if expected_url in current_url and len(help_and_support_sections) == 7:
                pass
            else:
                print(len(help_and_support_sections))
                assert False

        elif expected_url == "terms-and-conditions":

            current_url = self.driver.current_url

            WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located
                                                 ((By.XPATH, WebGuestAppStaticElements.
                                                   ALL_SCREENS_TITLE_ELEMENT.value)))

            terms_and_conditions_texts = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.
                                                                   TERMS_AND_CONDITIONS_TEXTS_LIST.value)
            if expected_url in current_url and len(terms_and_conditions_texts) == 28:
                pass
            else:
                print(len(terms_and_conditions_texts))
                assert False

        elif expected_url == "privacy-policy":

            current_url = self.driver.current_url

            WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located
                                                 ((By.XPATH, WebGuestAppStaticElements.
                                                   ALL_SCREENS_TITLE_ELEMENT.value)))

            terms_and_conditions_texts = self.driver.find_elements(By.XPATH, WebGuestAppStaticElements.
                                                                   PRIVACY_POLICY_PAGE_LINKS.value)
            if expected_url in current_url and len(terms_and_conditions_texts) == 14:
                pass
            else:
                print(len(terms_and_conditions_texts))
                assert False

    @allure.step("FeedPage.change_guestapp_language() | "
                 "Assure current_language_detected is the correct current_language_detected")
    def go_to_language_verification(self, expected_language, page_name):

        time.sleep(3)

        # Home page via side menu
        if page_name == "feed":

            empty_gallery_subtitle = self.driver.find_element \
                (By.XPATH, WebGuestAppStaticElements.ADD_MEDIA_PAGE_SUBTITLE.value)

            element_to_verify = empty_gallery_subtitle.text

            DetectorFactory.seed = 0

            current_language_detected = detect(element_to_verify)

            if current_language_detected == expected_language:
                pass
            else:
                assert False

        # Add media page via side menu
        elif page_name == "collect-media":

            empty_gallery_subtitle = self.driver.find_element \
                (By.XPATH, WebGuestAppStaticElements.ADD_MEDIA_PAGE_SUBTITLE.value)

            element_to_verify = empty_gallery_subtitle.text

            DetectorFactory.seed = 0

            current_language_detected = detect(element_to_verify)

            if current_language_detected == expected_language:
                pass
            else:
                assert False

        # Account settings page via side menu
        elif page_name == "settings":

            delete_account_subtitle = self.driver.find_element \
                (By.XPATH, WebGuestAppStaticElements.ACCOUNT_SETTINGS_MENU_SMS_SUBTITLE.value)

            element_to_verify = delete_account_subtitle.text

            DetectorFactory.seed = 0

            current_language_detected = detect(element_to_verify)

            if current_language_detected == expected_language:
                pass
            else:
                assert False

        # Help & support page via side menu
        elif page_name == "faq":

            my_photos_are_watermarked = self.driver.find_element \
                (By.XPATH, WebGuestAppStaticElements.HELP_AND_SUPPORT_SECTIONS.value)

            element_to_verify = my_photos_are_watermarked.text

            DetectorFactory.seed = 0

            current_language_detected = detect(element_to_verify)

            if current_language_detected == expected_language:
                pass
            else:
                assert False

        # Terms & conditions page via side menu
        elif page_name == "terms-and-conditions":

            terms_and_cconditions_subtitle = self.driver.find_element \
                (By.XPATH, WebGuestAppStaticElements.TERMS_AND_CONDITIONS_SUBTITLE.value)

            element_to_verify = terms_and_cconditions_subtitle.text

            DetectorFactory.seed = 0

            current_language_detected = detect(element_to_verify)

            if current_language_detected == expected_language:
                pass
            else:
                assert False

        # Privacy policy page via side menu
        elif page_name == "privacy-policy":

            privacy_policy_2nd_branch = self.driver.find_element \
                (By.XPATH, WebGuestAppStaticElements.PRIVACY_POLICY_PAGE_2ND_LINK.value)

            element_to_verify = privacy_policy_2nd_branch.text

            DetectorFactory.seed = 0

            current_language_detected = detect(element_to_verify)

            if current_language_detected == expected_language:
                pass
            else:
                assert False
