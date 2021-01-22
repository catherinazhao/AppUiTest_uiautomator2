# -*- coding：utf-8 -*-
# @Author: catherina zhao
# @Time: 2021-01-18
# @IDE: Pycharm
# @File: test_taobao.py

import pytest
import allure

from util.load_ddt import LoadDDT
from util.connect import d
from util.constant import *


@allure.epic("项目名称：手机APP测试")
@allure.feature("测试模块：淘宝APP")
class TestTaoBaoApp(object):
	def setup_class(self):
		""" 启动淘宝app主界面 """
		d.app_start(TAOBAO_PKG_NAME, TAOBAO_MAIN_ACTIVITY, wait=True)


	def teardown_class(self):
		""" 清除测试数据并关闭淘宝app """
		d.app_clear(TAOBAO_PKG_NAME)
		d.app_stop(TAOBAO_PKG_NAME)

	@allure.story("登录模块测试")
	@allure.title("用户名和登录密码")
	@pytest.mark.parametrize("user, password, expect", LoadDDT.load_test_data(LOGIN_TEST_DATA))
	def test_login(self, user, password, expect):
		if d(text="我的淘宝").exists:
			d(resourceId="android:id/tabs").child(description="我的淘宝").click(timeout=5)



