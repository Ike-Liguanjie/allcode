# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 3:31 下午
# @Author  : Ike
# @File    : config.py
# @Software: PyCharm
import functools

from datetime import datetime

sort_list = [3, 1, 5, 4, 2, 6]


def time_log(sort_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            now = datetime.now()
            f = func(*args, **kw)
            print("{}的运行时间为{}".format(sort_name, datetime.now() - now))
            return f

        return wrapper

    return decorator
