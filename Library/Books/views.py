from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from models import Book, Tag


def book_recommendation(request):
    context = {

    }
    return render(request, 'Books/recommend.html', context=context)


def book_search(request):
    context = {

    }
    return render(request, 'Books/search.html', context=context)


def book_info(request, isbn='9787550217454'):
    try:
        book = Book.objects.get(isbn=isbn)
    except Book.DoesNotExist:
        return redirect('recommedation')
    context = {
        'book': book
    }
    return render(request, 'Books/book.html', context=context)

