from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Book, Genre, BookIssued


def index(request):
    return render(request, 'index.html')


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.order_by('title')
    template_name = 'book_list.html'
    paginate_by = 6


class BookDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects
        post = get_object_or_404(queryset, slug=slug)
        cover = Book.cover
        genre = Book.genre
        borrowed = Book.borrowed

        return render(
            request,
            'book_detail.html',
            context={
                'book': post,
                'cover': cover,
                'genre': genre,
                'borrowed': borrowed
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects
        post = get_object_or_404(queryset, slug=slug)
        cover = Book.cover
        genre = Book.genre
        borrowed = Book.borrowed

        return render(
            request,
            'book_detail.html',
            context={
                'book': post,
                'cover': cover,
                'genre': genre,
                'borrowed': borrowed
            },
        )

    def borrow_book(request, book_isbn):
        book = get_object_or_404(Book, isbn=book_isbn)
        book.borrowed = not book.borrowed
        book.save()
        return render(
            request,
            'book_detail.html',
            context={
                'book': book,
            },
        )
