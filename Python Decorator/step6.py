#-*- coding:UTF-8 -*-
'''示例6：对参数输入不确定的函数进行装饰
参数用(*args,**kwagrs)，自动适应变参和命名参数
'''
def deco(func):
    def _deco(*args,**kwargs):
        print ("before myfunc() called")
        ret = func(*args,**kwargs)
        print("alter %s called. result:%s" %(func.__name__,ret))
        return ret
    return _deco


@deco
def myfunc(a,b):
    print("myfunc(%s,%s) called" %(a,b))
    return a+b


@deco
def myfunc2(a,b,c):
    print("myfunc(%s,%s,%s) called" %(a,b,c))
    return a+b+c

myfunc(1,2)
myfunc(1,4)
myfunc2(1,2,8)
myfunc2(8,2,9)