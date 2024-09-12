class SideMenuParameters():

    @staticmethod
    def get_url_verification_string(key):
        pages = {
            "Home": "feed",
            "Add media": "collect-media",
            "Account setting": "settings",
            "Help and support": "faq",
            "Terms and conditions": "terms-and-conditions",
            "Privacy policy": "privacy-policy"
        }
        return pages[key]
