from django.shortcuts import render

from models import Book, Category


def index(request):
    context = {'text': 'hello world'}
    return render(request, 'Books/index.html', context=context)
