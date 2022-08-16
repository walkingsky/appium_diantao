#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'walkingsky'


from tkinter import E
from appium import webdriver
import time

from elements import meizu_elements, desired_caps_meizu
from elements import xiaoyao_elements
from model.driver import *


def reward(driver):
    # 查找开奖剩余时间
    time_str = get_element_attr(
        driver=driver, attribute="text", element=meizu_elements["yuanban center"]["reward tips"])

    if time_str == '领取奖励':
        print('点击领奖')
        # 点击领奖
        click_element(
            driver=driver, element=meizu_elements["yuanban center"]["yuanba button"])
        time.sleep(1)
        # 判断是否可以领奖
        str_find = get_element_attr(
            driver=driver, element=meizu_elements["yuanban center"]["watch video text"], attribute='text')
        if "看直播" not in str_find:  # 不能领奖就关闭弹窗，重新获取领奖时间
            click_element(
                driver=driver, element=meizu_elements["yuanban center"]["watch video close"])
            time.sleep(1)
            return reward(driver)

        click_element(
            driver=driver, element=meizu_elements["yuanban center"]["watch video button"])
        reward_video(driver)
        # 关闭领奖
        # click_element(
        #    driver=driver, element=meizu_elements["yuanban center"]["close pop button"])
        # 重新获取开奖时间
        return reward(driver)
    else:
        print('元宝中心领奖剩余时间：' + time_str)
        # 转换成秒
        time_remain = str_to_secends(time_str)
        print(str(time_remain) + '秒')
        return time_remain


def reward_video(driver):
    """
    查看领奖视频
    """
    while True:
        str_element = get_element_attr(
            driver=driver, element=meizu_elements["video play"]["task tips"], attribute="text")
        if str_element == False:
            # click_element(
            #    driver=driver, element=meizu_elements["video play"]["close button"], retry=-1)
            enter_yuanbao_center(driver)
            print("视频播放60秒完成")
            swip_screen(driver, point=point)
            time.sleep(2)
            return
        # 红包雨广告 ，直接找关闭按钮
        click_element(
            driver=driver, element=meizu_elements["video play"]["close hongbao"])
        time.sleep(1)


def job_duck(driver):
    """
    打工鸭操作
    """
    str_element = get_element_attr(
        driver=driver, element=meizu_elements["duck"]["action drink tips"], attribute='text')
    if str_element == "去领取":
        click_element(
            driver=driver, element=meizu_elements["duck"]["action drink"])
        time.sleep(1)
        click_element(
            driver=driver, element=meizu_elements["duck"]["action drink close"])
        return job_duck(driver=driver)
    else:
        # 时间
        #remain_time = str_to_secends(str)
        time1 = get_element_attr(
            driver=driver, element=meizu_elements["duck"]["action drink tips1"], attribute='text')
        time2 = get_element_attr(
            driver=driver, element=meizu_elements["duck"]["action drink tips2"], attribute='text')
        time3 = get_element_attr(
            driver=driver, element=meizu_elements["duck"]["action drink tips3"], attribute='text')
        time4 = get_element_attr(
            driver=driver, element=meizu_elements["duck"]["action drink tips4"], attribute='text')
        time5 = get_element_attr(
            driver=driver, element=meizu_elements["duck"]["action drink tips5"], attribute='text')
        time6 = get_element_attr(
            driver=driver, element=meizu_elements["duck"]["action drink tips6"], attribute='text')
        remain_time = int(time1+time2)*3600 + \
            int(time3+time4)*60 + int(time5 + time6)
        print("打工赚钱剩余时间："+str(remain_time) + "秒")
        return remain_time


def return_ui(driver, from_ui="duck"):
    """
    返回视频列表 main 页面
    """
    if from_ui == "duck":
        # 返回元宝中心
        click_element(
            driver=driver, element=meizu_elements["duck"]["return button"])
        time.sleep(2)

    click_element(
        driver=driver, element=meizu_elements["yuanban center"]["return button"])
    time.sleep(3)


