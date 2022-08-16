#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'walkingsky'


from appium import webdriver
import time
import random


def str_to_secends(str):
    # 解析领奖时间
    se_list = str.split(':')
    return int(se_list[0])*3600 + int(se_list[1])*60 + int(se_list[2])


def lingjiang(driver):
    # 查找开奖剩余时间
    get_time = False
    while get_time == False:
        try:
            time_str_remain = driver.find_element(
                'xpath', '//com.uc.webview.export.WebView[@content-desc="WVUCWebView"]/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]')
            time_str = time_str_remain.get_attribute("text")
            get_time = True
        except Exception as e:
            # print(e)
            time.sleep(1)

    if time_str == '领取奖励':
        print('点击领奖')
        # 点击领奖
        driver.find_element(
            'xpath', '//com.uc.webview.export.WebView[@content-desc="WVUCWebView"]/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]').click()

        time.sleep(2)
        # 关闭领奖
        driver.find_element(
            'xpath', '//com.uc.webview.export.WebView[@content-desc="WVUCWebView"]/com.uc.webkit.bb/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.widget.Image[2]').click()
        # 重新获取开奖时间
        return lingjiang(driver)
    else:
        print('元宝中心领奖剩余时间：' + time_str)
        # 转换成秒
        time_remain = str_to_secends(time_str)
        print(str(time_remain) + '秒')
        return time_remain


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'txn'  # 安卓手机折本的名称
desired_caps['appPackage'] = 'com.taobao.live'
desired_caps['uuid'] = '872QAETA5QVCY'  # adb devices -l 显示的安卓手机的id
desired_caps['appActivity'] = '.home.activity.TaoLiveHomeActivity'
desired_caps['newCommandTimeout'] = '120'
# 不清空app数据
desired_caps['noReset'] = 'true'
desired_caps['fullReset'] = 'false'

# 是使用unicode编码方式发送字符串
# desired_caps['unicodeKeyboard'] = True
# 是将键盘隐藏起来; 输入中文的话，在字符串前面加上u，比如 u'中文'
# desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.find_element_by_id("com.meizu.flyme.calculator:id/clear_simple").click()

# 准备 等待时间
time.sleep(10)
# height、width
size = driver.get_window_size()
start_x = size['width']*0.6
start_y = size['height']*0.9
end_x = size["width"]*0.5
end_y = size['height']*0.1

print(f"划屏坐标[{start_x},{start_y}]->[{end_x},{end_y}]")


# 点击元宝中心，查看领奖时间

# 循环等待元宝中心
yuanbaozhongxing = False
while yuanbaozhongxing == False:
    try:
        driver.find_element(
            "id", 'com.taobao.live:id/gold_common_image').click()
        print("找到元宝中心按钮，并点击")
        yuanbaozhongxing = True
    except Exception as e:
        # print(e)
        time.sleep(1)
i = 1
try:
    while True:
        time.sleep(5)
        time_remain = lingjiang(driver)
        print(str(time_remain) + '秒')
        # 开始计时
        start = time.time()
        time.sleep(1)
        # 第一次点击返回首页，后面返回的是直播视频界面
        driver.find_element(
            'xpath', '//com.uc.webview.export.WebView[@content-desc="WVUCWebView"]/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]').click()
        if i == 1:
            print('点击，从元宝中心返回首页')
            time.sleep(1)
            # 第一次进入，需要 点击第2个视频
            driver.find_element(
                'xpath', "//*[@resource-id='com.taobao.live:id/taobao_live_base_list_recycler_view']/android.widget.FrameLayout[2]").click()
            print('点击视频列表的第2个视频')
        else:
            print('点击，从元宝中心返回视频直播界面')
            time.sleep(1)
        i = i + 1

        while int(time.time() - start) < time_remain:

            # 红包雨广告 ，直接找关闭按钮
            hongbaoyu = True
            try:

                driver.find_element(
                    "xpath", '//com.uc.webview.export.WebView[@content-desc="WVUCWebView"]/com.uc.webkit.bb/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Image').click()
                print("发现红包雨的提示1，并点击关闭")
            except Exception as e:
                # print(e)
                # print("没有发现红包雨")
                hongbaoyu = False

            if hongbaoyu == False:
                try:
                    driver.find_element(
                        "xpath", '//com.uc.webview.export.WebView[@content-desc="WVUCWebView"]/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Image').click()

                    print("发现红包雨的提示2，并点击关闭")
                    hongbaoyu = True
                except Exception as e:
                    # print(e)
                    # print("没有发现红包雨")
                    hongbaoyu = False

            if hongbaoyu == False:
                print('没有发现红包雨')
            try:
                driver.swipe(start_x, start_y, end_x, end_y, 600)
                #driver.flick(start_x, start_y, end_x, end_y)
                print(time.strftime("%H:%M:%S", time.localtime()
                                    ) + '->剩余：' + str(int(time_remain - time.time() + start)) + '秒')
                print('滑动屏幕')
            except Exception as e:
                # print(e)
                print("划屏报错")
            a = random.randint(20, 60)
            if a > int(time_remain - time.time() + start):
                time.sleep(int(time_remain - time.time() + start) + 1)
            else:
                time.sleep(a)
            # break
        # 从直播视频页面进入元宝中心
        find = False
        while find == False:
            try:
                driver.find_element(
                    "id", 'com.taobao.live:id/gold_center_image').click()
                print('从直播视频页面进入元宝中心')
                find = True
            except Exception as e:
                # print(e)
                time.sleep(1)
            try:
                driver.find_element(
                    'id', 'com.taobao.live:id/gold_egg_image').click()
                print('点击满蛋图片，获取积分')
                driver.find_element(
                    "id", 'com.taobao.live:id/gold_egg_image').click()
                print('从直播视频页面进入元宝中心')
                find = True
            except Exception as e:
                time.sleep(1)


except KeyboardInterrupt:
    driver.quit()
    print('用户中断程序，程序退出')
    exit()
