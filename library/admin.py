from django.contrib import admin
from .models import Book, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    summernote_fields = ('synopsis')


admin.site.register(Genre)
