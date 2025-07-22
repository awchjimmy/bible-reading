from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="書名")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")

    class Meta:
        ordering = ['order']  # default sort order

    def __str__(self):
        return f"{self.order} - {self.name}"

class Verse(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="書名")
    chapter = models.IntegerField(verbose_name="第幾章")
    verse = models.IntegerField(verbose_name="第幾節")
    content = models.TextField(verbose_name="內容")

    class Meta:
        ordering = ['book', 'chapter', 'verse']  # default sort order

    def __str__(self):
        return f"{self.chapter}:{self.verse} {self.content}"
