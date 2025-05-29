from drf_spectacular.utils import OpenApiExample, OpenApiParameter

book_query_param = OpenApiParameter(
    name="author",
    description="Фильтрация по автору",
    required=False,
    type=str,
    location=OpenApiParameter.QUERY,
)

book_bulk_create_example = OpenApiExample(
    name="Пример запроса на создание нескольких книг",
    value=[
        {
            "title": "Преступление и наказание",
            "author": "Фёдор Достоевский",
            "publish_year": 1866,
        },
        {"title": "Война и мир", "author": "Лев Толстой", "publish_year": 1869},
    ],
    request_only=True,
)

book_response_example = OpenApiExample(
    name="Пример ответа",
    value={
        "id": 1,
        "title": "Война и мир",
        "author": "Лев Толстой",
        "publish_year": 1869,
    },
    response_only=True,
)

book_detail_response_example = OpenApiExample(
    name="Пример книги по ID",
    value={
        "id": 1,
        "title": "Война и мир",
        "author": "Лев Толстой",
        "publish_year": 1869,
    },
    response_only=True,
    status_codes=["200"],
)
