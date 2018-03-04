from django.views.generic import ListView, TemplateView, DetailView
from .models import Instructor, Section, Course, Semester, Student


class Courseinfo(TemplateView):
    template_name = 'courseinfo/courseinfo_base.html'


class InstructorList(ListView):
    model = Instructor
    context_object_name = 'instructor_list'


class InstructorDetailView(DetailView):
    model = Instructor

    def get_context_data(self, **kwargs):
        context = super(InstructorDetailView, self).get_context_data(**kwargs)
        context['section_list'] = Section.objects.all()
        return context



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
