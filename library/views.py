from django.shortcuts import render
from django.views import generic
from .models import Book, Genre


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.order_by('title')
    template_name = 'index.html'
    paginate_by = 6
