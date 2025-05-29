from django.db import models


class Book(models.Model):
    title = models.CharField("Название", max_length=255)
    author = models.CharField("Автор", max_length=255, db_index=True)
    publish_year = models.PositiveIntegerField("Год публикации")

    def __str__(self):
        return f'"{self.title}" - {self.author}'

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
