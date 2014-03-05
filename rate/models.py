from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class University(models.Model):
    name = models.CharField(max_length=256)
    domain = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    postcode = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=32)
    id_uni = models.ForeignKey(University)

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName


class Course(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class UniCourse(models.Model):
    university = models.ManyToManyField(University)
    course = models.ManyToManyField(Course)
    school = models.CharField(max_length=128)
    year = models.IntegerField(default=2000)
    professor = models.CharField(max_length=128)
    total_rating = models.IntegerField(default=0)
    times_rated = models.IntegerField(default=0)
    stored_average_rating = models.FloatField(default=0.0)

    def _get_average_rating(self):
        if self.times_rated == 0:
            return 0.0
        else:
            return round(float(self.total_rating)/float(self.times_rated),1)

    average_rating2 = property(_get_average_rating)

    def __unicode__(self):
        return self.university + ' ' + self.course


class Rating(models.Model):
    student = models.ManyToManyField(Student)
    course = models.ManyToManyField(Course)
    rate = models.FloatField(default=0)
    comment = models.CharField(max_length=1024)
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return unicode(self.student) + ' ' + unicode(self.course)
