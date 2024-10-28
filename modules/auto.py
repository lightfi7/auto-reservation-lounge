from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

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
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
el.click()
driver.quit()
