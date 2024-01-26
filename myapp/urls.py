from django.urls import path
from .views import hello, booksAPI, oneBookAPI

#함수 import
from .views import hello, booksAPI

urlpatterns = [
  path("hello/",hello),
  path("books/", booksAPI), #example books
  path("book/<int:bid>",oneBookAPI) #str bookname
]

