from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

def start(request, emulator, task):
    request.app.database["emulators"].update_one({"_id": emulator["_id"]}, {"$set": {
        "status": 1
    }})
    driver = webdriver.Remote(emulator["server_url"], options=UiAutomator2Options().load_capabilities(capabilities))
    wait = WebDriverWait(driver, 30)
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
