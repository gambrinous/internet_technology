import os

# this is a template for a population script..

def populate():

    courses = ['Internet Technology', 'Big Data', 'Professional Skills and Issues']

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
        u = add_university(name=universities[i][0], domain=universities[i][1], address=universities[i][2], city=universities[i][3], country=universities[i][4], postcode=universities[i][5])
        for j in range(len(students)):
            s = add_student(name=students[j][0], surname=students[j][1], email=students[j][0]+'.'+students[j][1]+'@'+universities[i][1], password='1234', university=u)
        for k in courses:
            c = add_course(titlte = k)



def add_university(name, domain, address, city, country, postcode):
    u = University.objects.get_or_create(name=name, domain=domain, address=address, city=city, country=country, postcode=postcode)[0]
    return u

def add_student(name, surname, email, password, university):
    s = Student.objects.get_or_create(firstName=name, lastName=surname, email=email, password=password, id_uni=university)[0]
    return s

def add_course(title):
    c = Course.objects.get_or_create(title=title)[0]
    return c


# Start execution here!
if __name__ == '__main__':
    print "Starting Rate population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyCourse.settings')
    from rate.models import University, Student, Course
    populate()