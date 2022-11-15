from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Book, Genre


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.order_by('title')
    template_name = 'index.html'
    paginate_by = 6


class BookDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects
        post = get_object_or_404(queryset, slug=slug)
        cover = Book.cover

        return render(
            request,
            'book_detail.html',
            {
                'book': post,
                'cover': cover,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects
        post = get_object_or_404(queryset, slug=slug)
        cover = Book.cover

        return render(
            request,
            'book_detail.html',
            {
                'book': post,
                'cover': cover,
            },
        )
