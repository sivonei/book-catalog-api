from django.test import TestCase
from .models import Book
from rest_framework.test import APIClient
from rest_framework import status

# Book Catalog API Tests
# This module contains tests for the Book Catalog API.


class BookTests(TestCase):
    # Test cases for the Book Catalog API
    # This class contains tests for creating, listing, and deleting books.
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Test Book",
            "author": "Author Name",
            "isbn": "1234567890123",
            "published_date": "2020-01-01"
        }
    # Test setup for Book Catalog API
    # This method sets up the test client and sample book data.

    def test_create_book(self):
        response = self.client.post(
            "/api/books/", self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test listing books in the Book Catalog API
    # This method tests the retrieval of a list of books.
    def test_list_books(self):
        Book.objects.create(**self.book_data)
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test retrieving a single book in the Book Catalog API
    # This method tests the retrieval of a single book by its ID.
    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(f"/api/books/{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_single_book(self):  # Retrieve a single book
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book_data["title"])

    def test_update_book(self):  # Update a book's details
        updated_data = self.book_data.copy()
        updated_data["title"] = "Updated Title"
        response = self.client.put(
            f"/api/books/{self.book.id}/", updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")
