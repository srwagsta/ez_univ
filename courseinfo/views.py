from django.views.generic import (ListView, TemplateView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Instructor, Section, Course, Semester, Student
from .forms import (InstructorForm, SectionForm, CourseForm,
                    SemesterForm, StudentForm)
from .utils import CourseActionMixin, ValidateUnconnectedSectionsDeleteMixin

GENERIC_CRISPY_FORM_PATH = 'courseinfo/generic_crispy_form.html'
GENERIC_DELETE_TEMPLATE_PATH = 'courseinfo/generic_confirm_delete.html'
GENERIC_FAILED_DELETE_TEMPLATE_PATH = 'courseinfo/generic_failed_delete.html'


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


class InstructorCreate(CourseActionMixin, CreateView):
    model = Instructor
    success_msg = "Instructor Created!"
    form_class = InstructorForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(InstructorCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Instructor'
        return context


class InstructorUpdate(CourseActionMixin, UpdateView):
    model = Instructor
    success_msg = "Instructor Updated!"
    form_class = InstructorForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(InstructorUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Instructor'
        return context


class InstructorDelete(ValidateUnconnectedSectionsDeleteMixin, DeleteView):
    model = Instructor
    success_url = reverse_lazy('courseinfo:instructor_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH
    failed_delete_template = GENERIC_FAILED_DELETE_TEMPLATE_PATH


class SectionList(ListView):
    model = Section
    context_object_name = 'section_list'


class SectionDetailView(DetailView):
    model = Section

    def get_context_data(self, **kwargs):
        kwargs['students'] = self.get_object().students.all()
        kwargs['instructors'] = self.get_object().instructors.all()
        return super(SectionDetailView, self).get_context_data(**kwargs)


class SectionCreate(CourseActionMixin, CreateView):
    model = Section
    success_msg = "Section Created!"
    form_class = SectionForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(SectionCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Section'
        return context


class SectionUpdate(CourseActionMixin, UpdateView):
    model = Section
    success_msg = "Section Updated!"
    form_class = SectionForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(SectionUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Section'
        return context


class SectionDelete(DeleteView):
    model = Section
    success_url = reverse_lazy('courseinfo:section_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH

    def get_context_data(self, **kwargs):
        context = super(SectionDelete, self).get_context_data(**kwargs)
        context['page_title'] = 'Delete Instructor'
        return context


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        kwargs['sections'] = self.get_object().sections.all()
        return super(CourseDetailView, self).get_context_data(**kwargs)


class CourseCreate(CourseActionMixin, CreateView):
    model = Course
    success_msg = "Course Created!"
    form_class = CourseForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(CourseCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Course'
        return context


class CourseUpdate(CourseActionMixin, UpdateView):
    model = Course
    success_msg = "Course Updated!"
    form_class = CourseForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(CourseUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Course'
        return context


class CourseDelete(ValidateUnconnectedSectionsDeleteMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courseinfo:course_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH
    failed_delete_template = GENERIC_FAILED_DELETE_TEMPLATE_PATH


class SemesterList(ListView):
    model = Semester
    context_object_name = 'semester_list'


class SemesterDetailView(DetailView):
    model = Semester

    def get_context_data(self, **kwargs):
        kwargs['sections'] = self.get_object().sections.all()
        return super(SemesterDetailView, self).get_context_data(**kwargs)


class SemesterCreate(CourseActionMixin, CreateView):
    model = Semester
    success_msg = "Semester Created!"
    form_class = SemesterForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(SemesterCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Semester'
        return context


class SemesterUpdate(CourseActionMixin, UpdateView):
    model = Semester
    success_msg = "Semester Updated!"
    form_class = SemesterForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(SemesterUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Semester'
        return context


class SemesterDelete(ValidateUnconnectedSectionsDeleteMixin, DeleteView):
    model = Semester
    success_url = reverse_lazy('courseinfo:semester_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH
    failed_delete_template = GENERIC_FAILED_DELETE_TEMPLATE_PATH


class StudentList(ListView):
    model = Student
    context_object_name = 'student_list'


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        kwargs['sections'] = self.get_object().sections.all()
        return super(StudentDetailView, self).get_context_data(**kwargs)


class StudentCreate(CourseActionMixin, CreateView):
    model = Student
    success_msg = "Student Created!"
    form_class = StudentForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(StudentCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Student'
        return context


class StudentUpdate(CourseActionMixin, UpdateView):
    model = Student
    success_msg = "Student Updated!"
    form_class = StudentForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(StudentUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Student'
        return context


class StudentDelete(ValidateUnconnectedSectionsDeleteMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('courseinfo:student_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH
    failed_delete_template = GENERIC_FAILED_DELETE_TEMPLATE_PATH
