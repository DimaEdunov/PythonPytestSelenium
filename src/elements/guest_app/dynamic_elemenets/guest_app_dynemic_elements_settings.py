from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GuestAppDynemicElementsSettings():

    @staticmethod
    def settings_choose_language_element(driver, language):

        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable
                                             ((By.XPATH, "//label[@for='%s']//span" % language)))
