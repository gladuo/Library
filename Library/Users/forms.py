# coding=utf-8

from django import forms
from django.contrib.auth.models import User

from models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age', 'gender', 'university', 'description')
