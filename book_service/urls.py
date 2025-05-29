from django.urls import path

from book_service.views import BookListCreateAPIView, GetBookByIdAPIView

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", GetBookByIdAPIView.as_view(), name="book-detail"),
]
