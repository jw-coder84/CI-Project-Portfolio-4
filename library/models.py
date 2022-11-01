from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    synopsis = models.TextField(max_length=1000, help_text='Enter a brief \
        description of the book')
    isbn = models.PositiveBigIntegerField(max_length=13, unique=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class BookIssued(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
