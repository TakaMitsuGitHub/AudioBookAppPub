from django.db import models

from book.models import BookModel


class AudioBookModel(models.Model):
    title = models.CharField(
        verbose_name="audio_title",
        max_length=255,
        blank=True,
        default="",
        null=False
    )
    book = models.OneToOneField(
        to=BookModel,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.title = f'{self.title}_audio'

    def __str__(self):
        return self.title
