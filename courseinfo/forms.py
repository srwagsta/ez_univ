from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from courseinfo.models import (Instructor, Section, Course,
                               Semester, Student)


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(InstructorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit Instructor'))

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_name',
                  'semester',
                  'course',
                  'instructors',
                  'students']

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.fields['students'].required = False
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit Section'))


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_number',
                  'course_name']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit Course'))


class SemesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = ['calendar_period', 'year']

    def __init__(self, *args, **kwargs):
        super(SemesterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit Semester'))


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name',
                  'last_name',
                  'nick_name']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit Student'))

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_nick_name(self):
        return self.cleaned_data['nick_name'].strip()

