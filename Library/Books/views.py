from django.shortcuts import render
from django.contrib.auth.models import User

from models import Book, Tag


def book_search(request):
    return render(request, 'Books/recommend.html')


def book_info(request):
    return render(request, 'Books/book.html')

