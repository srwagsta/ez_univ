from django.views.generic import (ListView,
                                  TemplateView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Instructor, Section, Course, Semester, Student
from .forms import InstructorForm
from .utils import CourseActionMixin


class Courseinfo(TemplateView):
    template_name = 'courseinfo/courseinfo_base.html'


class InstructorList(ListView):
    model = Instructor
    context_object_name = 'instructor_list'


class InstructorDetailView(DetailView):
    model = Instructor

    def get_context_data(self, **kwargs):
        kwargs['sections'] = self.get_object().sections.all()
        return super(InstructorDetailView, self).get_context_data(**kwargs)

#TODO add the loginRequiredMixin to the CRUD views
class InstructorCreate(CourseActionMixin, CreateView):
    model = Instructor
    success_msg = "Instructor Created!"
    form_class = InstructorForm
    template_name_suffix = '_create'


class InstructorUpdate(CourseActionMixin, UpdateView):
    model = Instructor
    success_msg = "Instructor Updated!"
    form_class = InstructorForm
    template_name_suffix = '_update'


class SectionList(ListView):
    model = Section
    context_object_name = 'section_list'


class SectionDetailView(DetailView):
    model = Section

    def get_context_data(self, **kwargs):
        kwargs['students'] = self.get_object().students.all()
        kwargs['instructors'] = self.get_object().instructors.all()
        return super(SectionDetailView, self).get_context_data(**kwargs)


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        kwargs['sections'] = self.get_object().sections.all()
        return super(CourseDetailView, self).get_context_data(**kwargs)


class SemesterList(ListView):
    model = Semester
    context_object_name = 'semester_list'


class SemesterDetailView(DetailView):
    model = Semester

    def get_context_data(self, **kwargs):
        kwargs['sections'] = self.get_object().sections.all()
        return super(SemesterDetailView, self).get_context_data(**kwargs)


class StudentList(ListView):
    model = Student
    context_object_name = 'student_list'


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        kwargs['sections'] = self.get_object().sections.all()
        return super(StudentDetailView, self).get_context_data(**kwargs)
