from __future__ import print_function
import fnmatch
import os
import glob


print([name for name in os.listdir('.') if fnmatch.fnmatch(name, '*.py')])

print(glob.glob('*.py'))

