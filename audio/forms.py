from django import forms

from audio.models import AudioBookModel


class AudioBookForm(forms.ModelForm):

    class Meta:
        model = AudioBookModel
        fields = ("title",)
