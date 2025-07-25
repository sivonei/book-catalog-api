from django.shortcuts import render

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Book Catalog API Views
# This module defines the views for the Book Catalog API.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
