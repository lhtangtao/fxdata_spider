#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = timer
#author = tangtao
#time   = 2017/3/24 17:51
#Description=添加描述信息
#eMail   =tangtao@lhtangtao.com
#git     =lhtangtao
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""

import datetime
import time
from get_info_from_163.http.class_info import *
from get_info_from_163.tools.connect_Linux import connect_linux

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def timer_customize(time_stamp, expect_start_time='2017-03-21 17:04:00', expect_end_time='2017-03-21 17:20:00'):
    """
    输入期望开始的时间随后每隔五分钟会调用一次
    :param time_stamp:
    :param expect_end_time:
    :param expect_start_time:
    :return:
    """
    expect_start_time = datetime.datetime.strptime(expect_start_time, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(
        minutes=1)
    expect_end_time = datetime.datetime.strptime(expect_end_time, '%Y-%m-%d %H:%M:%S')
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 显示现在的时间
    now_time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')  # 格式化当前的时间
    if now_time > expect_start_time:
        log.info(u'预期开始时间不能大于现在的时间' + '\n' + u'结束进程')
        sys.exit()
    if expect_end_time < expect_start_time:
        log.info(u'结束时间不能小于开始时间' + '\n' + u'结束进程')
        sys.exit()
    expect_end_time = expect_end_time + datetime.timedelta(minutes=5)
    node = 1
    curl_log = "./curl_log/curl_log_" + time_stamp
    log.info(u'清除指定的时间戳的curl_log文件中的内容，之前的内容都是测试kind_info中的信息而产生的')
    f = open(curl_log, 'w+')
    f.close()
    init_debug_info = connect_linux(
        ' /home/icache/icached debug', '192.168.1.106')
    log.info(u'debug信息如下所示：' + '\n' + init_debug_info)
    f = open(curl_log, 'a')
    f.write(init_debug_info)
    f.flush()
    count_kind1 = 1
    count_kind2 = 1
    count_kind3 = 1
    count_kind4 = 1
    count_kind5 = 1
    log.info(u'开始执行循环操作')
    while True:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 显示现在的时间
        log.info(u'当前的时间是：' + unicode(now_time))
        now_time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')  # 格式化当前的时间
        log.info(u'期望结束的时间加上五分钟是：' + str(expect_end_time))  # 离结束还有多久
        wait_to_end = str(expect_end_time - now_time)  # 期望结束的时间+5分钟-当前的时间 即剩下多少时间
        log.info(u'离结束的时间还有几分几秒（请自行减去五分钟）：' + str(wait_to_end))  # 离结束还有几分几秒
        end_hour = int(wait_to_end.split(':')[0])
        end_minute = int(wait_to_end.split(':')[1])
        end_second = int(wait_to_end.split(':')[2])
        seconds_to_wait_end = end_hour * 3600 + end_minute * 60 + end_second  # 离跳出循环还有几秒钟
        log.info(u'离结束时间还有几秒：' + str(seconds_to_wait_end))
        if seconds_to_wait_end < 300:
            log.info(u'马上自动退出程序，请查看基础日志')
            break
        else:
            log.info(u"倒计时还没结束,等待倒计时")
        wait_time = str(expect_start_time - now_time)
        hours = int(wait_time.split(':')[0])
        minute = int(wait_time.split(':')[1])
        seconds = int(wait_time.split(':')[2])
        seconds_to_wait = hours * 3600 + minute * 60 + seconds
        log.info(u"等待时间为" + str(seconds_to_wait) + u'秒后开始执行')
        time.sleep(seconds_to_wait)
        if node == 1:
            log.info(u'开始执行kind1的实际curl操作')
            kind1(time_stamp)
            log.info(u'kind1执行了' + str(count_kind1) + u"次")
            count_kind1 += 1
        elif node == 2:
            log.info(u'开始执行kind2的实际curl操作')
            kind2(time_stamp)
            log.info(u'kind2执行了' + str(count_kind2) + u"次")
            count_kind2 += 1
        elif node == 3:
            log.info(u'开始执行kind3的实际curl操作')
            kind3(time_stamp)
            log.info(u'kind3执行了' + str(count_kind3) + u"次")
            count_kind3 += 1
        elif node == 4:
            log.info(u'开始执行kind4的实际curl操作')
            kind4(time_stamp)
            log.info(u'kind4执行了' + str(count_kind4) + u"次")
            count_kind4 += 1
        elif node == 5:
            log.info(u'开始执行kind5的实际curl操作')
            kind5(time_stamp)
            log.info(u'kind5执行了' + str(count_kind5) + u"次")
            count_kind5 += 1
        time_line = datetime.timedelta(minutes=5)  # 两个kind之间每次curl间隔的时间，要求为5分钟
        expect_start_time = expect_start_time + time_line
        log.info(u'下一次的curl_kind操作开始时间为：' + unicode(expect_start_time))
        node += 1
        if node == 6:
            node = 1
    end_debug_info = connect_linux('/home/icache/icached debug', '192.168.1.106')
    log.info(u'结束所有的curl操作，debug_info如下所示：' + end_debug_info)
    f.write(end_debug_info)
    log.info(u'kind执行的次数写入到curl_log文件中')
    f.write('count_kind1:' + str(count_kind1) + '\n')
    f.write('count_kind2:' + str(count_kind2) + '\n')
    f.write('count_kind3:' + str(count_kind3) + '\n')
    f.write('count_kind4:' + str(count_kind4) + '\n')
    f.write('count_kind5:' + str(count_kind5) + '\n')
    f.close()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log.info(u'当前的时间为：'+unicode(current_time))