from .models import BookIssued
from django import forms


class BookBorrow(forms.ModelForm):
    class Meta:
        model = BookIssued
        exclude = ('status', 'id', 'book', 'return_date', 'borrower')
