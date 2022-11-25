from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Book, Genre


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
            {
                'book': post,
                'cover': cover,
                'genre': genre,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects
        post = get_object_or_404(queryset, slug=slug)
        cover = Book.cover
        genre = Book.genre

        return render(
            request,
            'book_detail.html',
            {
                'book': post,
                'cover': cover,
                'genre': genre,
            },
        )
