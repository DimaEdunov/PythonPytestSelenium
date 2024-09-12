import enum


class AngelaStaticElements(enum.Enum):
    ############ ANGELA ################
    # Angela - menu page
    CUSTOMER_MEDIA_BUTTON = "//a[@href='/customer-media']"
    SEARCH_CUSTOMER_BUTTON = "//a[@href='/search-customer']"
    ANGELA_LOGIN_REFFERANCE_ELEMENT = "//div[contains(text(),'Welcome')]"

    # Angela - customer media page
    CUSTOMER_MEDIA_SELECT_PARK_PICKLIST = "//label[@for='parkSelect']/following-sibling::label"
    CUSTOMER_MEDIA_SELECT_ATTRACTION_PICKLIST = "//label[contains(@class, 'q-select--single q-field--outlined q-field--dense')]"
    CUSTOMER_MEDIA_SEARCH_BUTTON = "//i[contains(@class, 'text-white notranslate')]"
    CUSTOMER_MEDIA_FIRST_PHOTO = "(//div[@class='column absolute-center full-width full-height'])[1]"
    MEDIA_DETAILS_PREFIX_PLUS_MEDIA_NUMBER = "//span[contains(text(), 'Prefix')]/following-sibling::span"
    CUSTOMER_MEDIA_PARK_PICKLIST = '(//div[@class="q-field__append q-field__marginal row no-wrap items-center q-anchor--skip"])[1]'

    # Angela search customer page
    SEARCH_CUSTOMER_USER_ID_OR_PHONE_FIELD = "(//input[contains(@class,'q-field__native')])[1]"
    SEARCH_CUSTOMER_SEARCH_BUTTON_BY_USER_ID_OR_PHONE = "(//button[contains(@class, 'button--icon')])[1]"
    SEARCH_CUSTOMER_USER_FOUND = "//div[contains(@class, 'q-img__content')]"
    OPEN_SEARCH_CUSTOMER_PARK_PICKLIST = "//div[@id='parkSelect']"

    # Angela customer information page
    CUSTOMER_INFORMATION_PRICE_OF_TICKET = "(//td[@class='text-left item-subtitle'])[7]"

    # navigate between upper tool bar
    TOOL_BAR_NAVIGATION = "//div[@class='q-tab__label']"
