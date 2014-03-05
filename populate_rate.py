import os

# this is a template for a population script..

def populate():

    #For each university this is the tables to pair with the courses

    uni_course = [['Internet Technology','School of Computing Science', 2014, 'Dr Azzopardi', 4.6],  #glasgow
                  ['Economics 101','School of Economics', 2010, 'Dr Aniston', 3.5],
                  ['History 1','School of History', 2011, 'Dr Jolie', 4.3],                         #london
                  ['Geology 101','School of Geology', 2011, 'Dr Johanson', 3.0],
                  ['Project Management','School of Computing Science', 2010, 'Dr Knightley', 3.7],  #leeds
                  ['Mathematics 1','School of Mathematics', 2012, 'Dr Stone', 3.4],
                  ['Professional Skills and Issues','School of Computing Science', 2008, 'Dr Cruz', 4.4], #sheffield
                  ['Internet Technology','School of Computing Science', 2008, 'Dr App', 4.8],
                  ['Mathematics 1','School of Mathematics', 2008, 'Dr Swift', 3.3],
                  ['Project Management','School of Computing Science', 2010, 'Dr Andrew', 2.3]]

    #stu_id, course_id, rate, comment, date
    rateit = [[11, 5, 4, 'What an interesting course!', '2014-02-11'], [11, 3, 2, 'Not very good', '2013-01-23'],
             [8, 6, 4, 'it is okay', '2011-03-12'], [12, 1, 2, 'not good at all', '2008-11-10'],
             [12, 3, 3, 'not very objective', '2008-12-05'], [2, 2, 4, 'very fluent', '2010-04-02']]

    #all of the courses
    courses = ['Internet Technology', 'Economics 101', 'Professional Skills and Issues', 'Project Management',
               'Mathematics 1', 'History 1', 'Geology 101']

    #the students of all univeristies
    students = [['Maggie', 'McGeek'], ['Charlie', 'Cheaterson'], ['Leif', 'Azzopardi'], ['Mark', 'Zuckerberg'],
        ['Emily', 'Robinson'], ['Sarah', 'Taylor'], ['Emma', 'Jones'], ['Jessica', 'White'],
        ['Daniel', 'Wilson'], ['Courtney', 'Smith'], ['Matthew', 'Thompson'], ['Ryan', 'Walker'],
        ['Jacob', 'King'], ['Olivia', 'Lee'], ['Peter', 'Nguyen']]

    universities = [
        ['University of Glasgow', 'student.gla.ac.uk', 'University Avenue', 'Glasgow', 'United Kingdom', 'G12 8QQ'],
        ['University of London', 'student.lon.ac.uk', 'Malet Street', 'London', 'United Kingdom', 'WC1E 7HU'],
        ['University of Leeds', 'student.leeds.ac.uk', 'Clarendon Place', 'Leeds', 'United Kingdom', 'LS2 9JT'],
        ['University of Sheffield', 'student.sheffield.ac.uk', 'Western Bank', 'Sheffield', 'United Kingdom', 'S10 2TN']
    ]

    #import Universities
    for i in range(len(universities)):
        u = add_university(universities[i][0], universities[i][1], universities[i][2], universities[i][3], universities[i][4], universities[i][5])

    #import Courses
    for k in courses:
        c = add_course(k)

    #import students in each University
    #GLASGOW
    for j in range(0, 4, 1):
        u = University.objects.get(name="University of Glasgow")
        s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[0][1],
                        '1234')
    #LONDON
    for j in range(4, 9, 1):
        u = University.objects.get(name="University of London")
        s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[1][1],
                        '1234', u)
    #LEEDS
    for j in range(9, 11, 1):
        u = University.objects.get(name="University of Leeds")
        s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[2][1],
                        '1234', u)
    #SHEFFIELD
    for j in range(11, 15, 1):
        u = University.objects.get(name="University of Sheffield")
        s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[3][1],
                        '1234', u)

    #Cources in each university
    for j in range(len(uni_course)):
        u = University.objects.get(name="University of Glasgow")
        c = Course.objects.get(title=uni_course[j][0])
        add_unicourse(u, c, uni_course[j][1], uni_course[j][2], uni_course[j][3], uni_course[j][4])


    #ratings per uni
    for i in range(len(rateit)):
        st = User.objects.get(id=rateit[i][0])
        c = Course.objects.get(id=rateit[i][1])
        add_rate(st, c, rateit[i][2], rateit[i][3], rateit[i][4])


def add_university(name, domain, address, city, country, postcode):
    u = University.objects.get_or_create(name=name, domain=domain, address=address, city=city, country=country, postcode=postcode)[0]
    return u

def add_student(name, surname, email, password, university):
    s = User.objects.get_or_create(first_name=name, last_name=surname, email=email)[0]
    s.set_password(password)
    s.save()
    return s

def add_course(title):
    c = Course.objects.get_or_create(title=title)[0]
    return c

def add_unicourse(uni, course, school, year, professor, rating):
    uC = UniCourse.objects.get_or_create(school=school, year=year, professor=professor, rating=rating)[0]
    uC.university.add(uni)
    uC.course.add(course)
    return uC

def add_rate(student, course, rate, comment, date):
    r = Rate.objects.get_or_create(rate=rate, comment=comment, date=date)[0]
    r.course.add(course)
    r.student.add(student)
    return r

# Start execution here!
if __name__ == '__main__':
    print "Starting Rate population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyCourse.settings')
    from rate.models import University, Course, UniCourse, Rate
    from django.contrib.auth.models import User
    populate()
    print "Well Done!"