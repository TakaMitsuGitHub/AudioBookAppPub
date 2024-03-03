from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from rest_framework import generics

from audio.models import AudioBookModel
from audio.forms import AudioBookForm
from audio.serializers import TitleSerializer
from book.models import BookModel

class AudioIndexView(TemplateView):
    template_name = "audio/index.html"


class TitleList(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = TitleSerializer
