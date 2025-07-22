from django.contrib import admin
from .models import Book, Verse

class VerseAdmin(admin.ModelAdmin):
    list_filter = ['chapter']

# Register your models here.
admin.site.register(Book)
admin.site.register(Verse, VerseAdmin)
