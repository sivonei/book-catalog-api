from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# This file defines the URL routing for the Book Catalog API.
# It uses Django REST Framework's DefaultRouter to automatically generate
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
