from django import forms

from book.models import BookModel


class BookForm(forms.ModelForm):

    class Meta:
        model = BookModel
        fields = ("title",)
