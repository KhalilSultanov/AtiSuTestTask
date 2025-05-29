import re

from rest_framework import serializers
from book_service.models import Book
from datetime import date


class CreateBookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания книги.
    Содержит валидацию для названия, автора и года публикации.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Book title cannot be empty.")
        return value

    def validate_author(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Author name cannot be empty.")
        if not re.match(r"^[\w\s\.\-А-Яа-яЁё]+$", value):
            raise serializers.ValidationError(
                "Author name contains invalid characters."
            )
        if value.isdigit():
            raise serializers.ValidationError("Author name cannot be numeric.")
        return value

    def validate_publish_year(self, value):
        current_year = date.today().year
        if value < 1000 or value > current_year:
            raise serializers.ValidationError("Invalid publication year.")
        return value


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения книг.
    """

    class Meta:
        fields = "__all__"
        model = Book
