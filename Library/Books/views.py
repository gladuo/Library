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
        'books': book_list[:10],
    }
    print book_list
    return render(request, 'Books/search.html', context=context)


def book_info(request, id=1, isbn=9787550217454):
    if id:
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return redirect('recommendation')
    else:
        try:
            book = Book.objects.get(isbn=isbn)
        except Book.DoesNotExist:
            return redirect('recommendation')
    print book.tags.all()
    context = {
        'book': book
    }
    return render(request, 'Books/book.html', context=context)

