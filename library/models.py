from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    cover = models.ImageField(
                    height_field=398,
                    width_field=261,
                    null=True,
    )
    author = models.CharField(max_length=200)
    synopsis = models.TextField(
        max_length=1000,
        help_text='Enter a brief description of the book'
    )
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class BookIssued(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    return_date = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('co', 'Checked out'),
        ('a', 'Available'),
    )

    status = models.CharField(
        max_length=2,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['return_date']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
