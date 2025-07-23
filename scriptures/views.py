from django.shortcuts import get_list_or_404, render

from .models import Book, Verse

# Create your views here.
def index(request):
    old_testament = Book.objects.filter(id__gte=1, id__lte=39)
    new_testament = Book.objects.filter(id__gte=40, id__lte=66)
    verse_list = Verse.objects.filter(book=1, chapter=1)

    context = {}
    context['old_testament'] = old_testament
    context['new_testament'] = new_testament
    context['verses'] = verse_list

    return render(request, 'scriptures/index.html', context)

def verses(request, book, chapter):
    book_list = Book.objects.order_by("order")
    verses = get_list_or_404(Verse, book=book, chapter=chapter)

    context = {}
    context['old_testament'] = book_list
    context['chapter'] = verses[0].chapter
    context['verses'] = verses

    return render(request, 'scriptures/verse.html', context)
