from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="書名")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")

    class Meta:
        ordering = ['order']  # default sort order

    def __str__(self):
        return f"{self.order} - {self.name}"
