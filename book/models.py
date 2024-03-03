from django.db import models

# Create your models here.


class BookModel(models.Model):
    title = models.CharField(
        verbose_name="book_title",
        max_length=255,
        blank=True,
        default="",
        null=False
    )
    sentence = models.TextField(
        verbose_name="book_sentence",
        blank=True,
        default="",
        null=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
