#!/usr/bin/env python
# coding: utf-8


def try_init(arg, default):
	try:
		arg = int(arg)
	except Exception, e:
		arg = default

	return arg
