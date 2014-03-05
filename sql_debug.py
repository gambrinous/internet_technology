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

    print 'rate course'
    for row in c.execute('SELECT * FROM rate_course'):# WHERE id=68'):
        print row

    print 'rate unic uni'
    for row in c.execute('select * from rate_uniCourse_university'):
        print row

    print 'rate_unicourse_course'
    for row in c.execute('select * from rate_uniCourse_course'):
        print row

    print 'rate_unicourse'
    for row in c.execute('select * from rate_uniCourse'):
        print row


    print 'rate rating course'
    for row in c.execute('SELECT * FROM rate_rating_course'):#' WHERE id=68'):
        print row

    print 'rate rating student'
    for row in c.execute('SELECT * FROM rate_rating_student'):#' WHERE id=68'):
        print row

    print 'rate rating'
    for row in c.execute('SELECT * FROM rate_rating'):#' WHERE id=69'):
        print row

    '''
    print 'rate uni'
    for row in c.execute('SELECT * FROM rate_university'):
        print row

    for row in c.execute('SELECT * FROM SQLite_master'):
        print row

    print 'rate student'
    for row in c.execute('SELECT * FROM rate_student where id_uni_id=4'): # WHERE id=68'):
        print row

    for row in c.execute('select * from rate_rating_course where course_id=1'):#' where student_id=68'):
        print row'''

'''
    print 'rate course'
    for row in c.execute('SELECT * FROM rate_course'):# WHERE id=68'):
        print row

    print 'rate unic uni'
    for row in c.execute('select * from rate_uniCourse_university'):
        print row

    print 'rate_unicourse_course'
    for row in c.execute('select * from rate_uniCourse_course'):
        print row

    print 'rate_unicourse'
    for row in c.execute('select * from rate_uniCourse'):
        print row


    print 'rate rating course'
    for row in c.execute('SELECT * FROM rate_rating_course'):#' WHERE id=68'):
        print row

    print 'rate rating student'
    for row in c.execute('SELECT * FROM rate_rating_student'):#' WHERE id=68'):
        print row

    print 'rate rating'
    for row in c.execute('SELECT * FROM rate_rating'):#' WHERE id=69'):
        print row
'''

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyCourse.settings')
    from rate.models import University, Student, Course, UniCourse, Rating
    run()