# -*- coding：utf-8 -*-
# @Author: catherina zhao
# @Time: 2021-01-18
# @IDE: Pycharm
# @File: test_greektime.py
import time

import pytest
import allure

from util.load_ddt import LoadDDT
from util.connect import d
from util.constant import *


@allure.epic("项目名称：手机APP测试")
@allure.feature("测试模块：极客时间App")
class TestGeekTimeApp(object):

	def setup_class(self):
		""" 启动app主界面 """
		d.app_start(GEEK_PKG_NAME, GEEK_MAIN_ACTIVITY, wait=True)
		print("setupClass")
		init_app()

	def teardown_class(self):
		""" 清除测试数据并关闭淘宝app """
		print("tearDownClass")
		d.app_clear(GEEK_PKG_NAME)
		d.app_stop(GEEK_PKG_NAME)

	def teardown(self):
		d(resourceId="org.geekbang.geekTime:id/et_phone").clear_text()
		d(resourceId="org.geekbang.geekTime:id/et_password").clear_text()
		print("tearDown")

	def setup(self):
		print("setUp")

	def teardown_method(self):
		print("tearDown_method")

	def setup_method(self):
		print("setUp_method")



	@allure.story("登录模块测试")
	@allure.title("用户名和登录密码")
	@pytest.mark.parametrize("user_name, password, expect", LoadDDT().load_test_data(LOGIN_TEST_DATA))
	def test_login(self, user_name, password, expect):
		# 输入用户名和密码
		d(resourceId="org.geekbang.geekTime:id/et_phone").send_keys(user_name)
		d(resourceId="org.geekbang.geekTime:id/et_password").send_keys(password)

		# 获取当前组件的信息id.info
		is_enable = d(resourceId="org.geekbang.geekTime:id/tv_login").info['enabled']
		if not is_enable:
			# "user_name or password is incorrect, user_name: %s(len:%s), password: %s(len: %s)" % (user_name, len(user_name), password, len(password))
			print(11111111111)

		d(resourceId="org.geekbang.geekTime:id/tv_login").click(timeout=SHORT_TIME_OUT)
		if d(resourceId="nc_1-stage-1").exists:
			d.drag(127, 553, 440, 553)

		assert d.toast.get_message() == expect, "[Login] It is not login successfuly! "


""" App初始化界面 """
def init_app():
	while True:
		if d.app_current()['activity'] == 'org.geekbang.geekTime.project.start.UserProtocolActivity':
			d(resourceId="org.geekbang.geekTime:id/btn_dialog_right").click()

		if d(resourceId="org.geekbang.geekTime:id/iv_close").exists:
			d(resourceId="org.geekbang.geekTime:id/iv_close").click()

			break

	# d(text="我的").exists(timeout=LONG_TIME_OUT), "[LOGIN] GeekTime APP is open fail!"

	d(className="android.widget.RelativeLayout", index=3).click(timeout=LONG_TIME_OUT)

	if d(text='点击登录').exists:
		d(resourceId="org.geekbang.geekTime:id/tv_name").click(timeout=SHORT_TIME_OUT)

	if d(resourceId="org.geekbang.geekTime:id/tv_go_password_login").exists(timeout=SHORT_TIME_OUT):
		d(resourceId="org.geekbang.geekTime:id/tv_go_password_login").click(timeout=SHORT_TIME_OUT)







