from django.db import models
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


class Course(models.Model):
    title = models.CharField(max_length=128)
    university = models.ForeignKey(University)
    year = models.IntegerField(default=2000)
    level = models.IntegerField(default=1)
    professor = models.CharField(max_length=128)
    rating = models.FloatField(default=0)

    def __unicode__(self):
        return self.title


class Rate(models.Model):
    student = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    rate = models.FloatField(default=0)
    comment = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.student) + ' / ' + unicode(self.course)
