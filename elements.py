#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "walkingsky"


desired_caps_meizu = {}
desired_caps_meizu['platformName'] = 'Android'
desired_caps_meizu['platformVersion'] = '8.1.0'
desired_caps_meizu['deviceName'] = 'txn'  # 安卓手机折本的名称
desired_caps_meizu['appPackage'] = 'com.taobao.live'
desired_caps_meizu['uuid'] = '872QAETA5QVCY'  # adb devices -l 显示的安卓手机的id
desired_caps_meizu['appActivity'] = '.home.activity.TaoLiveHomeActivity'
desired_caps_meizu['newCommandTimeout'] = '240'
# 不清空app数据
desired_caps_meizu['noReset'] = 'true'
desired_caps_meizu['fullReset'] = 'false'
# 是使用unicode编码方式发送字符串
# desired_caps['unicodeKeyboard'] = True
# 是将键盘隐藏起来; 输入中文的话，在字符串前面加上u，比如 u'中文'
# desired_caps['resetKeyboard'] = True


desired_caps_xiaoyao = {}
desired_caps_xiaoyao['platformName'] = 'Android'
desired_caps_xiaoyao['platformVersion'] = '7.1.2'
desired_caps_xiaoyao['deviceName'] = 'PCRT00'  # 安卓手机折本的名称
desired_caps_xiaoyao['appPackage'] = 'com.taobao.live'
# desired_caps_xiaoyao['uuid'] = '872QAETA5QVCY'  # adb devices -l 显示的安卓手机的id
desired_caps_xiaoyao['appActivity'] = '.home.activity.TaoLiveHomeActivity'
desired_caps_xiaoyao['newCommandTimeout'] = '240'
# 不清空app数据
desired_caps_xiaoyao['noReset'] = 'true'
desired_caps_xiaoyao['fullReset'] = 'false'

