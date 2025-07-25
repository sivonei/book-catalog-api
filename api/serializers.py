from rest_framework import serializers
from .models import Book

# Book Catalog API Serializers
# This module defines the serializers for the Book Catalog API.


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
