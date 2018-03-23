from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from courseinfo.models import (Instructor,
                               Section)


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name']

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
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
