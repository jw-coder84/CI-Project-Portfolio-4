from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Book, Genre, BookIssued
from .forms import BookBorrow


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

        return render(
            request,
            'book_detail.html',
            context={
                'book': post,
                'cover': cover,
                'genre': genre,
                'checked_out': False,
                'borrow_form': BookBorrow(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects
        post = get_object_or_404(queryset, slug=slug)
        cover = Book.cover
        genre = Book.genre
        title = Book.title

        borrow_form = BookBorrow(data=request.POST)

        if borrow_form.is_valid():
            borrow_form.instance.borrower = request.user.username
            borrow_form.instance.book = post
            borrow = borrow_form.save(commit=False)
            borrow.post = post
            borrow.save()
        else:
            borrow_form = BookBorrow()

        return render(
            request,
            'book_detail.html',
            context={
                'book': post,
                'cover': cover,
                'genre': genre,
                'checked_out': True,
                'borrow_form': BookBorrow()
            },
        )
