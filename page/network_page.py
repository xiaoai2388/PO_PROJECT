class NetworkPage:

    def __init__(self,driver):

        self.driver = driver

    def click_network(self):
        # 点击移动网络
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
    def click_elect(self):
        # 点击网络类型选择
        self.driver.find_element_by_xpath("//*[contains(@text,'网络类型选择')]").click()
    def click_2G(self):
        # 点击2G网络
        self.driver.find_element_by_xpath("//*[contains(@text,'仅使用2G网络(更省电)')]").click()
    def click_3G(self):
        # 点击3G
        self.driver.find_element_by_xpath("//*[contains(@text,'3G网络优先')]").click()
