import os
import sqlite3
conn = sqlite3.connect('rate.db')
'''
Creating table rate_university
Creating table rate_student
Creating table rate_course
Creating table rate_unicourse_university
Creating table rate_unicourse_course
Creating table rate_unicourse
Creating table rate_rating_course
Creating table rate_rating_student
Creating table rate_rating
'''

def run():

    c = conn.cursor()
    for row in c.execute('SELECT * FROM rate_university'):
        print row

    for row in c.execute('SELECT * FROM rate_student WHERE id=68'):
        print row

    for row in c.execute('SELECT * FROM rate_course WHERE id=68'):
        print row

    for row in c.execute('SELECT * FROM rate_rating_student WHERE id=68'):
        print row

    for row in c.execute('SELECT * FROM rate_rating_course WHERE id=68'):
        print row

    for row in c.execute('SELECT * FROM rate_rating WHERE id=69'):
        print row


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyCourse.settings')
    from rate.models import University, Student, Course, UniCourse, Rating
    run()