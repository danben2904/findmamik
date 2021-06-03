from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Seeker

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class SeekerForm(ModelForm):
    class Meta:
        model = Seeker
        fields = "__all__"
        exclude = ["user", "loyalty_points"]

class MamikForm(forms.Form):
    min_age = forms.IntegerField(label='Min age')
    max_age = forms.IntegerField(label='Max age')
    min_salary = forms.IntegerField(label='Min salary')

class ChildForm(forms.Form):
    min_age = forms.IntegerField(label='Min age')
    max_age = forms.IntegerField(label='Max age')
