from django.contrib import admin
from unfold.admin import ModelAdmin
from book_service.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ("title", "author", "publish_year")
    list_filter = ("author",)
    search_fields = ("title", "author")
