from django.contrib import admin
from .models import (CalendarPeriod, Semester, Student,
                     Instructor, Section, Course)

admin.site.register(CalendarPeriod)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Section)
admin.site.register(Course)

