from django.shortcuts import render

from .models import Book, Verse

# Create your views here.
def index(request):
    book_list = Book.objects.order_by("order")
    verse_list = Verse.objects.filter(book=1, chapter=1)

    context = {}
    context['old_testament'] = book_list
    context['verses'] = verse_list

    return render(request, 'scriptures/index.html', context)