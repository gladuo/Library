from django.shortcuts import render
from django.contrib.auth.models import User
from forms import UserForm, UserProfileForm

from models import UserProfile


def index(request):
    user = User
    context = {
        user: user
    }
    return render(request, 'Library/index.html', context=context)


def user_profile(request):
    return render(request, 'Users/user_profile.html')


def user_settings(request):
    user_form = UserForm()
    user_profile_form = UserProfileForm()
    context = {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
    }
    return render(request, 'Users/user_settings.html', context=context)
