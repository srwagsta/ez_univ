from django.http.response import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import Instructor, Section, Course, Semester, Student


def courseinfo_home_view(request):
    template = loader.get_template('courseinfo/courseinfo_base.html')
    return HttpResponse(template.render())


class InstructorList(ListView):
    model = Instructor
    context_object_name = 'instructor_list'


class SectionList(ListView):
    model = Section
    context_object_name = 'section_list'


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'


class SemesterList(ListView):
    model = Semester
    context_object_name = 'semester_list'


class StudentList(ListView):
    model = Student
    context_object_name = 'student_list'
