import enum



class WebGuestAppStaticElements(enum.Enum):
    # GUEST APP #
    # GuestApp - Login related elements
    SMS_INPUT_FIRST_CELL_WAIT_ELEMENT = '//input[@id="code-0"]'

    LOGIN_PAGE_ERROR_MESSAGE_INVALID_PHONE = "//div[@data-is-valid='false']"
    LOGIN_PAGE_ACCEPT_COOKIES_BUTTON = "//button[contains(text(),'Accept')]"
    PHONE_NUMBER_FIELD = "//input[@id='phoneNumber']"
    LOGIN_VIEW_YOUR_CONTENT = "//h1[contains(text(),'View Your Content')]"
    LOGIN_AGREE_TERMS_BUTTON = "(//div[@class='modal-buttons-block']//button[contains(@class,'buttonComponent')])[2]"
    LOGIN_NEXT_BUTTON = '//button[@type="submit"]'
    LOGIN_TERMS_AND_CONDITIONS_LINK = "//a[contains(@href, 'terms-and-conditions')]"
    TERMS_AND_CONDITIONS_VERIFICATION_PAGE = "//div[contains(@class, 'terms-page')]"
    GUEST_APP_GO_BACK_BUTTON = "//header[contains(@class,'header')]//button[@class='buttonComponent-j_QRg ']"
    COUNTRY_CODE_NUMBER_FIELD = "//div[@class='country-code-block']"
    COUNTRY_CODE_POPUP_FIRST_ITEM = '(//li//label)[1]'
    LOGIN_PAGE_GOOGLE_BUTTON = '//body[@class="qJTHM"]'
    LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_EMAIL_FIELD = '//input[@type="email"]'
    LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_NEXT_BUTTON = '(//button//span[@class="VfPpkd-vQzf8d"])[2]'
    LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_NEXT_BUTTON_SECOND_PAGE = '//input[@type="submit"]'
    LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_PASSWORD_FIELD = '//input[@name="passwd"]'
    LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_SUBMIT_BUTTON = '//input[@type="submit"]'
    LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_LOGGED_IN_EMAIL = '(//div[@class="fFW7wc-ibnC6b-r4m2rf"])[1]'
    GOOGLE_BUTTON_IFRAME = "(//iframe)[1]"
    LOGIN_PAGE_EMAIL_POPUP_REGISTRATION_CONTINUE_BUTTON = '(//span[@jsname="V67aGc"])[1]'
    SIDE_MENU_FEED = ''

    # GuestApp - Feed Page elements

    #New Feed Elements
    BODY_ELEMENT = '//div[@id="app"]'
    PARK_LOGO = '//a//img[@class="logo"]'
    SPECIAL_OFFER_BANNER = '//div[@class="bundles-marketing-banner-Z00vD"]'
    ATTRACTION_NAME_NEW_FEED = '(//div[@class="text-pair"])//h2[1]'
    ATTRACTION_LOCATION_NEW_FEED = '//div[@class="text-pair"]'
    MEDIA_DATE_NEW_FEED = '//span[@class="sbody sb date"]'
    FIRST_MEDIA_ROW = '//div[@class="feed-group-wrapper-ubt_h"][1]'
    MEDIA_IN_THE_ROW = '//div[@class="media-block"]'
    FIRST_MEDIA_HEART_ICON = '(//div[@class="group-media"]//button[@data-shape="square"])[1]'
    FIRST_MEDIA_THREE_DOTS_ICON = '(//div[@class="group-media"]//button[@data-shape="square"])[4]'
    MEDIA_MARK = '//li[@class="xxsbody b"]'
    SELECT_AND_BUY_BUTTON = '(//button[@class="buttonComponent-j_QRg feed-float-cta uppercase"])'
    DELETE_CONTENT = '//*[contains(text(), "Delete content")]'
    DELETE_CONTENT_APPROVE = '//div[@class="modal-buttons-block"]//button[@class="buttonComponent-j_QRg uppercase "  and contains(text(), "Delete")]'
    REPORT_CONTENT = '//*[contains(text(), "Report content")]'
    REPORT_CONTENT_APPROVE = '//div[@class="modal-buttons-block"]//button[@class="buttonComponent-j_QRg uppercase "  and contains(text(), "Report")]'
    NOT_MY_CONTENT = '//*[contains(text(), "Not my content")]'
    NOT_MY_CONTENT_APPROVE = '//div[@class="modal-buttons-block"]//button[@class="buttonComponent-j_QRg uppercase "  and contains(text(), "Not my content")]'
    INFO_POPUP = '//*[contains(text(), "Info")]'
    INFO_POPUP_CLOSE = '//div[@id="media-info-modal-component-wCzcE"]//button[@class="buttonComponent-j_QRg close" and @type="button" and @data-size="m" and @data-type="simple-icon"]'
    NEW_FEED_OVERLAY = '//div[@class="overlay-component-HTuA6 transitioned-in visible menu-overlay-component "]'
    MEDIA_BLOCKS = '//div[@class="media-block"]'
    FIRST_UNPAID_MEDIA_BLOCK = '(//div[@class="media-block"])[1]'
    SECOND_UNPAID_MEDIA_BLOCK = '(//div[@class="media-block"])[2]'
    THIRD_UNPAID_MEDIA_BLOCK = '(//div[@class="media-block"])[3]'
    DISPLAY_ONE_MEDIA_BUTTON = '//div[@class="cta-wrapper"]'
    DISPLAY_TWO_MEDIA_BUTTON = '//div[@class="cta-wrapper grouped-cta"]'
    TAGS = '//ul[@class="feed-item-tags-bVE07"]'
    OPEN_FIRST_MEDIA_POPUP = '(//span[@class="zoom-arrows-icon"])[1]'
    OPEN_SECOND_MEDIA_POPUP = '(//span[@class="zoom-arrows-icon"])[2]'
    OPEN_FIRST_PAID_MEDIA_POPUP = '//img[@data-media-index="0"]'
    SECOND_PAID_MEDIA_POPUP = '//img[@data-media-index="1"]'
    POPUP_HEART_ICON = '//button[@class="buttonComponent-j_QRg keep-modal-opened"]'
    POPUP_SHARE_ICON = '(//button[@class="buttonComponent-j_QRg "])[last()-2]'
    POPUP_DOWNLOAD_ICON = '(//button[@class="buttonComponent-j_QRg "])[last()-1]'
    POPUP_THREE_DOTS = '(//button[@class="buttonComponent-j_QRg " and @data-type="simple-icon"])[last()]'
    POPUP_MEDIA_INFO_CLOSE = '(//button[@class="buttonComponent-j_QRg close"])[2]'
    CLOSE_MEDIA_POPUP = '//button[@class="buttonComponent-j_QRg close"]'
    SELECT_FIRST_MEDIA_BLOCK = '//div[@class="media-block"]'
    SPECIAL_OFFER_BANNER_AFTER_PAYMENT = '//div[@class="post-payment-banner-component-EK1Tt new-banner"]'
    SPECIAL_OFFER_NO_THANKS = '//p[@class="sb sublink"]'
    SPECIAL_OFFER_YES_PLEASE = '//button[@class="buttonComponent-j_QRg uppercase bold"]'


    # Paid media:
    FIRST_MEDIA_SHARE_ICON = '(//div[@class="group-media"]//button[@data-shape="square"])[2]'
    FIRST_MEDIA_DOWNLOAD_ICON = '(//div[@class="group-media"]//button[@data-shape="square"])[3]'
    DOWNLOAD_ALL_BUTTON = '//button[@class="buttonComponent-j_QRg feed-float-cta uppercase"]'
    SHARE_POPUP_ELEMENT = ''




    HOME_SCREEN_SIDEMENU_LOGIN_VERIFICATION = '//div[@class="menu-block"]'
    SIDE_MENU_LOGOUT_BUTTON = '(//div[@class="menu-block"]//button)[7]'
    SIDE_MENU_LOGOUT = "//button[contains(text(), 'Logout')]"
    LOGOUT_POPUP_SUBMIT_LOGOUT = '(//div[@class="modal-buttons-block"]//button)[2]'
    ACCOUNT_SETTINGS_PAGE_VIA_SIDE_MENU = "//button[@class='buttonComponent-j_QRg '][3]"  # Need to chang
    ACCOUNT_SETTING_DELETE_ACCOUNT = "//div[@class='settings-item'][2]"  # Need to chang
    CONFIRM_DELETE_ACCOUNT_POPUP = "(//div[@class='modal-block ']//button[contains(@class,'buttonComponent-j_QRg')])[2]" # Need to chang
    ASSOCIATED_GUEST_MEDIA_IN_GALLERY = "//div[@class='media-block']//img"
    MARKETING_BANNER = "//div[contains(@class, 'banner-component')]"
    BUY_NOW_BUTTON_FEED = '//button[@class="buttonComponent-j_QRg feed-float-cta uppercase secondary-color"]'
    BUY_NOW_BUTTON_POPUP ='//button[@class="buttonComponent-j_QRg uppercase bold"]'

    PAYMENT_SUCCESS_FEED_BUTTON = "//button[@class='buttonComponent-j_QRg uppercase']"
    ADD_MEDIA_PAGE_ASK_AN_OPERATOR_BUTTON = "//div[@class='associations-block']//button[last()]"  # Need to chang
    HOME_PAGE_VIA_SIDE_MENU = "(//div[@class = 'menu-block']//button[@class = 'buttonComponent-j_QRg '])[1]"
    ADD_MEDIA_PAGE_SUBTITLE = "//P[@class = 'subtitle']"
    GUEST_APP_SHARE_BUTTON = "//div[@class='ticket-media-actions-block']//button[@class='buttonComponent-j_QRg b']"
    GUEST_APP_DOWNLOAD_BUTTON = "(//div[@class='ticket-media-actions-block']//button[@class='buttonComponent-j_QRg '])[1]"
    GUEST_APP_MEDIA_LINK_BUTTON = "(//div[@class='ticket-media-actions-block']//button[@class='buttonComponent-j_QRg '])[2]"
    GUEST_APP_IMAGE_LINK_COPIED_TO_YOUR_CLIPBOARD_POPUP = "//div[@class='notification-component-xCcfJ ']"
    FEED_PAGE_ADD_TO_CART_BUTTONS = '//button[@class="buttonComponent-j_QRg uppercase"]'
    FEED_PAGE_ALL_PHOTOS = "//img[not(@class='logo') and not(@alt='photo-thumbnail')]"
    FEED_PAGE_ALL_VIDEOS = '//div[@class="feed-component-SNULA"]//video'
    FEED_PAGE_NAVIGATION_BAR_CART_BUTTON = '//button[contains(@class,"capitalize  cart")]'
    FEED_PAGE_PROCEED_TO_CART_BUTTON = '//button[contains(@class,"to-cart")]'

    # Billing details
    BILLING_DETAILS_EMAIL = '//input[@id="emailInput"]'
    BILLING_DETAILS_COUNTY_NAME = '//input[@class="search-input-component-u8YSu"]'
    BILLING_DETAILS_CONTINUE_TO_PAYMENT_BUTTON = '//button[@type="submit"]'
    COUNTRY_CODE_POPUP_SEARCH_FIELD = '//input[@id="country"]'
    BILLING_DETAILS_COUNTRY_NAME_POPUP_SEARCH_FIELD = '//input[@type="search"]'

    # Payment page
    PAYMENT_PAGE_CREDIT_CARD_BUTTON = '//button[contains(text(), "Credit Card")]'
    PAYMENT_PAGE_IFRAME_CREDIT_CARD = '//iframe[@title="Secure payment input frame"]'
    PAYMENT_PAGE_CARD_NUMBER_STRIPE = "//input[@id='Field-numberInput']"
    PAYMENT_PAGE_EXPIRATION_DATE_STRIPE = '//input[@id="Field-expiryInput"]'
    PAYMENT_PAGE_CVC_STRIPE = '//input[@id="Field-cvcInput"]'
    PAYMENT_PAGE_PAY_BUTTON = '//button[contains(text(), "Pay")]'
    CHECKOUT_SUMMERY_DETAILS = '(//div[@class="label-box"])[2]//p'
    PAYMENT_PAGE_PAYPAL_BUTTON_IFRAME = '(//iframe[contains(@name,"__privateStripeFrame")])[2]'
    PAYMENT_PAGE_PAYPAL_BUTTON_IFRAME_2 = '//div[contains(@class,"p-PayPalFrame")]//iframe'
    PAYMENT_PAGE_PAYPAL_BUTTON_IFRAME_3 = '(//div[contains(@id,"zoid-paypal-buttons-uid")]//iframe)[1]'
    PAYMENT_PAGE_PAYPAL_BUTTON = '//div[contains(@class,"paypal-button-container")]'

    # Cart page
    CART_PAGE_ITEM_TYPE_AND_NUMBER_OF_ITEMS = '//span[@class="description xsbody b"]'
    # CART_PAGE_PROCEED_TO_PAYMENT_BUTTON = '//button[@class="buttonComponent-j_QRg uppercase"]'
    CART_PAGE_PROCEED_TO_PAYMENT_BUTTON = '//button[@class="buttonComponent-j_QRg uppercase bold"]'
    NEW_CART_PAGE_PROCEED_TO_PAYMENT_BUTTON = '//button[@class="buttonComponent-j_QRg uppercase bold"]'
    SHARE_YOUR_MOMENTS_BUTTON = '//button[@class="buttonComponent-j_QRg uppercase bold"]'
    MEDIA_IN_THE_CART = '//div[@class="cart-list-item-KggNr cart-media-item-eQqCA"]'
    DELETE_FIRST_MEDIA_FROM_CART = '(//button[@class="buttonComponent-j_QRg delete-item"])[1]'
    APPROVE_DELETE_MEDIA_FROM_CART = '//div[@class="modal-buttons-block"]//button[@data-type="primary"]'
    CONTINUE_SHOPPING = '//p[@class="sb footer-link"]'




    # GuestApp - Add media page elements
    ADD_MEDIA_PAGE_VIA_SIDE_MENU = "//button[@class='buttonComponent-j_QRg '][3]"  # Need to chang
    ADD_MEDIA_RANDOM_ASSOCIATION_METHOD = "//div[@class='associations-block']//button"
    USERID_NUMBER_ASK_AN_OPERATOR = "//P[@class='body b']"
    ENTER_PHOTO_NUMBER_BUTTON = "//div[@class='associations-block']//button[2]"  # Need to change
    ATTRACTIONS_IN_CHOOSE_ATTRACTION_POPUP_GET_ID = "//form//div/input[not(@id='photoId')]"
    ATTRACTIONS_IN_CHOOSE_ATTRACTION_POPUP_CHOOSE_ATTRACTION = "//form//div[@class='radio-wrapper']"
    ENTER_PHOTO_NUMBER_FIELD = "//input[@id='photoId']"
    SEARCH_BUTTON_IN_ENTER_PHOTO_NUMBER = "//div[contains(@class,'padded')]//button[contains(@class,'buttonComponent')]"
    ADD_MEDIA_TOO_MANY_ATTEMPTS_BUTTON = "//h1[@class='title b']"
    PHOTO_NOT_FOUND_GOT_IT_BUTTON = "//div[@class='modal-buttons-block']"
    ADD_MEDIA_CLOSE_POPUP_TOO_MANY_ATTEMPTS = "//div[@class='modal-buttons-block']//button"
    ADD_MEDIA_IS_THIS_YOUR_PHOTO_YES_BUTTON = "(//div[@class='buttons-wrapper']//button[@type='button'])[2]"

    # Guest App - Account settings elements
    ACCOUNT_SETTING_PAGE_VIA_SIDE_MENU = "(//div[@class = 'menu-block']//button[@class = 'buttonComponent-j_QRg '])[3]"
    ACCOUNT_PAGE_DELETE_ACCOUNT_BUTTON = "(//span[@class='name l'])[2]"
    ACCOUNT_SETTINGS_CHANGE_LANGUAGE_BUTTON = "//div//span[@class='name l']"
    ACCOUNT_SETTINGS_MENU_SMS_SUBTITLE = "//label[@for='sms']"

    # Guest App - Help & support elements
    HELP_AND_SUPPORT_PAGE_VIA_SIDE_MENU = "(//div[@class = 'menu-block']//button[@class = 'buttonComponent-j_QRg '])[4]"
    HELP_AND_SUPPORT_SECTIONS = "(//div[@class='buttons-wrapper']//button[@class='buttonComponent-j_QRg '])"
    HELP_AND_SUPPORT_CONTACT_US_BUTTON = "//div[@id='float-wrapper']//button"
    CONTACT_US_SENT_VERIFICATION = "//div[@class='gG1SKx_8sRWXWUqBql1Ygd7tnyV_z43E']"

    # Guest App - Terms & conditions
    TERMS_AND_CONDITIONS_PAGE_VIA_SIDE_MENU = "(//div[@class = 'menu-block']//button[@class='buttonComponent-j_QRg '])[5]"
    TERMS_AND_CONDITIONS_TEXTS_LIST = "//div[contains(@class, 'terms-page')]//li"
    TERMS_AND_CONDITIONS_SUBTITLE = "(//div[contains(@class, 'terms-page')]//li)[4]"

    # contact us form web
    CONTACT_US_EMAIL = "//input[@id='request_anonymous_requester_email']"

    # Guest App - Privacy policy
    PRIVACY_POLICY_PAGE_VIA_SIDE_MENU = "(//div[@class = 'menu-block']" \
                                        "//button[@class = 'buttonComponent-j_QRg '])[6]"
    PRIVACY_POLICY_PAGE_LINKS = "//div[contains(@class, 'privacy-page')]//li"
    PRIVACY_POLICY_PAGE_2ND_LINK = "(//div[contains(@class, 'privacy-page')]//li//a)[2]"

    # Guest App - Inner screens header verification
    ALL_SCREENS_TITLE_ELEMENT = "//div[contains(@class, 'pa')]//h1"

    # taxamo page
    TAXAMO_EMAIL_FIELD = "//input[@type='email']"
    TAXAMO_CARD_NUMBER_FIELD = "//form//div[@class='CardNumberField-input-wrapper']//input"
    TAXAMO_EXPIRE_DATE_FIELD = "//input[@name='exp-date']"
    TAXAMO_CVC_FIELD = "//input[@name='cvc']"
    TAXAMO_PROCEED_BUTTON = "//button[@class='proceed pull-right']"
    TAXAMO_IFAME_ELEMENTS = "iframe"
    TAXAMO_PAYPAL_RADIOBUTTON = "//input[@id='payment_paypal']"
    TAXAMO_CREDIT_CARD_RADIOBUTTON = "//input[@id = 'payment_stripe']"
    TAXAMO_TOTAL_PRICE = "//div[@class='price']//h3[@class='ng-binding']"
    TAXAMO_I_SELF_DECLARE_BUTTON = "//button[@class='select-country']"

    # paypal page
    PAYPAL_PAGE_EMAIL_FIELD = "//input[@id='email']"
    PAYPAL_PAGE_NEXT_BUTTON = "//button[@id='btnNext']"
    PAYPAL_PAGE_PASSWORD_FIELD = "//input[@id='password']"
    PAYPAL_PAGE_LOGIN_BUTTON = "//button[@id='btnLogin']"
    PAYPAL_PAGE_PAY_NOW_BUTTON = "//button[@id='payment-submit-btn']"
