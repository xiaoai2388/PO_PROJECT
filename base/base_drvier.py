from appium import webdriver

def init_driver():
    # server启动参数
    device = {}
    # 设备信息
    device["deviceName"] = "654f25d"
    device["platformName"] = "Android"
    device["platformVersion"] = "6.0.1"
    # 输入中文
    device["unicodeKeyboard"] = True
    device["resetKeyboard"] = True
    # 过滤弹窗
    device["noReset"] = True
    # APP信息
    device["appPackage"] = "com.android.settings"
    device["appActivity"] = "com.oppo.settings.SettingsActivity"
    # 声明对象
    driver = webdriver.Remote("http://localhost:4723/wd/hub", device)
    return driver