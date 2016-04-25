#!/usr/bin/env python
# coding: utf-8
from django.utils.safestring import mark_safe


class Pageinfo(object):
	'''

	'''

	def __init__(self, page, count, default_num):
		self.Page = page
		self.Count = count
		self.Page_per_item = default_num

	def start(self):
		return (self.Page - 1) * self.Page_per_item

	def end(self):
		return self.Page * self.Page_per_item

	def all_page(self):
		temp = divmod(self.Count, self.Page_per_item)  # 用来判断总数据能不能被整除，不能整出，加1
		if temp[1] == 0:
			all_page = temp[0]
		else:
			all_page = temp[0] + 1
		return all_page


def pager(page, all_page):
	"""

	:param page: 当前页
	:param all_page: 总页数
	:return: html的字符串
	"""
	page_list = []
	first_html = '<a href="/index/%d">首页</a>' % (1,)  # 定义首页
	page_list.append(first_html)
	if page <= 1:  # 上一页 并添加限制 不能是0
		prev_html = '<a href="/index/1"><上一页</a>'
	else:
		prev_html = '<a href="/index/%d"><上一页</a>' % (page - 1,)

	page_list.append(prev_html)

	if all_page < 11:
		begin = 0
		end = all_page
	else:
		if page < 6:
			begin = 0
			end = 11
		else:
			if page + 5 >= all_page:
				begin = all_page - 11
				end = all_page
			else:
				begin = page - 6
				end = page + 5
	if page == all_page:
		for i in range(page - 7, all_page):  # 循环添加到每个字符串中 并对应相应的页码
			if page == i + 1:  # 判断 如果url的page等于当前页则 加样式
				a_html = '<a style="color: brown" href="/index/%d">%d</a>' % (i + 1, i + 1)
			else:
				a_html = '<a  href="/index/%d">%d</a>' % (i + 1, i + 1)
			page_list.append(a_html)
	else:
		for i in range(begin, end):  # 循环添加到每个字符串中 并对应相应的页码
			if page == i + 1:  # 判断 如果url的page等于当前页则 加样式
				a_html = '<a style="color: brown" href="/index/%d">%d</a>' % (i + 1, i + 1)
			else:
				a_html = '<a  href="/index/%d">%d</a>' % (i + 1, i + 1)
			page_list.append(a_html)

		all_page_html = '<a href="/index/%d">...%d</a>' % (all_page, all_page)
		page_list.append(all_page_html)
		if page >= all_page:  # 判断 下一页不嗯呢该无限下一页，限制到最后一页
			next_html = '<a href="/index/%d">下一页></a>' % (all_page,)
		else:
			next_html = '<a href="/index/%d">下一页></a>' % (page + 1,)
		page_list.append(next_html)

		end_html = '<a href="/index/%d">尾页</a>' % (all_page,)
		page_list.append(end_html)

	page1 = mark_safe(' '.join(page_list))  # 把所有的a标签都能被html解析

	return page1
