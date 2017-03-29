#-*- coding:UTF-8 -*-
from __future__ import print_function

#列表推导
list1 = [i for i in range(10)]

#集合推导
set1 = {i for i in range(10)}

#字典推导
dict1 = {i:i*i for i in range(10)}

print(list1)
print(set1)
print(dict1)