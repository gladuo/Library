from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from models import UserProfile, User
from forms import UserFormEdit, UserProfileForm

from models import UserProfile
from Books.models import Book


def index(request):
    if request.user.is_authenticated():
        return redirect('recommendation')
    else:
        context = {
            'user': request.user
        }
        return render(request, 'Library/index.html', context=context)


@login_required()
def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    book_list = [Book.objects.get(id=b) for b in profile.history]
    print book_list[:8]
    context = {
        'user_profile': profile,
        'book_list': book_list[:8],
        'tag_list': [t for t, n in sorted(profile.favorite_tag.items(), key=lambda d: d[1], reverse=True)][:16]
    }
    return render(request, 'Users/user_profile.html', context=context)


@login_required()
def user_edit(request):
    if request.method == 'POST':
        user_form = UserFormEdit(data=request.POST, instance=request.user)
        if user_form.is_valid:
            new_info = user_form.save()
        else:
            print user_form.errors
    else:
        user_form = UserFormEdit(instance=request.user)
    context = {
        'user_form': user_form,
    }
    return render(request, 'Users/user_edit.html', context=context)


@login_required()
def user_settings(request):

    old_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_profile_form = UserProfileForm(data=request.POST, instance=old_profile)
        if user_profile_form.is_valid:
            new_profile = user_profile_form.save()
        else:
            print user_profile_form.errors
    else:
        user_profile_form = UserProfileForm(instance=old_profile)
    context = {
        'user_profile_form': user_profile_form,
    }
    return render(request, 'Users/user_settings.html', context=context)
