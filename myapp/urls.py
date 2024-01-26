from django.urls import path
from .views import hello

#함수 import
from .views import hello, booksAPI

urlpatterns = [
  path("hello/",hello),
  path("books/", booksAPI) #example books
]

