# coding=utf-8

from django.shortcuts import render, redirect
from django.db.models import Q

from models import Book, Tag


def book_recommendation(request):
    context = {

    }
    return render(request, 'Books/recommend.html', context=context)


def book_search(request):
    search_text = request.GET.get('q', default=u'算法')
    book_list = Book.objects.filter(Q(title__icontains=search_text) | Q(summary__icontains=search_text))
    context = {
        'q': search_text,
        'count': len(book_list),
        'books': book_list[:50],
    }
    print book_list
    return render(request, 'Books/search.html', context=context)


def book_isbn_info(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
        print book
    except Book.DoesNotExist:
        return redirect('recommendation')
    context = {
        'book': book
    }
    return render(request, 'Books/book.html', context=context)


def book_id_info(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return redirect('recommendation')
    context = {
        'book': book
    }
    return render(request, 'Books/book.html', context=context)


def tag_info(request, tag):
    book_list = Book.objects.filter(tags=tag)  # Todo
    context = {
        'books': book_list,
    }
    return render(request, 'Books/tag_info.html', context=context)

