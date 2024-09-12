@staticmethod
def delete_cookies(driver):
    driver.delete_all_cookies()

@staticmethod
def open_and_switch_to_new_url_in_new_window(driver, new_url):
    # Open a new window
    driver.execute_script("window.open('');")

    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])
    driver.get(new_url)

@staticmethod
def switch_to_default_window(driver):
    # Switching to old tab
    driver.switch_to.window(driver.window_handles[0])

@staticmethod
def switch_and_close_selected_window(driver, window_number):
    driver.switch_to.window(driver.window_handles[int(window_number)])
    driver.close()

