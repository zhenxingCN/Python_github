#-*- coding:UTF-8 -*-
from __future__ import print_function
import argparse
import pymysql as db
import sys

def _argparse():
    parser = argparse.ArgumentParser(description='health checker for MySQL database')
    parser.add_argument('--host', action='store', dest='host', required=True, help='connect to host')
    parser.add_argument('-u', '--user', action='store', dest='user', required=True, help='user for login')
    parser.add_argument('-P', '--password', action='store', dest='password',required=True, help='password to use when connecting to server')
    parser.add_argument('-p --port', action='store', dest='port', default=3306, type=int, help='port number to use for connection or 3306 for default')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()


def get_conn(**kwargs):
    print(kwargs)





def main():
    if sys.argv[1] == 'report':
        with open('/tmp/.mysql_qps') as orgi_file,open('/tmp/avg_mysql_qps','w') as report_file:
            for line in orgi_file:
                print()
        with open('/etc/passwd') as source_file, open('/tmp/passwd', 'w') as target_file:
            for line in source_file:
                print(line.split(':')[0], line.split(':')[-1], file=target_file)







    try:
        parser = _argparse()
        conn = get_conn(host=parser.host, user=parser.user, password=parser.password, port=parser.port)
        with conn as cur:
            cur.execute("show global status like "questions)


if __name__ == '__main__':
    main()