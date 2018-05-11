# -*- coding: utf-8 -*-

from __future__ import print_function

# import data
# # 414478124 1084660392
# jsonb = data.get_data(414478124)
# print(jsonb)


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#
#
# def fab2(max):
#     yield range(1, max)
#
#
# f = fab(5)
#
# for s in f:
#     print(s)
# print(f.next())
# print(f.next())
# print(f.next())
# print(f.next())
# print(f.next())
# print(f.next())


# y, n = 'y', 'n'
# try:
#     isCoders = input(r'您是否有其它程序语言基础（y/n）：')
#     if isCoders == y:
#         print ('本文档适合您阅览')
#     elif isCoders == n:
#         print ('请在成人陪同下继续阅览')
# except NameError:
#     print ('限制级文档，本文档不适合您继续观看')


# cc = None
# cc = r'''first
#          second'''
# print(cc)
# chinese = u'中文'
# print (len(chinese))
# print (ord('A'))
#
# names = ['Tow Dog','Shan Pao']
# print (names.index('Shan Pao'))

# def log(fn):
#     def wrapper(*args, **kw):
#         print('call %s():' % fn.__name__)
#         return fn(*args, **kw)
#
#     return wrapper
#
#
# @log
# def date():
#     print('2018-05-01')
#
#
# date()
import functools

# def log(weather):
#     def decorator(fn):
#         @functools.wraps(fn)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (weather, fn.__name__))
#             return fn(*args, **kw)
#
#         return wrapper
#
#     return decorator
#
#
# @log('sunny')
# def date():
#     print('2018-05-01')
#
#
# print(date.__name__)

int2 = functools.partial(int, base=16)
dd = int2('100000')
print("%d" % dd)
