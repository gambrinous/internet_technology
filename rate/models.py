from django.db import models

class User(models.Model):
    id_user = models.PrimaryKey(User)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=32)
    id_uni = models.ForeignKey(University)

    def __unicode__(self):
        return self.id_user


class University(models.Model):
    id_uni = models.PrimaryKey(University)
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
    timestamp = models.DateField(datetime.date)
    ind_rate = models.FloatField(default=0)

    def __unicode__(self):
        return self.id_user