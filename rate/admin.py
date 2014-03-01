__author__ = 'Marios'
from django.contrib import admin
from rate.models import University, Student

admin.site.register(University)
admin.site.register(Student)