# -*- coding：utf-8 -*-
# @Author: catherina zhao
# @Time: 2021-01-18
# @IDE: Pycharm
# @File: constant.py
import os

GEEK_PKG_NAME = "org.geekbang.geekTime"
TAOBAO_ACT_NAME = "corg.chromium.chrome.browser.ChromeTabbedAtivity"
GEEK_MAIN_ACTIVITY = "org.geekbang.geekTime.project.start.MainActivity"

SHORT_TIME_OUT = 5
LONG_TIME_OUT = 10

USER_LENGTH = 11
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIR_TEST_DATA = PROJECT_PATH + os.sep + "ddt"
LOGIN_TEST_DATA = DIR_TEST_DATA + os.sep + 'login_info'
