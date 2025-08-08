from django.db import models

# Create your models here.
class BibleCover(models.Model):
    book = models.CharField(max_length=100, verbose_name="書名")
    image = models.ImageField(upload_to='book_covers/', verbose_name="封面圖片")

    def __str__(self):
        return self.book
