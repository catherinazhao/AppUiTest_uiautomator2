# -*- coding：utf-8 -*-
# @Author: catherina zhao
# @Time: 2021-01-18
# @IDE: Pycharm
# @File: load_ddt.py
# @Function: load data dependency test from txt
import re

PATTERN = r"{(.*)}"


class LoadDDT(object):
	""" 通过DDT的方式加载测试用例 """
	def __init__(self):
		self.datas = {}

	def load_test_data(self, data_file):
		""" 返回依赖的测试用例内容 """
		self.open_file(data_file)
		data_list = []
		for key, value in self.datas.items():
			pat = re.compile(PATTERN)
			cur_data = [val.strip() for val in re.findall(pat, value)[0].split(";")]
			data_list.append(cur_data)

		return data_list

	""" 读取测试数据文件 """
	def open_file(self, file):
		print(file)
		with open(file, 'r', encoding='utf-8') as f:
			for line in f.readlines():
				if line.startswith("#"):
					continue
				else:
					line = line.strip()
					case_name, cur_data = line.split(":")[0], line.split(":")[1]
					self.datas[case_name] = cur_data


if __name__ == '__main__':
	ldt = LoadDDT(r"C:\Users\yangzhao\Desktop\Software\AppUiTest_uiautomator2\ddt\login_info")
	ldt.load_test_data()