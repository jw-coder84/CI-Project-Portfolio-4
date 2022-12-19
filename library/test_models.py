from django.test import TestCase
from .models import BookIssued, Book


class TestModels(TestCase):

    def test_book_string_method_returns_name(self):
        book = Book.objects.create(title='test book')
        self.assertEqual(str(book), 'test book')
