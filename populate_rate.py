import os

# this is a template for a population script..

def populate():

    firstnames = ['Maggie', 'Charlie', 'Leif', 'James', 'Emily', 'Sarah', 'Emma', 'Jessica', 'Daniel', 'Courtney', 'Matthew', 'Ryan', 'Jacob', 'Olivia', 'Peter']
    surnames = ['McGeek', 'Cheaterson', 'Azzopardi', 'Zuckerberg', 'Robinson', 'Taylor', 'Jones', 'White', 'Wilson', 'Smith', 'Thompson', 'Lee', 'Nguyen', 'Walker', 'King']
    email = ['maggie','charlie','leif','james','emily','sarah','emma','jessica','daniel','courtney','matthew','ryan','jacob','olivia', 'peter']
    passwords = '1234'
    domain = '@student.gla.ac.uk'

    courses = ['Internet Technology', 'Big Data', 'Professional Skills and Issues']

    universities = [['University of Glasgow', 'student.gla.ac.uk', 'University Avenue', 'Glasgow', 'United Kingdom', 'G12 8QQ'],
                    ['University of London', 'student.lon.ac.uk', 'Malet Street', 'London', 'United Kingdom', 'WC1E 7HU'],
                    ['University of Leeds', 'student.leeds.ac.uk', 'Clarendon Place', 'Leeds', 'United Kingdom', 'LS2 9JT'],
                    ['University of Sheffield', 'student.sheffield.ac.uk', 'Western Bank', 'Sheffield', 'United Kingdom', 'S10 2TN']
    ]

    for i in range(len(universities)):
        for j in range(len(universities[i])):
            add_university(name=universities[i][0], domain=universities[i][1], address=universities[i][2], city=universities[i][3], country=universities[i][4], postcode=universities[i][5])

def add_university(name, domain, address, city, country, postcode):
    u = University.objects.get_or_create(name=name, domain=domain, address=address, city=city, country=country, postcode=postcode)[0]
    return u

# Start execution here!
if __name__ == '__main__':
    print "Starting Rate population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyCourse.settings')
    from rate.models import University
    populate()