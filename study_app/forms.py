from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Assignment


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'tutor', 'tutee', 'content']

# class NewUser(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
