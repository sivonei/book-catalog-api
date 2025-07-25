from django.db import models

# Book Catalog API Models
# This module defines the data models for the Book Catalog API.


class Book(models.Model):
    # Represents a book in the catalog.
    title = models.CharField(max_length=255)
    # Represents the author of the book.
    author = models.CharField(max_length=255)
    # Represents the ISBN of the book.
    isbn = models.CharField(max_length=13, unique=True)
    # Represents the genre of the book.
    published_date = models.DateField()

    def __str__(self):
        return self.title
