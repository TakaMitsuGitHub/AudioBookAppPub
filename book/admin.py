from django.contrib import admin

from book.models import BookModel

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(BookModel, BookAdmin)
