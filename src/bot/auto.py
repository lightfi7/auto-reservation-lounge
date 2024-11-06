import time
from datetime import datetime
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Basic configuration for logging
logging.basicConfig(level=logging.INFO,
                    filename='log.ini',
                    filemode='a',  # 'w' for overwrite, 'a' for append
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Logging messages at different levels
logging.debug("This is a debug message")  # Will not be logged since level is INFO
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")



appium_server_url = 'http://127.0.0.1:4723'


def is_at_bottom(driver):
    return driver.execute_script("return mobile.scrollGesture();")


def award(request, emulator, task):
    logging.info(f"user: {task['user_id']} {task['params']}")
    logging.info(f"emulator: {emulator['server_url']}/{emulator['usable_num']}")
    request.app.database["emulators"].update_one({"id": emulator["id"]}, {"$set": {
        "status": 1
    }})

    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='emulator-5558',
        appPackage='com.everylounge',
        appActivity='.MainActivity',
        autoGrantPermissions=True,
        noReset=True,
        udid=emulator["udid"]
    )

    # Start
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    wait = WebDriverWait(driver, 30)
    # el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    # el.click()

    # Login
    # armhouse.kz@gmail.com

    # el_close = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
    #                                                   '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView')))
    # # el_close = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView')
    # el_close.click()

    # el_continue = wait.until(
    #     EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@content-desc="В другой раз"]')))
    # el_continue.click()

    # Business Lounge \ Travel
    try:
        params = task['params']

        el_business = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
                                                             '//android.widget.ImageView[@content-desc="Выбрать\nбизнес-зал\nПутешествуйте\nс комфортом"]')))
        el_business.click()

        #
        el_search = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText')))
        el_search.click()
        title, location = params[0].split('@')
        el_search.send_keys(title)

        el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.view.View//*[contains(@content-desc, "{location}")]')))

        el.click()

        el = None
        name, group = params[1].split('@')
        while True:
            el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.view.View//*[contains(@content-desc, "{name}\n{group}")]')))
            if el is None:
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                    'new UiScrollable(new UiSelector().scrollable(true)).flingToEnd(5)')
            else:
                break
            time.sleep(5)
            if is_at_bottom(driver):
                break
        el.click()

        # el = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Авторизоваться')))
        # if el is None:
        #     print('Авторизоваться')
        #     return
        # el.click()

        el = None
        while True:
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                    'new UiScrollable(new UiSelector().scrollable(true)).flingToEnd(1)')
            time.sleep(5)
            if is_at_bottom(driver):
                break

        first_name, last_name = params[2].split('@')

        el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.EditText[1]/android.widget.ImageView')))
        el.click()
        el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
                                                    '//android.widget.ScrollView/android.view.View/android.widget.EditText[1]')))
        el.click()
        el.send_keys(first_name)

        el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.EditText[2]/android.widget.ImageView')))
        el.click()
        el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
                                                    '//android.widget.ScrollView/android.view.View/android.widget.EditText[2]')))
        el.click()
        el.send_keys(last_name)

        # el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.ImageView[3]')))
        # el.click()

        # return
        #
        # el = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Оформить')))
        # el.click()
        #
        # # get qr code
        # base64_image = driver.get_screenshot_as_png()
        # #
        #
        # request.app.database["tasks"].update_one({"id": emulator["id"]}, {"$set": {
        #     "success": True,
        #     "log": "Success",
        #     "base64_image": f"{base64_image}"
        # }})

        # request.app.database["emulators"].update_one({"id": emulator["id"]}, {"$set": {
        #     "status": 0,
        #     "usable_num": emulator["usable_num"] - 1
        # }})

        driver.back()
        driver.back()
        driver.back()

    except Exception as e:
        logging.info(f'error: {e}')
        request.app.database["tasks"].update_one({"id": emulator["id"]}, {"$set": {
            "success": False,
            "log": e,
        }})
        request.app.database["emulators"].update_one({"id": emulator["id"]}, {"$set": {
            "status": 0,
        }})
        print(e)

    # End







