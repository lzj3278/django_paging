# coding: utf-8
from django.shortcuts import render, render_to_response
from fenye_app import models
from fenye_app import commom
from django.utils.safestring import mark_safe
from fenye_app import html_helper
#from fenye_app.html_helper import Pageinfo, pager


# Create your views here.

def index(request, page):
	page_int = commom.try_init(page, 1)  # 把所有page都变成int型
	count = models.host.objects.all().count()  # 计算总数据数
	#调用计算值的函数
	page_info = html_helper.Pageinfo(page_int, count, 10)
	start = page_info.start()
	end = page_info.end()
	all_page = page_info.all_page()

	count1 = models.host.objects.all()[start:end].count()  # 计算每一个显示的数据数
	result = models.host.objects.all()[start:end]
	page_str = html_helper.pager(page_int, all_page)
	date = {'data': result, 'count': count1, 'page': page_str}
	return render_to_response('index.html', date)
