from __future__ import print_function
import zipfile


zf = zipfile.ZipFile('access.zip')
with open('passwords.txt') as f:
    for line in f:
        try:
            zf.extractall(pwd=line.strip())
            print(line)
            break
        except Exception as err:
            pass