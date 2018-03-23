from django.forms import ModelForm
from courseinfo.models import (Instructor)


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name']

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()
