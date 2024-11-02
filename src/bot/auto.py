from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.everylounge',
    appActivity='.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
wait = WebDriverWait(driver, 30)

# Login
#armhouse.kz@gmail.com

el_close = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView')))
# el_close = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView')
el_close.click()

el_continue = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@content-desc="В другой раз"]')))
el_continue.click()

el_business = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Выбрать\nбизнес-зал\nПутешествуйте\nс комфортом"]')))
el_business.click()

# Business Lounge \ Travel
el_search = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText')))
el_search.click()
el_search.send_keys('Даллес')




# Upgrade \ Flight






# Order \ VIP services























# driver.quit()


