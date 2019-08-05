from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

USER_TYPE_CHOICES = (
    ('s', 'Student'),
    ('ic', 'Internship-coordinator'),
    ('h','HOD')
)

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    usertype = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=USER_TYPE_CHOICES)
    class Meta:
        model = User
        fields = ('username','password1', 'password2','email','usertype')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username']
