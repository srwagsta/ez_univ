from django.contrib import admin
from .models import Semester, Student, Instructor, Section, Course

admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Section)
admin.site.register(Course)

