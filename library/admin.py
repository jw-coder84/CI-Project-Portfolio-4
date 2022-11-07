from django.contrib import admin
from .models import Book, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('synopsis')


admin.site.register(Genre)