# 魅族真机的元素字典
meizu_elements = {
    # 首页
    "home page": {
        # 元宝中心按钮
        "yuanbao center button": {"text": "元宝中心按钮", "method":
                                  "xpath", "des": "//*[@resource-id='com.taobao.live:id/gold_common_image']"},
        # 视频列表的第二个视频
        "second video": {"text": "视频列表的第二个视频", "method":
                         "xpath", "des": "//*[@resource-id='com.taobao.live:id/taobao_live_base_list_recycler_view']/android.widget.FrameLayout[2]"},

    },
    # 元宝中心
    "yuanban center": {
        # 元宝按钮的领奖提示
        "reward tips": {"text": "元宝按钮的领奖提示", "method":
                        "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[1]/android.view.View[2]"},
        # 两个领奖时
        #
        # //com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[1]/android.view.View[2]
        # 每日收益
        # //com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View[1]
        # 元宝按钮
        "yuanba button": {"text": "元宝按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[1]/android.widget.Image[1]"},
        # 看直播60秒得68元宝 的按钮
        "watch video button": {"text": "看直播60秒得68元宝 的按钮", "method": "xpath", "des": "//*[@text='看直播60秒得68元宝']"},
        "watch video text": {"text": "领取成功的弹窗按钮提示文本", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[2]"},
        "watch video close": {"text": "关闭领奖成功弹层按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.widget.Image[2]"},
        # 关闭弹层按钮
        "close pop button": {"text": "关闭弹层按钮", "method": "xpath", "des": "//*[@text='O1CN01LxFPWH1Mmy2hurJW4_!!6000000001478-2-tps-54-54.png_']"},
        # 返回 按钮
        "return button": {"text": "返回 按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]"},
        # 签到按你
        "sign button": {"text": "签到按你", "method": "xpath", "des": ""},
    },
    # 元宝鸭
    "duck": {
        # 元宝鸭 打工挣钱按钮
        "duck button": {"text": "元宝鸭 打工挣钱按钮", "method": "xpath", "des": "//*[@text='O1CN01ZjCqq31SsMS8cJm1t_!!6000000002302-2-tps-225-225.png_']"},
        # 元宝鸭 打工挣钱按钮
        "job duck": {"text": "元宝鸭 打工挣钱按钮", "method": "xpath", "des": "//*[@resource-id='J-duck']/android.view.View[4]/android.widget.Image"},
        # 领元宝
        "action main": {"text": "领元宝", "method": "xpath", "des": "//*[@resource-id='action-main']"},
        "action main": {"text": "领元宝弹窗提示按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.Image[1]"},
        # 领取体力阿按钮
        "action drink": {"text": "领取体力阿按钮", "method": "xpath", "des": "//*[@resource-id='action-drink']/android.widget.Image"},
        "action drink tips": {"text": "领取体力提示", "method": "xpath", "des": "//*[@resource-id='action-drink']/android.view.View[2]"},
        "action drink tips1": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[2]"},
        "action drink tips2": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[3]"},
        "action drink tips3": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[5]"},
        "action drink tips4": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[6]"},
        "action drink tips5": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[8]"},
        "action drink tips6": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[9]"},
        "action drink close": {"text": "关闭领取体力提示弹窗按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Image"},
        "return button": {"text": "返回按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]"}
    },
    # 视频播放界面
    "video play": {
        # 元宝按钮
        "yuanba button": {"text": "元宝按钮", "method": "id", "des": "com.taobao.live:id/gold_center_image"},
        # 满蛋按钮
        "egg button": {"text": "满蛋按钮", "method": "id", "des": "com.taobao.live:id/gold_egg_image"},
        # 关闭视频按钮
        "close button": {"text": "关闭视频按钮", "method": "id", "des": "com.taobao.live:id/taolive_close_btn"},
        # 红包雨
        # 红包雨按钮
        "close hongbao": {"text": "红包雨按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Image"},
        # 视频播放任务提示
        "task tips": {"text": "视频播放任务提示", "method": "id", "des": "com.taobao.live:id/task_center_action"},
        #
        "task process": {"text": "元宝进度", "method": "xpath", "des": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView"}
    },
    # 签到页面
    "sign in": {
        # 签到按钮，需要拼接后面的xpath，添加 [i] ，来具体定位到具体的6个按钮中的某一个上
        "button": {"text": "签到按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc ='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[5]/android.view.View"},
        # 已签到提示图标
        "signed": {"text": "已签到提示图标", "method": "xpath", "des": "//*[@text='O1CN01lYhaf41SueO0HEah5_!!6000000002307-2-tps-25-17.png_']"},
        # 返回按钮
        "return button": {"text": "返回按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]"},
        # 提示弹窗
        "tips": {"text": "提示弹窗", "method": "id", "des": "J_dialogContainer"},
        # 提示关闭按钮
        "tips close": {"text": "提示关闭按钮", "method": "xpath", "des": "//*[@resource-id='J_dialogContainer']/android.view.View/android.view.View[2]"},
    }
}

# 逍遥模拟器的元素 字典
xiaoyao_elements = {
    # 首页
    "home page": {
        # 元宝中心按钮
        "yuanbao center button": {"text": "元宝中心按钮", "method":
                                  "xpath", "des": "//*[@resource-id='com.taobao.live:id/gold_common_image']"},
        # 视频列表的第二个视频
        "second video": {"text": "视频列表的第二个视频", "method":
                         "xpath", "des": "//*[@resource-id='com.taobao.live:id/taobao_live_base_list_recycler_view']/android.widget.FrameLayout[2]"},

    },
    # 元宝中心
    "yuanban center": {
        # 元宝按钮的领奖提示
        "reward tips": {"text": "元宝按钮的领奖提示", "method":
                        "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[1]/android.view.View[2]"},
        # 两个领奖时
        #
        # //com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[1]/android.view.View[2]
        # 每日收益
        # //com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View[1]
        # 元宝按钮
        "yuanba button": {"text": "元宝按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[1]/android.widget.Image[1]"},
        # 看直播60秒得68元宝 的按钮
        "watch video button": {"text": "看直播60秒得68元宝 的按钮", "method": "xpath", "des": "//*[@text='看直播60秒得68元宝']"},
        "watch video text": {"text": "领取成功的弹窗按钮提示文本", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[2]"},
        "watch video close": {"text": "关闭领奖成功弹层按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.widget.Image[2]"},
        # 关闭弹层按钮
        "close pop button": {"text": "关闭弹层按钮", "method": "xpath", "des": "//*[@text='O1CN01LxFPWH1Mmy2hurJW4_!!6000000001478-2-tps-54-54.png_']"},
        # 返回 按钮
        "return button": {"text": "返回 按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]"},
        # 签到按你
        "sign button": {"text": "签到按你", "method": "xpath", "des": ""},
    },
    # 元宝鸭
    "duck": {
        # 元宝鸭 打工挣钱按钮
        "duck button": {"text": "元宝鸭 打工挣钱按钮", "method": "xpath", "des": "//*[@text='O1CN01ZjCqq31SsMS8cJm1t_!!6000000002302-2-tps-225-225.png_']"},
        # 元宝鸭 打工挣钱按钮
        "job duck": {"text": "元宝鸭 打工挣钱按钮", "method": "xpath", "des": "//*[@resource-id='J-duck']/android.view.View[4]/android.widget.Image"},
        # 领元宝
        "action main": {"text": "领元宝", "method": "xpath", "des": "//*[@resource-id='action-main']"},
        "action main": {"text": "领元宝弹窗提示按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.Image[1]"},
        # 领取体力阿按钮
        "action drink": {"text": "领取体力阿按钮", "method": "xpath", "des": "//*[@resource-id='action-drink']/android.widget.Image"},
        "action drink tips": {"text": "领取体力提示", "method": "xpath", "des": "//*[@resource-id='action-drink']/android.view.View[2]"},
        "action drink tips1": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[2]"},
        "action drink tips2": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[3]"},
        "action drink tips3": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[5]"},
        "action drink tips4": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[6]"},
        "action drink tips5": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[8]"},
        "action drink tips6": {"text": "领取体力提示", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View[9]"},
        "action drink close": {"text": "关闭领取体力提示弹窗按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Image"},
        "return button": {"text": "返回按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]"}
    },
    # 视频播放界面
    "video play": {
        # 元宝按钮
        "yuanba button": {"text": "元宝按钮", "method": "id", "des": "com.taobao.live:id/gold_center_image"},
        # 满蛋按钮
        "egg button": {"text": "满蛋按钮", "method": "id", "des": "com.taobao.live:id/gold_egg_image"},
        # 关闭视频按钮
        "close button": {"text": "关闭视频按钮", "method": "id", "des": "com.taobao.live:id/taolive_close_btn"},
        # 红包雨
        # 红包雨按钮
        "close hongbao": {"text": "红包雨按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Image"},
        # 视频播放任务提示
        "task tips": {"text": "视频播放任务提示", "method": "id", "des": "com.taobao.live:id/task_center_action"},
        #
        "task process": {"text": "元宝进度", "method": "xpath", "des": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView"}
    },
    # 签到页面
    "sign in": {
        # 签到按钮，需要拼接后面的xpath，添加 [i] ，来具体定位到具体的6个按钮中的某一个上
        "button": {"text": "签到按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc ='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[5]/android.view.View"},
        # 已签到提示图标
        "signed": {"text": "已签到提示图标", "method": "xpath", "des": "//*[@text='O1CN01lYhaf41SueO0HEah5_!!6000000002307-2-tps-25-17.png_']"},
        # 返回按钮
        "return button": {"text": "返回按钮", "method": "xpath", "des": "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]"},
        # 提示弹窗
        "tips": {"text": "提示弹窗", "method": "id", "des": "J_dialogContainer"},
        # 提示关闭按钮
        "tips close": {"text": "提示关闭按钮", "method": "xpath", "des": "//*[@resource-id='J_dialogContainer']/android.view.View/android.view.View[2]"},
    }
}
