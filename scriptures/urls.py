from django.urls import path

from . import views

app_name = "scripture"

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:book>/chapter/<int:chapter>", views.chapter, name="chapter"),
]