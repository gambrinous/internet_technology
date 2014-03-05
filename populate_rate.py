import os

# this is a template for a population script..

def populate():

    #For each university this is the tables to pair with the courses
    #glasgow
    uni_course1 = [['Internet Technology','School of Computing Science', 2014, 'Dr Azzopardi', 92, 20],# 4.6],
                  ['Economics 101','School of Economics', 2010, 'Dr Aniston', 70, 20]]#, 3.5]]

    #london
    uni_course2 = [['History 1','School of History', 2011, 'Dr Jolie', 86, 20],# 4.3],
                  ['Geology 101','School of Geology', 2011, 'Dr Johanson', 60, 20]]#, 3.0]]

    #leeds
    uni_course3 = [['Project Management','School of Computing Science', 2010, 'Dr Knightley', 74, 20],# 3.7],
                  ['Mathematics 1','School of Mathematics', 2012, 'Dr Stone', 68, 20]]#, 3.4]]

    #sheffield
    uni_course4 = [['Professional Skills and Issues','School of Computing Science', 2008, 'Dr Cruz', 88, 20],# 4.4],
                  ['Internet Technology','School of Computing Science', 2008, 'Dr App', 96, 20],# 4.8],
                  ['Mathematics 1','School of Mathematics', 2008, 'Dr Swift', 66, 20],# 3.3],
                  ['Project Management','School of Computing Science', 2010, 'Dr Andrew', 46, 20]]#, 2.3]]

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
                        '1234', u)
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
    #GLASGOW
    for j in range(0, 2, 1):
        u = University.objects.get(name="University of Glasgow")
        c = Course.objects.get(title=uni_course1[j][0])
        add_unicourse(u, c, uni_course1[j][1], uni_course1[j][2], uni_course1[j][3], uni_course1[j][4], uni_course1[j][5])#, uni_course1[j][6])

    #LONDON
    for j in range(0, 2, 1):
        u = University.objects.get(name="University of London")
        c = Course.objects.get(title=uni_course2[j][0])
        add_unicourse(u, c, uni_course2[j][1], uni_course2[j][2], uni_course2[j][3], uni_course2[j][4], uni_course2[j][5])#, uni_course2[j][6])

    #LEEDS
    for j in range(0, 2, 1):
        u = University.objects.get(name="University of Leeds")
        c = Course.objects.get(title=uni_course3[j][0])
        add_unicourse(u, c, uni_course3[j][1], uni_course3[j][2], uni_course3[j][3], uni_course3[j][4], uni_course3[j][5])#, uni_course3[j][6])

    #SHEFFIELD
    for j in range(0, 3, 1):
        u = University.objects.get(name="University of Sheffield")
        c = Course.objects.get(title=uni_course4[j][0])
        add_unicourse(u, c, uni_course4[j][1], uni_course4[j][2], uni_course4[j][3], uni_course4[j][4], uni_course4[j][5])#, uni_course4[j][6])
        #r = add_rate(s, c, rateit[0], rateit[1], rateit[2])

    #ratings per uni
    #LEEDS
    for i in range(len(rateit)):
        st = Student.objects.get(id=rateit[i][0])
        c = Course.objects.get(id=rateit[i][1])
        add_rate(st, c, rateit[i][2], rateit[i][3], rateit[i][4])


def add_university(name, domain, address, city, country, postcode):
    u = University.objects.get_or_create(name=name, domain=domain, address=address, city=city, country=country, postcode=postcode)[0]
    return u

def add_student(name, surname, email, password, university):
    s = Student.objects.get_or_create(firstName=name, lastName=surname, email=email, password=password, id_uni=university)[0]
    return s

def add_course(title):
    c = Course.objects.get_or_create(title=title)[0]
    return c

def add_unicourse(uni, course, school, year, professor, total_rating, times_rated):#, rating):
    uC = UniCourse.objects.get_or_create(school=school, year=year, professor=professor, total_rating=total_rating, times_rated=times_rated) [0]#, average_rating=rating)[0]
    uC.university.add(uni)
    uC.stored_average_rating = (round(float(total_rating)/float(times_rated),2))
    print uC.stored_average_rating
    uC.course.add(course)
    uC.save()
    return uC

def add_rate(student, course, rate, comment, date):
    r = Rating.objects.get_or_create(rate=rate, comment=comment, date=date)[0]
    '''uc._get_total_rating(course)
    uc.total_rating += rate
    uc.times_rated += 1
    uc.save()'''
    r.course.add(course)
    r.student.add(student)
    return r

# Start execution here!
if __name__ == '__main__':
    print "Starting Rate population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyCourse.settings')
    from rate.models import University, Student, Course, UniCourse, Rating
    populate()
    print "Well Done!"#