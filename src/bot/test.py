import time
from datetime import datetime

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.everylounge',
    appActivity='.MainActivity',
    autoGrantPermissions=True,
    noReset=True
)

appium_server_url = 'http://localhost:4723'


def is_at_bottom(driver):
    # Get the current visible elements
    current_elements = driver.find_elements(AppiumBy.XPATH, '//*[not(@visibility="gone")]')
    return len(current_elements) == 0  # Adjust based on your app's behavior



def award(request, emulator, task):
    request.app.database["emulators"].update_one({"_id": emulator["_id"]}, {"$set": {
        "status": 1
    }})

    action = dict(Type="Lounge", Actions=[
        {
            "Find": "Даллес@Вашингтон, США"
        },
        {
            "Find": "Turkish Airlines Lounge@Зал B"
        },
        {
            "Name": "<First name>@<Last name>",
        }
    ])


    # Start
    # driver = webdriver.Remote(emulator["server_url"], options=UiAutomator2Options().load_capabilities(capabilities))
    # wait = WebDriverWait(driver, 30)
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
        # el_business = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
        #                                                      '//android.widget.ImageView[@content-desc="Выбрать\nбизнес-зал\nПутешествуйте\nс комфортом"]')))
        # el_business.click()
        #
        # #
        # el_search = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText')))
        # el_search.click()
        # title, location = action['Actions'][0]['Find'].split('@')
        # el_search.send_keys(title)
        #
        # el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.view.View//*[contains(@content-desc, "{location}")]')))
        #
        # print(el.get_attribute('content-desc'))
        # el.click()
        #
        # el = None
        # name, group = action['Actions'][1]['Find'].split('@')
        # while True:
        #     print('=>')
        #     el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.view.View//*[contains(@content-desc, "{name}\n{group}")]')))
        #     if el is None:
        #         driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                             'new UiScrollable(new UiSelector().scrollable(true)).flingToEnd(5)')
        #     else:
        #         print(';)')
        #         break
        #     time.sleep(1)
        #     if is_at_bottom(driver):
        #         print(';(')
        #         break
        # el.click()
        #
        # # el = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Авторизоваться')))
        # # if el is None:
        # #     print('Авторизоваться')
        # #     return
        # # el.click()
        #
        # el = None
        # while True:
        #     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                             'new UiScrollable(new UiSelector().scrollable(true)).flingToEnd(5)')
        #     time.sleep(1)
        #     if is_at_bottom(driver):
        #         break
        #
        # first_name, last_name = action['Actions'][2]['Name'].split('@')
        #
        # el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.EditText[1]/android.widget.ImageView')))
        # el.click()
        # el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
        #                                             '//android.widget.ScrollView/android.view.View/android.widget.EditText[1]')))
        # el.click()
        # el.send_keys(first_name)
        #
        # el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.EditText[2]/android.widget.ImageView')))
        # el.click()
        # el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
        #                                             '//android.widget.ScrollView/android.view.View/android.widget.EditText[2]')))
        # el.click()
        # el.send_keys(last_name)
        #
        # # el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.ImageView[3]')))
        # # el.click()
        #
        # return
        #
        # el = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Оформить')))
        # el.click()
        #
        # # get qr code
        # base64_image = driver.get_screenshot_as_png()
        #

        request.app.database["tasks"].update_one({"_id": emulator["_id"]}, {"$set": {
            "success": True,
            "log": "Success",
            "base64_image": f"{'base64_image'}"
        }})
        # driver.back()
        # driver.back()
        # driver.back()
        # driver.quit()
    except Exception as e:
        request.app.database["tasks"].update_one({"_id": emulator["_id"]}, {"$set": {
            "success": False,
            "log": e,
        }})
        print(e)

    # End


    request.app.database["emulators"].update_one({"_id": emulator["_id"]}, {"$set": {
        "status": 0,
        "usable_num": emulator["usable_num"]-1
    }})





