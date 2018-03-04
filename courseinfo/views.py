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


class SectionDetailView(DetailView):
    model = Section
    # I don't think I need to add any extra context, the default will do fine


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'


class CourseDetailView(DetailView):
    model = Course
    # The default context should be fine


class SemesterList(ListView):
    model = Semester
    context_object_name = 'semester_list'


class SemesterDetailView(DetailView):
    model = Semester

    def get_context_data(self, **kwargs):
        context = super(InstructorDetailView, self).get_context_data(**kwargs)
        # context['section_list'] = Section.objects.all()
        # We can add some more context here
        return context


class StudentList(ListView):
    model = Student
    context_object_name = 'student_list'


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(InstructorDetailView, self).get_context_data(**kwargs)
        # context['section_list'] = Section.objects.all()
        # Add some context here
        return context
