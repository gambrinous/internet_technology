import os

# this is a template for a population script..

def populate():

    uni_course = ['School of Computing Science', 2014, 'Dr Azzopardi', 4.3]

    rateit = [4.3, 'What an interesting course!', '2014-02-11']

    courses = ['Internet Technology', 'Big Data', 'Professional Skills and Issues', 'Project Management', 'Information Retrieval']

    students = [
        ['Maggie', 'McGeek'],
        ['Charlie', 'Cheaterson'],
        ['Leif', 'Azzopardi'],
        ['Mark', 'Zuckerberg'],
        ['Emily', 'Robinson'],
        ['Sarah', 'Taylor'],
        ['Emma', 'Jones'],
        ['Jessica', 'White'],
        ['Daniel', 'Wilson'],
        ['Courtney', 'Smith'],
        ['Matthew', 'Thompson'],
        ['Ryan', 'Walker'],
        ['Jacob', 'King'],
        ['Olivia', 'Lee'],
        ['Peter', 'Nguyen']
    ]

    universities = [
        ['University of Glasgow', 'student.gla.ac.uk', 'University Avenue', 'Glasgow', 'United Kingdom', 'G12 8QQ'],
        ['University of London', 'student.lon.ac.uk', 'Malet Street', 'London', 'United Kingdom', 'WC1E 7HU'],
        ['University of Leeds', 'student.leeds.ac.uk', 'Clarendon Place', 'Leeds', 'United Kingdom', 'LS2 9JT'],
        ['University of Sheffield', 'student.sheffield.ac.uk', 'Western Bank', 'Sheffield', 'United Kingdom', 'S10 2TN']
    ]

    for i in range(len(universities)):
        u = add_university(universities[i][0], universities[i][1], universities[i][2], universities[i][3], universities[i][4], universities[i][5])
        for k in courses:
            c = add_course(k)
            #uC = add_uniCourse(u, c, uni_course[0], uni_course[1], uni_course[2], uni_course[3])
            for j in range(len(students)):
                s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[i][1], '1234', u)
                #r = add_rate(s, c, rateit[0], rateit[1], rateit[2])


def add_university(name, domain, address, city, country, postcode):
    u = University.objects.get_or_create(name=name, domain=domain, address=address, city=city, country=country, postcode=postcode)[0]
    return u

def add_student(name, surname, email, password, university):
    s = Student.objects.get_or_create(firstName=name, lastName=surname, email=email, password=password, id_uni=university)[0]
    return s

def add_course(title):
    c = Course.objects.get_or_create(title=title)[0]
    return c

def add_uniCourse(uni, course, school, year, professor, rating):
    uC = UniCourse.objects.get_or_create(university=uni, course=course, school=school, year=year, professor=professor, rating=rating)[0]
    return uC

def add_rate(student, course, rate, comment, date):
    r = UniCourse.objects.get_or_create(student=student, course=course, rate=rate, comment=comment, date=date)[0]
    return r

# Start execution here!
if __name__ == '__main__':
    print "Starting Rate population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyCourse.settings')
    from rate.models import University, Student, Course, UniCourse
    populate()