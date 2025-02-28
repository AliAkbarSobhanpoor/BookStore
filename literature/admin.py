from django.contrib import admin
from . import models
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    model = models.Book
    list_display = [
        "name",
        "isbn_number"
    ]
admin.site.register(models.Book, BookAdmin)