def enter_duck(driver):
    """
    从元宝中心，进入打工鸭界面
    """
    # 进入打工鸭界面
    click_element(
        driver=driver, element=meizu_elements["duck"]["job duck"])


def enter_yuanbao_center(driver, from_ui='main'):
    if from_ui == "main":
        click_element(
            driver=driver, element=meizu_elements["home page"]["yuanbao center button"], retry=-1)
    else:
        click_element(
            driver=driver, element=meizu_elements["video play"]["egg button"])
        click_element(
            driver=driver, element=meizu_elements["video play"]["yuanba button"])


desired_caps = desired_caps_meizu

# 是使用unicode编码方式发送字符串
# desired_caps['unicodeKeyboard'] = True
# 是将键盘隐藏起来; 输入中文的话，在字符串前面加上u，比如 u'中文'
# desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 准备 等待时间
time.sleep(10)
# 设置划屏坐标
size = driver.get_window_size()
start_x = size['width']*0.6
start_y = size['height']*0.9
end_x = size["width"]*0.5
end_y = size['height']*0.1
point = [start_x, start_y, end_x, end_y]
print(f"划屏坐标[{start_x},{start_y}]->[{end_x},{end_y}]")


# 点击进入元宝中心，
enter_yuanbao_center(driver, 'main')


# 获取开奖剩余时间
time.sleep(5)
reward_time_remain = reward(driver)
# 领奖开始计时
reward_start = time.time()


"""
# 进入打工鸭界面,这个界面获取元素太太慢了。 弃用了
enter_duck(driver)
time.sleep(3)
# 获取体力获奖剩余时间
duck_drink_remain_time = job_duck(driver)
duck_start_time = time.time()

# 返回元宝中心
click_element(driver=driver, element=meizu_elements["duck"]["return button"])
time.sleep(3)
"""

# 返回视频直播列表页面
click_element(
    driver=driver, element=meizu_elements["yuanban center"]["return button"])
time.sleep(3)
click_element(
    driver=driver, element=meizu_elements["home page"]["second video"])
# 进入循环
time.sleep(3)
i = 1
while True:
    time.sleep(1)

    # 定时划屏 ，后面换成根据能量进度条划屏
    if i % 5 == 0:
        find_str = get_element_attr(
            driver=driver, element=meizu_elements["video play"]["task process"], attribute='text')
        if find_str == '6/6':
            # 红包雨广告 ，直接找关闭按钮
            click_element(
                driver=driver, element=meizu_elements["video play"]["close hongbao"])
            swip_screen(driver=driver, point=point)
            print(time.strftime("%H:%M:%S", time.localtime()
                                ) + '->元宝中心领奖剩余：' + str(int(reward_time_remain - time.time() + reward_start)) + '秒')

    """
    if i % 15 == 0:  # 每隔15秒打印 打工鸭 体力领取时间
        print(time.strftime("%H:%M:%S", time.localtime()
                            ) + '->打工鸭体力剩余：' + str(int(duck_drink_remain_time - time.time() + duck_start_time)) + '秒')

    if int(time.time() - duck_start_time) > duck_drink_remain_time:  # 打工鸭体力领取到时
        enter_yuanbao_center(driver, 'live')
        enter_duck(driver)
        time.sleep(3)
        duck_drink_remain_time = job_duck(driver)
        duck_start_time = time.time()
        # 返回元宝中心
        return_ui(driver)
    """
    if int(time.time() - reward_start) > reward_time_remain:  # 元宝中心领奖时间到
        # 红包雨广告 ，直接找关闭按钮
        click_element(
            driver=driver, element=meizu_elements["video play"]["close hongbao"])
        enter_yuanbao_center(driver, 'live')
        time.sleep(3)
        reward_time_remain = reward(driver)
        # 领奖开始计时
        reward_start = time.time()

        return_ui(driver, 'yuanbao center')

    time.sleep(1)
    i = i + 1
    if i > 3600:
        i = 1
