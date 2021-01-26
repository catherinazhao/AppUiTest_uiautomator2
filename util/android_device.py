# -*- coding：utf-8 -*-
# @Author: catherina zhao
# @Time: 2021-01-18
# @IDE: Pycharm
# @File: android_device.py
import os
import re
import sys

import uiautomator2 as u2


class ControlDevice(object):
	def __init__(self):
		""" 等待ADB连接上 """
		os.system("adb wait-for-device")
		serial_no = self.get_serial
		if not serial_no:
			print("Please set you android device")
			sys.exit()

	""" 取得当前设备的设备ID """
	@property
	def get_serial(self):
		""" 从系统的配置文件中读取设备信息 """
		res = os.popen('adb shell getprop ro.serialno')
		# 等价于 res = os.popen('adb get-serialno') 都是获取安卓设备序列号
		serial = res.readline()
		if not serial:
			print("Please connect you test device")
			return None

		return serial



def connect():
	""" 连接安卓设备 """
	d = u2.connect()
	return d



