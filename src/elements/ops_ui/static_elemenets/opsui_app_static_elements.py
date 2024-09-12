import enum


class OpsuiAppStaticElements(enum.Enum):
    ############ OPSUI ################

    # General elements
    GUEST_OR_MEDIA_DOES_NOT_EXIST_ERROR_POPUP = '//header[@class="toast-header"]'
    OPSUI_GUEST_SUBMIT_CREATE_BUTTON = "//div[@class='b-overlay-wrap position-relative d-inline-block mt-2']//button"
    OPSUI_CREATE_USER_VERIFICATION = '//div[@class="ml-1"]'

    # OpsUi - Login related elements
    CLOUDFLARE_PAGE_AZURE_AD_BUTTON = '//a[@title="Azure AD ・ Pomvom Microsoft Account"]'
    INSERT_EMAIL_FIELD = '//input[@type="email"]'
    INSERT_PASSWORD_FIELD = '//input[@type="password"]'
    LOGIN_SUBMIT_BUTTON = '//input[@type="submit"]'
    OPSUI_HOMEPAGE_LOGO = '//div[@class="logo-center"]'
    LANGUAGE_BUTTON = '//button[@aria-haspopup="true"]'
    ENGLISH_PICKLIST = '//li[@class="language-item"][1]'

    # General buttons and fields
    OPSUI_INSERT_PHONE_NUMBER_FIELD = "//input[@id='phone']"
    OPSUI_GUEST_ID_FIELD = "//div[@class='ml-1']"
    OPSUI_GENERAL_X_BUTTON = "//div[@class='text-right']//*[name()='svg']"
    HOME_BUTTON = "(//button[contains(@class, 'btn-opsui secondary')])[2]"
    BACK_BUTTON = "(//button[contains(@class, 'btn-opsui secondary')])[1]"
    ADD_TO_PASS_BUTTON = "//button[contains(@class, 'success')]"
    OPSUI_GUEST_SEARCH_CONFIRM_QR_CREATION_POPUP = "//div[@id='b-toaster-top-center']//div[@class='toast-body']"
    OPSUI_GUEST_PAGE_ACTIVATED_NOT_PAID_BUTTON = "//div[contains(@class, 'h-100 ')]" \
                                                 "//div[contains(@class, 'mt-3 text-white')]"
    PHOTO_DETAILS_VERIFICATION_POPUP = "//div[@id='confirmation___BV_modal_body_']"
    PHOTOS_IN_FEED = "//div[@class='col']"
    OK_BUTTON_VERIFICATION_POPUP = "//div[contains(@id,'confirmation')]//button[contains(@class, 'success')]"

    # QR/phone guest page
    OPSUI_GUEST_PAGE_FIND_MEDIA_BY_NUMBER = "(//button[@class = 'btn btn-opsui primary mx-2 btn-secondary'])[1]"
    OPSUI_GUEST_PAGE_FIND_MEDIA_BY_ATTRACTION = "(//button[@class = 'btn btn-opsui primary mx-2 btn-secondary'])[2]"
    OPSUI_GUEST_PAGE_FIND_MEDIA_BY_BY_QR = "(//button[@class = 'btn btn-opsui primary mx-2 btn-secondary'])[3]"
    OPSUI_GUEST_PAGE_SEND_SMS_BUTTON = "(//div[@class='row mb-3 mt-4']//button[@class = 'btn btn-opsui primary " \
                                       "btn-secondary'])[2] "
    OPSUI_QR_USERID_INVALID_INPUT_VERIFICATION = "//input[contains(@class, 'input is-invalid')]"
    OPSUI_GUEST_PAGE_VIDEO_THUMBNAIL = "//div[@class='thumbnail-video']"
    OPSUI_GUEST_PAGE_PREVIEW_BUTTON = '(//div[contains(@class,"b-overlay-wrap")]//button[@type="button"])[2]'
    OPSUI_GUEST_PAGE_ADD_TO_CART_BUTTON = '//div[@class="p-0 col-2"]//button[@class="btn btn-opsui btn-secondary secondary"]'
    OPSUI_GUEST_PAGE_REMOVE_FROM_CART = '//div[@class="p-0 col-2"]//button[@class="btn btn-opsui btn-secondary primary"]'
    OPSUI_GUEST_PAGE_PREVIEW_CLOSE_ICON = "//*[name()='path' and contains(@d,'M4.646 4.6')]"
    OPSUI_GUEST_PAGE_ENTITLEMENT_BUTTON = "//button[normalize-space()='Entitlement']"
    OPSUI_GUEST_PAGE_ENTITLEMENT_POPUP_ALL_CART_ITEMS = '(//div[contains(@class,"b-overlay-wrap")]//button[contains(@class,"btn entitlement-button")])[2]'
    OPSUI_GUEST_PAGE_ENTITLEMENT_POPUP_EDIT_ENTITLEMENT = "//button[contains(text(),' Edit Entitlement ')]"
    OPSUI_GUEST_PAGE_ENTITLEMENT_POPUP_ALL_PHOTOS = '(//div[contains(@class,"b-overlay-wrap")]//button[contains(@class,"btn entitlement-button")])[1]'

    # Main screen
    MAIN_PAGE_FEATURES_BUTTONS = "//span[@class='button-text']"
    MAIN_PAGE_FEATURES = "//button[(@type='button') and not (@class='btn btn-logout btn-secondary') and not (@class='btn dropdown-toggle btn-secondary language-toggle')]"

    # Entitlements
    GUEST_ID_QR_INSERT_FIELD = '//input[@id="guestQr"]'
    GUEST_APP_ENTITLEMENT_PAGE_VERIFICATION = '//h1[@class="mx-auto mt-5 mb-3"]'
    GUEST_ENTITLEMENT_PHONE_NUMBER = "//div[@class='ml-1 mb-1']"
    GUEST_ENTITLEMENT_ADD_BUTTON = "//button[contains(@class, 'btn-opsui primary')]"
    GUEST_ENTITLEMENT_ONE_DAY_PASS_BUTTON = "(//button[contains(@class, 'entitlement-button')])[1]"
    GUEST_ENTITLEMENT_START_DATE_FIRST = "(//tr[@role='row']//td[@aria-colindex='4'])[1]"
    GUEST_ENTITLEMENT_START_DATE_SECOND = "(//tr[@role='row']//td[@aria-colindex='4'])[2]"
    REMOVE_ENTITLEMENT_YES_BUTTON_POPUP = "//button[contains(@class, 'btn-danger')]"
    ENTITLEMENT_PAGE_TYPE_TEXT_FIRST = "(//tbody[@role='rowgroup']//tr)[1]//td[2]"
    ENTITLEMENT_PAGE_TYPE_TEXT_SECOND = '(//tbody[@role="rowgroup"]//tr)[2]//td[2]'

    # Find Media By Number
    FIND_MEDIA_BY_NUMBER_MEDIA_NUMBER_FIELD = "//input[@placeholder='Media Number']"
    FIND_MEDIA_BY_NUMBER_SUBMIT_BUTTON = "//button[@class='btn btn-opsui primary mx-auto btn-secondary']"
    FIND_MEDIA_BY_NUMBER_ATTRACTION_PICKLIST_FIELD = "(//button[contains(@class, 'dropdown-toggle')])[1]"

    # Guest Media page
    PHONE_TEXT_FIELD_INVALID_INPUT_RED_INDICATION = '//input[contains(@class, "input is-invalid")]'
    PHONE_TEXT_FIELD_VALID_INPUT_GREEN_INDICATION = '//input[contains(@class, "input is-valid")]'
    REMOVE_FROM_PASS_BUTTON = "//button[contains(@class, 'danger')]"

    # Find media by attraction page elements
    FIND_MEDIA_BY_ATTRACTION_PAGE_VERIFICATION = "//div[contains(@class, 'row text-left')]"

    GUEST_PAGE_PREVIEW_BUTTON = '//div[@class="b-overlay-wrap position-relative d-inline-block"]//button[@class="btn btn-opsui primary btn-secondary"]'
    FIND_MEDIA_BY_ATTRACTION_FIRST_PHOTO = "(//div[@class='col'])[1]//img"

    FIND_MEDIA_BY_ATTRACTION_FROM_HOUR_BUTTON = "(//button[contains(@Class, 'btn h-auto')])[1]"
    FIND_MEDIA_BY_ATTRACTION_TO_HOUR_BUTTON = "(//button[contains(@Class, 'btn h-auto')])[2]"
    FIND_MEDIA_BY_ATTRACTION_DISPLAY_NUMBER_IN_FROM_HOUR = "(//label[@class='form-control'])[1]"
    FIND_MEDIA_BY_ATTRACTION_DISPLAY_NUMBER_IN_TO_HOUR = "(//label[@class='form-control'])[2]"
    FIND_MEDIA_BY_ATTRACTION_DOWN_HOUR_ARROW_IN_FROM = "(//div[contains(@class, 'search-time')]//button)[3]"
    FIND_MEDIA_BY_ATTRACTION_UP_HOUR_ARROW_IN_FROM = "(//div[contains(@class, 'search-time')]//button)[2]"
    FIND_MEDIA_BY_ATTRACTION_DOWN_HOUR_ARROW_IN_TO = "(//div[contains(@class, 'search-time')]//button)[4]"
    FIND_MEDIA_BY_ATTRACTION_SEARCH_BUTTON = "//div[contains(@Class,'col-1')]//button"
    FIND_MEDIA_BY_ATTRACTION_ADDED_TO_GUEST_PASS_POPUP = "//div[@id='confirmation___BV_modal_content_']"
    FIND_MEDIA_BY_ATTRACTION_ADDED_TO_GUEST_PASS_OK_BUTTON = "//button[contains(@Class,'btn btn-opsui success')]"
    FIND_MEDIA_BY_ATTRACTION_PRINT_BUTTON = '//div[@class="col-2"]//button[@class="btn btn-opsui primary btn-secondary"]'
    FIND_MEDIA_BY_ATTRACTION_PHOTO_NUMBER = "(//span[@class='thumbnail-number'])[1]"
    FIND_MEDIA_BY_ATTRACTION_VERIFICATION_POPUP = "//div[contains(@id,'mediapreview')]"
    FIND_MEDIA_BY_ATTRACTION_ATTRACTION_BUTTON = "//button[@id='capture-location__BV_toggle_']"
    FIND_MEDIA_BY_ATTRACTION_DATE_BUTTON = "//button[@id='capture-date__BV_toggle_']"
    FIND_MEDIA_BY_ATTRACTION_DATE_PICKLIST = "//ul[@aria-labelledby='capture-date__BV_toggle_']//li[@role='presentation']"
    FIND_MEDIA_BY_ATTRACTION_MULTI_PHOTOS_BUTTON = "(//div[@Class='footer-buttons']//button)[1]"
    FIND_MEDIA_BY_ATTRACTION_PHOTO_SELECTED_SIGN = "//div[@class='photo-selected']"
    FIND_MEDIA_BY_ATTRACTION_PREVIEW_BUTTON = "(//div[@Class='footer-buttons']//button)[2]"
    FIND_MEDIA_BY_ATTRACTION_PREVIEW_POPUP = "//div[@id='multiSelectPreview___BV_modal_body_']"
    FIND_MEDIA_BY_ATTRACTION_EDIT_SELECTION_BUTTON = "(//div[contains(@class, ' text-center')]//button)[2]"
    FIND_MEDIA_BY_ATTRACTION_ADD_ALL_TO_PASS_BUTTON = "(//div[contains(@class, ' text-center')]//button)[1]"

    # Photo details popup in by attraction page elements
    PHOTO_DETAILS_POPUP_ATTRACTION_NAME = "//div[@class='text-right col-auto']"
    PHOTO_DETAILS_POPUP_PHOTO_NUMBER = "//span[@class='preview-number']"
    PHOTO_DETAILS_POPUP_DATE = '//div//div[@class="text-left col-auto"]'

