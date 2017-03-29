#-*- coding:UTF-8 -*-
from __future__ import print_function

#获取/etc/passwd中第一列和最后一列输出到/tmp/passwd文件中
with open('/etc/passwd') as source_file,open('/tmp/passwd','w') as target_file:
    for line in source_file:
        print(line.split(':')[0],line.split(':')[-1],file=target_file)
