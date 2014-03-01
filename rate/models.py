from django.db import models


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
        return self.firstName


class Course(models.Model):
    title  = models.CharField(max_length=128)
    year = models.IntegerField(default=2000)
    professor = models.CharField(max_length=128)
    rating = models.FloatField(default=0)

    universities = models.ManyToManyField(University)

    def __unicode__(self):
        return self.title


class Rate(models.Model):
    student = models.ManyToManyField(Student)
    course = models.ManyToManyField(Course)
    rate = models.IntegerField(default=0)
    #timestamp

    def __unicode__(self):
        return self.rate