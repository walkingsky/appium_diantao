#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "walkingsky"


import time

DEBUG_FLG = True


def str_to_secends(str):
    """ 
    解析领奖时间
    Args:
        str 解析的时间字符窜 '00:01:12'
    return:
        int 秒数
    """
    se_list = str.split(':')
    return int(se_list[0])*3600 + int(se_list[1])*60 + int(se_list[2])


def find_element(driver, element, retry=3, debug=DEBUG_FLG):
    """ 
    查找元素，没找到返回False，找到后返回元素
    Args:
        driver : 测试驱动   
        element : 元素描述,字典  {"method":"id", "des": "com.taobao.live:id/gold_common_image","text":"元素描述"}
        retry: int 重试次数，每次间隔1秒 ,-1 为循环重试 ,-1 为循环重试
        debug: bool 是否将异常信息输出
    return:
        False 没有找打元素
        找到元素
    """
    loop = False
    method = element["method"]
    xpath = element["des"]
    if retry == -1:
        loop = True
    while True:
        retry = retry - 1
        try:
            finded_element = driver.find_element(method, xpath)
            if debug == True:
                print("成功定位到元素：" + element["text"])
            return finded_element
        except Exception as e:
            if debug == True:
                print(e)
            if (retry == 0 and loop == False) or retry < -100:  # 最大重试次数 100秒
                return False
        time.sleep(1)


def get_element_attr(driver, element, attribute: str, retry=3, debug=DEBUG_FLG):
    """
    获取元素的属性，没找到返回False，找到后返回属性值
    Args:
        driver : 测试驱动   
        element : 元素描述,字典  {"method":"id", "des": "com.taobao.live:id/gold_common_image","text":"元素描述"}
        attribute : str 属性名称
        retry: int 重试次数，每次间隔1秒 ,-1 为循环重试
        debug: bool 是否将异常信息输出
    return:
        False 没有找打元素
    """
    loop = False
    method = element["method"]
    xpath = element["des"]
    if retry == -1:
        loop = True
    while True:
        retry = retry - 1
        try:
            find_element = driver.find_element(
                method, xpath)
            find_str = find_element.get_attribute(attribute)
            if debug == True:
                print("获取到的元素属性值为：" + find_str)
            return find_str
        except Exception as e:
            if debug == True:
                print(e)
            if (retry == 0 and loop == False) or retry < -100:  # 最大重试次数 100秒
                return False
        time.sleep(1)
    """
    element = find_element(driver=driver, element=element,
                           retry=retry, debug=debug)
    if element == False:
        return False
    else:
        try:
            str = element.get_attribute(attribute)
            if debug:
                print("获取到的元素属性值为：" + str)
            return str
        except Exception as e:
            if debug == True:
                print(e)
            return False
    """


def click_element(driver, element,  retry=3, debug=DEBUG_FLG):
    """
    点击元素
    Args:
        driver : 测试驱动   
        element : 元素描述,字典  {"method":"id", "des": "com.taobao.live:id/gold_common_image","text":"元素描述"}
        retry: int 重试次数，每次间隔1秒 ,-1 为循环重试
        debug: bool 是否将异常信息输出
    return:
        False 没有找打元素
    """
    loop = False
    method = element["method"]
    xpath = element["des"]
    if retry == -1:
        loop = True
    while True:
        retry = retry - 1
        try:
            driver.find_element(method, xpath).click()
            if debug == True:
                print("成功点击元素：" + element["text"])
            return True
        except Exception as e:
            if debug == True:
                print(e)
            if (retry == 0 and loop == False) or retry < -100:  # 最大重试次数 100秒
                print("未能成功点击元素：" + element["text"])
                return False
        time.sleep(1)

    """
    element_finded = find_element(driver=driver, element=element,
                                  retry=retry, debug=debug)
    if element_finded != False:
        element_finded.click()
        print("成功点击元素：" + element["text"])
    else:
        print("没有找到元素：" + element["text"] + "，无法点击")
    """


def swip_screen(driver, point: list, debug=DEBUG_FLG):
    """
    划屏操作
    Args:
        driver : 测试驱动
        point: dict point[start_x,start_y, end_x, end_y]
    """
    try:
        driver.swipe(point[0], point[1], point[2], point[3], 600)
        print('滑动屏幕')
    except Exception as e:
        if debug == True:
            print(e)
        print("划屏报错")
