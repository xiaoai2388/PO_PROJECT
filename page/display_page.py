from time import sleep
from selenium.webdriver.common.by import By



class DisplayPage:

    def __init__(self,driver):
        self.driver = driver

    def click_swipe(self):
        # 进行滑屏
        for i in range(5):
            self.driver.swipe("350", "1100", "350", 700)
    def click_more(self):
        # 点击更多应用
        #self.driver.find_element_by_xpath("//*[contains(@text,'更多应用')]").click()
        # 上下等价关系
        self.driver.find_element(By.XPATH,"//*[contains(@text,'更多应用')]").click()
    def click_input(self):
        # 点击输入框
        #self.driver.find_element_by_id("android:id/input").click()
        self.driver.find_element(By.ID, "android:id/input").click()
    def click_input_counter(self):
        # 输入“计算器”
        #self.driver.find_element_by_class_name("miui.widget.ClearableEditText").send_keys("计算器")
        self.driver.find_element(By.CLASS_NAME, "miui.widget.ClearableEditText").send_keys("计算器")
    def click_back(self):
        # 点击返回
        sleep(3)
        #self.driver.find_element_by_id("miui:id/search_btn_cancel").click()
        self.driver.find_element(By.ID, "miui:id/search_btn_cancel").click()
