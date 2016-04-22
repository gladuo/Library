# coding=utf-8

from django.shortcuts import render, redirect
from django.db.models import Q
from operator import attrgetter

from models import Book, Tag
from Users.models import UserProfile

import random


def book_recommendation(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    tag_list = sorted(user_profile.favorite_tag.items(), key=lambda d: d[1], reverse=True)[:5]
    print tag_list
    book_list = {}
    for tag, num in tag_list:
        book_list[tag] = random.sample(Book.objects.filter(Q(tags__name__icontains=tag))[:100], 4)
    print book_list
    context = {
        'book_list': book_list,
    }
    return render(request, 'Books/recommend.html', context=context)


def book_search(request):
    search_text = request.GET.get('q', default=u'算法')
    start = request.GET.get('start', default='0')
    try:
        start = int(start)
    except ValueError:
        start = 0
    if start < 0:
        start = 0
    book_list = Book.objects.filter(Q(title__icontains=search_text))
    print book_list
    context = {
        'q': search_text,
        'count': len(book_list),
        'books': sorted(book_list, key=attrgetter('pubdate'), reverse=True)[start:start+10],
    }
    print book_list
    return render(request, 'Books/search.html', context=context)


def book_isbn_info(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        if book.id not in user_profile.history:
            user_profile.history.append(book.id)
        if len(user_profile.history) > 8:
            user_profile.history.pop(0)
        for i in user_profile.history:
            b = Book.objects.get(id=int(i))
            for j in b.tags.all():
                if j.slug not in user_profile.favorite_tag:
                    user_profile.favorite_tag[j.slug] = 1
                else:
                    user_profile.favorite_tag[j.slug] += 1
        user_profile.save()
        tag_list = [t.name for t in book.tags.all()][:2]
        print tag_list
        book_list = {}
        for tag in tag_list:
            book_list[tag] = random.sample(Book.objects.filter(Q(tags__name__icontains=tag))[:100], 2)
        print book_list
    except Book.DoesNotExist:
        return redirect('recommendation')
    context = {
        'book': book,
        'book_list': book_list
    }
    return render(request, 'Books/book.html', context=context)


def book_id_info(request, id):
    try:
        book = Book.objects.get(id=id)
        user_profile, create = UserProfile.objects.get_or_create(user=request.user)
        if id not in user_profile.history:
            user_profile.history.append(id)
        if len(user_profile.history) > 8:
            user_profile.history.pop(0)
        for i in user_profile.history:
            b = Book.objects.get(id=int(i))
            for j in b.tags.all():
                if j.slug not in user_profile.favorite_tag:
                    user_profile.favorite_tag[j.slug] = 1
                else:
                    user_profile.favorite_tag[j.slug] += 1
        user_profile.save()

        tag_list = [t.name for t in book.tags.all()][:2]
        print tag_list
        book_list = {}
        for tag in tag_list:
            book_list[tag] = random.sample(Book.objects.filter(Q(tags__name__icontains=tag))[:100], 2)
        print book_list
    except Book.DoesNotExist:
        return redirect('recommendation')

    context = {
        'book': book,
        'book_list': book_list
    }
    return render(request, 'Books/book.html', context=context)


def tag_info(request, tag):
    book_list = Book.objects.filter(tags=tag)  # Todo
    context = {
        'books': book_list,
    }
    return render(request, 'Books/tag_info.html', context=context)


