from __future__ import print_function
import os
import datetime
import time
path = '/home/zhenxing/script1.py'

print("split path:",os.path.split(path))
print("dirname:",os.path.dirname(path))
print("basename:",os.path.basename(path))
print("split text:",os.path.splitext(path))
print("get current work directory:",os.getcwd())
print("current user home directory:",os.path.expanduser('~'))
print("abs path:",os.path.abspath('.'))
print("path join:",os.path.join('~','python_study','demo.py'))
print("path join user home:",os.path.join(os.path.expanduser('~'),'python_study','demo.py'))
print("/home/zhenxing/script1.py is abs:",os.path.isabs(path))
print(". is abs:",os.path.isabs('.'))
print("abspath use __file__ :",os.path.abspath(__file__))


print("get file access time:",os.path.getatime(__file__))
print("get file access time:",datetime.datetime.fromtimestamp(os.path.getatime(__file__)).strftime('%Y-%m-%d %H:%M:%S'))
print("get file access time:",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(os.path.getatime(__file__)))))
print("get file modify time:",os.path.getmtime(__file__))
print("get file create time:",os.path.getctime(__file__))
print("get file size:",os.path.getsize(__file__))

print("check path exists:",os.path.exists(os.path.abspath(__file__)))
print("check whether if file:",os.path.isfile(os.path.abspath(__file__)))
print("check whether if link:",os.path.islink(os.path.abspath(__file__)))
print("check whether if mount:",os.path.ismount(os.path.abspath(__file__)))


#print("create directory:",os.mkdir('testdir'))
#print("unlink file:",os.unlink('aaa.txt'))
#print("remove directory:",os.rmdir('testdir'))
#print("rename directoryL",os.rename('testdir','demodir'))