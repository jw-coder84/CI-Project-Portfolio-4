from django.contrib import admin
from .models import Book, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'display_genre', 'cover')
    list_filter = ('title', 'genre')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'genre', 'author']
    summernote_fields = ('synopsis')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
