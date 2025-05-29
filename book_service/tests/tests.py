import pytest
from rest_framework import status
from django.urls import reverse
from book_service.models import Book
import json

pytestmark = pytest.mark.django_db


@pytest.fixture
def create_books():
    return [
        Book.objects.create(title="Book 1", author="Author A", publish_year=2020),
        Book.objects.create(title="Book 2", author="Author B", publish_year=2021),
        Book.objects.create(title="Book 3", author="Author A", publish_year=2022),
    ]


def test_get_all_books(client, create_books):
    response = client.get(reverse("book-list-create"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3


def test_get_books_filtered_by_author(client, create_books):
    response = client.get(reverse("book-list-create"), {"author": "Author A"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    for book in response.data:
        assert "Author A" in book["author"]


def test_create_single_book(client):
    payload = {"title": "New Book", "author": "New Author", "publish_year": 2024}
    response = client.post(reverse("book-list-create"), payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.count() == 1
    assert Book.objects.first().title == "New Book"


def test_create_multiple_books(client):
    payload = [
        {"title": "Book A", "author": "Author A", "publish_year": 2021},
        {"title": "Book B", "author": "Author B", "publish_year": 2022},
    ]
    response = client.post(
        reverse("book-list-create"),
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.count() == 2


def test_create_book_invalid_data(client):
    payload = {"title": "", "author": "", "publish_year": ""}
    response = client.post(reverse("book-list-create"), payload, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_book_by_id(client, create_books):
    book = create_books[0]
    response = client.get(reverse("book-detail", args=[book.id]))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == book.title


def test_get_book_by_id_not_found(client):
    response = client.get(reverse("book-detail", args=[999]))
    assert response.status_code == status.HTTP_404_NOT_FOUND
