import enum


class GmailStaticElements(enum.Enum):

    INSERT_EMAIL_FIELD = '//input[@type="email"]'
    INSERT_PASSWORD_FIELD = '//input[@type="password"]'
    LOGIN_SUBMIT_BUTTON = '//input[@type="submit"]'
    FIRST_EMAIL_ITEM_IN_LIST = '//div[@class="FiPRo"]//div[contains(@style, "position: absolute")]'
    OPEN_SELECT_ALL_BUTTON_SELECTION = '//i[@data-icon-name="SelectAllOffRegular"]'
    SELECT_ALL_BUTTON = '//div[@title="Select all messages"]'
    DELETE_ALL = '//button[@aria-label="Empty folder"]'
    DELETE_ITEMS_CONFIRM = "//div[contains(@class,'ms-Layer')]//button[contains(@id,'ok')]"

