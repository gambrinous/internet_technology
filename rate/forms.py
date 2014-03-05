from django import forms
from django.contrib.auth.models import User
from rate.models import Student

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('firstName', 'lastName')