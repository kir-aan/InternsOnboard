from django import forms
from .models import studentInternship
from crispy_forms.helper import FormHelper


class studentInternshipForm(forms.ModelForm):

    class Meta:
        model = studentInternship
        fields = ['studentName','applied']

    def __init__(self, *args, **kwargs):
        super(studentInternshipForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)