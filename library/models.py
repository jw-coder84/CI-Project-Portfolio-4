from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime, timedelta
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    cover = models.ImageField(
                    null=True,
    )
    author = models.CharField(max_length=200)
    synopsis = models.TextField(
        max_length=2000,
        help_text='Enter a brief description of the book'
    )
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre)

    def display_genre(self):
        """Creates a string for the Genre.
        This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title


class BookIssued(models.Model):
    expiry = datetime.today() + timedelta(days=14)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    return_date = models.DateField(default=expiry)
    borrower = models.CharField(max_length=80)

    @property
    def is_overdue(self):
        """Determines if the book is overdue based
        on due date and current date."""
        return bool(self.return_date and date.today() > self.return_date)

    LOAN_STATUS = (
        ('co', 'Checked out'),
        ('a', 'Available'),
    )

    status = models.CharField(
        max_length=2,
        choices=LOAN_STATUS,
        blank=True,
        default='co',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['return_date']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
