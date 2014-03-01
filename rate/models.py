from django.db import models

class User(models.Model):
    id_user = models.IntegerField(unique=True)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=32)
    id_uni = models.ForeignKey(University)

    def __unicode__(self):
        return self.id_user


class University(models.Model):
    id_uni = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
    domain = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    postcode = models.CharField(max_legth=10)

    def __unicode__(self):
        return self.id_uni

class Rate(models.Model):
    id_user = models.ForeignKey(User)
    id_uni = models.ForeignKey(University)
    id_rate = (id_user + id_uni).IntegerField(unique=True)
    timestamp = models.DateField
    ind_rate = models.FloatField(default=0)

    def __unicode__(self):
        return self.id_rate

class Course(models.Model):
    id_course = models.IntegerField(unique=True)
    title = models.CharField(max_length=50)
