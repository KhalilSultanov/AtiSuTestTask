from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book_service.models import Book
from book_service.schema import (
    book_query_param,
    book_response_example,
    book_detail_response_example,
    book_bulk_create_example,
)
from book_service.serializers import BookSerializer, CreateBookSerializer


class BookListCreateAPIView(APIView):
    """
    GET: Возвращает список всех книг.
         Поддерживает фильтрацию по автору.

    POST: Создаёт новую книгу на основе переданных данных.
    """

    @extend_schema(
        tags=["api/v1"],
        summary="Получить список книг",
        description="GET: получение всех книг с возможностью фильтрации по автору",
        parameters=[book_query_param],
        responses=BookSerializer,
        examples=[book_response_example],
    )
    def get(self, request):
        author = request.query_params.get("author")
        books = Book.objects.all()
        if author:
            books = books.filter(author__icontains=author)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["api/v1"],
        summary="Создать одну или несколько книг",
        description="POST: создание книг",
        request=CreateBookSerializer,
        responses=BookSerializer,
        examples=[book_bulk_create_example, book_response_example],
    )
    def post(self, request):
        data = request.data
        is_many = isinstance(data, list)
        serializer = CreateBookSerializer(data=data, many=is_many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetBookByIdAPIView(APIView):
    """
    GET: Возвращает одну книгу по её ID.
         Если книга не найдена — возвращает 404.
    """

    @extend_schema(
        tags=["api/v1"],
        summary="Получить книгу по ID",
        description="Возвращает одну книгу по её ID",
        responses=BookSerializer,
        examples=[book_detail_response_example],
    )
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
