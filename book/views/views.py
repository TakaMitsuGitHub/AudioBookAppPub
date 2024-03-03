from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from book.models import BookModel
from book.forms import BookForm


class CreateView(CreateView):
    template_name = "book/index.html"
    model = BookModel
    form_class = BookForm

    success_url = "/"
