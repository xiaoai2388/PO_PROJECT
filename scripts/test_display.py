import os, sys
# 表示在当前文件下搜索
sys.path.append(os.getcwd())

from appium import webdriver
from time import sleep
# 因为pytest运行方式，找不到自己创建模块，需要使用sys,os
from base.base_drvier import init_driver
from page.display_page import DisplayPage
class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        # 进行滑屏
        self.display_page.click_swipe()
        # 点击更多操作
        self.display_page.click_more()
        # 点击输入框
        self.display_page.click_input()
        # 输入内容“计算器”
        self.display_page.click_input_counter()
        # 点击返回
        self.display_page.click_back()

