#-*- coding:UTF-8 -*-
'''示例2：替换函数(装饰)
装饰函数的参数是被装饰的函数的对象，返回原函数的对象
装饰的实质语句：myfunc = deco(myfunc)'''

def deco(func):
    print("before myfunc() called")
    func()
    print("after myfunc called")
    return func

def myfunc():
    print("myfunc() called")


myfunc = deco(myfunc)

print ("----------------------------")
myfunc()

