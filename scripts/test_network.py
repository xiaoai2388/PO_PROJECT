import os, sys
# 表示在当前文件下搜索
sys.path.append(os.getcwd())


from appium import webdriver
from time import sleep
# 因为pytest运行方式，找不到自己创建模块，需要使用sys,os
from base.base_drvier import init_driver
from page.network_page import NetworkPage
class TestNetwoek:

    def setup(self):
        self.driver = init_driver()
        self.notwork_page = NetworkPage(self.driver)
    def test_network_2G(self):
        # 点击移动网络
        self.notwork_page.click_network()
        # 点击网络类型选择
        self.notwork_page.click_elect()
        # 点击2G
        self.notwork_page.click_2G()
        
    def test_network_3G(self):
        # 点击移动网络
        self.notwork_page.click_network()
        # 点击网络类型选择
        self.notwork_page.click_elect()
        # 点击3G
        self.notwork_page.click_3G()
        
 def test_network_4G(self):
        # 点击移动网络
        self.notwork_page.click_network()
        # 点击网络类型选择
        self.notwork_page.click_elect()
        # 点击3G
        self.notwork_page.click_4G()
        
 def test_network_5G(self):
        # 点击移动网络
        self.notwork_page.click_network()
        # 点击网络类型选择
        self.notwork_page.click_elect()
        # 点击3G
        self.notwork_page.click_5G()

 def test_network_6G(self):
        # 点击移动网络
        self.notwork_page.click_network()
        # 点击网络类型选择
        self.notwork_page.click_elect()
        # 点击3G
        self.notwork_page.click_5G()

