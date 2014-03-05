from django.contrib import admin
from rate.models import University, Student, Course, Rate

admin.site.register(University)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Rate)