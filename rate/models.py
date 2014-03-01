from django.db import models


class University(models.Model):
    id_uni = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
    domain = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    postcode = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    id_student = models.IntegerField(unique=True)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=32)
    id_uni = models.ForeignKey(University)

    def __unicode__(self):
        return self.id_student


class Rate(models.Model):
    id_student = models.ForeignKey(Student)
    id_uni = models.ForeignKey(University)
    #id_rate = (id_student + id_uni).IntegerField(unique=True)
    #timestamp = models.DateField
    ind_rate = models.FloatField(default=0)

    def __unicode__(self):
        return self.id_rate


class Course(models.Model):
    id_course = models.IntegerField(unique=True)
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Uni_Course(models.Model):
    id_uni = models.ForeignKey(University)
    id_course = models.ForeignKey(Course)
    year = models.IntegerField(default=0)
    prof_name = models.CharField(max_length=128)
    ave_rate = models.FloatField(default=0)

    def __unicode__(self):
        return self.id_uni