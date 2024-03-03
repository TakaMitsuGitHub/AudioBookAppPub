from rest_framework import serializers

from book.models import BookModel


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['title']
