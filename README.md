# ATI.SU Тестовое задание

## Стек

- Python 3.11
- Django 5.2
- PostgreSQL 15
- Docker
- Poetry

---

## Запуск проекта

### 1. Клонируй репозиторий

```bash
git clonehttps://github.com/KhalilSultanov/AtiSuTestTask.git
cd ati-su-test-task
````

### 2. Создай `.env`

Пример содержимого:

```env
POSTGRES_DB=book_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=passwd
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 3. Собери и запусти

```bash
docker-compose up --build
```

---

### 4. Данные к админ-панели

* Логин: `admin`
* Пароль: `admin`

---

### 5. Swagger-документация

Документация доступна по адресу:

[http://localhost:8000/api/v1/docs/](http://localhost:8000/api/v1/docs/)

## Примеры запросов

### 1. Получить все книги

```http
GET /api/v1/books/
```

---

### 2. Фильтрация по автору

```http
GET /api/v1/books/?author=martin
```

---

### 3. Получить книгу по ID

```http
GET /api/v1/books/1/
```

---

### 4. Создать одну книгу

```http
POST /api/v1/books/
Content-Type: application/json
```

```json
{
  "title": "Refactoring",
  "author": "Martin Fowler",
  "publish_year": 1999
}
```

---

### 5. Создать несколько книг

```http
POST /api/v1/books/
Content-Type: application/json
```

```json
[
  {
    "title": "The Pragmatic Programmer",
    "author": "Andy Hunt",
    "publish_year": 1999
  },
  {
    "title": "Code Complete",
    "author": "Steve McConnell",
    "publish_year": 2004
  }
]
```

---
