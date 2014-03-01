from django.contrib import admin
from rate.models import University, Student, Course, Rating, UniCourse

admin.site.register(University)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Rating)
admin.site.register(UniCourse)