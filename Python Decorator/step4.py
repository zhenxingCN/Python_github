#-*- coding:UTF-8 -*-
'''示例4：使用内嵌包装函数来确保每次新函数都被调用'''

def deco(func):
    def _deco():
        print("before myfunc() called")
        func()
        print("after myfunc() called")
    return _deco

@deco
def myfunc():
    print("myfunc() called")
    return  'ok'

myfunc()
myfunc()
