from django.test import TestCase
from .models import BookIssued, Book


class TestModels(TestCase):

    def book_string_method_returns_name(self):
        book = Book.objects.create(title='test book')
        self.assertEqual(str(book), 'test book')

    # def book_issued_status_defaults_to_co(self):
    #     book = BookIssued.objects.create(book='test book')
    #     self.assertEqual(status, 'co')
