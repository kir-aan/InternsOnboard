from django import forms
from InternsOnboardMain.models import internshipPost
from crispy_forms.helper import FormHelper

class InternshipsUploadForm(forms.ModelForm):

    class Meta:
        model = internshipPost
        fields = ['company_name','discription']

    def __init__(self, *args, **kwargs):
        super(InternshipsUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
