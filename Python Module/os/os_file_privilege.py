from __future__ import print_function
import os
import sys

def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + 'does not exists')
    elif not os.access(filename,os.R_OK):
        os.chmod(filename,777)
    else:
        with open(filename) as f:
            print(f.read())
