from appium import webdriver


class DriverFactory:

    def __init__(self):
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            self.create_driver()
        return self.driver

    def create_driver(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.google.android.apps.nexuslauncher'
        desired_caps['appActivity'] = 'com.google.android.apps.nexuslauncher.NexusLauncherActivity'

        # desired_caps['automationName'] = 'UiAutomator2'
        # desired_caps['platformVersion'] = '4.2'
        # desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def kill_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
