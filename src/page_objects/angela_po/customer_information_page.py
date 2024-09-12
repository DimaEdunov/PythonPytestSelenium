import re
import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.elements.angela.dynamic_elemenets.angela_dynamic_elements_picklists import AngelaDynamicElementsPicklists
from src.elements.angela.static_elemenets.angela_static_elements import AngelaStaticElements


class CustomerInformationPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("CustomerInformationPage.get_price_of_ticket_in_angela() | get price of ticket in angela")
    def get_price_of_ticket_in_angela(self):
        price_of_ticket = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, AngelaStaticElements.CUSTOMER_INFORMATION_PRICE_OF_TICKET.value))).text
        price_of_ticket_list = re.findall(r'[\d\.\d]+', price_of_ticket)
        price_of_ticket_float = float(price_of_ticket_list[0])
        print("price_of_ticket_int" + str(price_of_ticket_float))

        return price_of_ticket_float

    @allure.step("CustomerInformationPage.verify_price_of_ticket_in_angela_equals_to_price_in_guest_app() | verify price of ticket in angela equals to the price in guest app")
    def verify_price_of_ticket_in_angela_equals_to_price_in_guest_app(self, price_in_guest_app, price_in_angela):

        if price_in_guest_app == price_in_angela:
            assert True
        else:
            assert False

    @allure.step("CustomerInformationPage.top_tool_bar_navigation() | top tool bar navigation")
    def top_tool_bar_navigation(self, page_name):
        AngelaDynamicElementsPicklists.select_page_from_tool_bar(self.driver, page_name)
        time.sleep(3.5)

