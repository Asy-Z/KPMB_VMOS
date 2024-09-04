from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    USERTYPE = [
        ('Student', 'Student'),
        ('Lecturer', 'Lecturer'),
        ('Administrator', 'Administrator')
    ]

    UserId = forms.CharField(max_length=12)
    UserLevel = forms.ChoiceField(choices=USERTYPE)
    PhoneNo = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'UserId','UserLevel', 'PhoneNo']






