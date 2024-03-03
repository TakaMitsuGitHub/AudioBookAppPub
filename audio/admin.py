from django.contrib import admin

from audio.models import AudioBookModel


class AudioBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(AudioBookModel, AudioBookAdmin)
