from __future__ import print_function
import pymysql as db

from student import  Student


def get_conn(**kwargs):
    return db.connect(host=kwargs.get('host', 'localhost'),
        user=kwargs.get('user'),
        passwd=kwargs.get('passwd'),
        port=kwargs.get('port', 3306),
        db=kwargs.get('db'))


def get_top_student(students):
    top_student = students[0]

    for student in students[1:]:
        if top_student.get_sum() < student.get_sum():
            top_student = student

    return top_student


def display_students(students):
    for student in students:
        print(student)


def main():
    conn = get_conn(host='172.25.21.11', user='yzx', passwd='yzx', port=3306, db='yzx')
    try:
        students = []
        with conn as cur:
            cur.execute('select name, chinese, math, english from student')
            rows = cur.fetchall()
            for row in rows:
                obj = Student(row[0], row[1], row[2], row[3])
                students.append(obj)

        display_students(students)
        print(get_top_student(students))
    finally:
        if conn:
            conn.close()



if __name__ == '__main__':
    main()