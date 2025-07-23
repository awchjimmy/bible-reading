from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect

from .models import Book, Verse

# Create your views here.
def index(request):
    return redirect('scripture:chapter', book=1, chapter=1)

def chapter(request, book, chapter):
    old_testament = Book.objects.filter(id__gte=1, id__lte=39)
    new_testament = Book.objects.filter(id__gte=40, id__lte=66)
    chapters = range(1, get_object_or_404(Book, id=1).chapter+1)
    verse_list = Verse.objects.filter(book=1, chapter=chapter)

    context = {}
    context['old_testament'] = old_testament
    context['new_testament'] = new_testament
    context['chapter'] = chapter
    context['chapters'] = chapters
    context['verses'] = verse_list

    return render(request, 'scriptures/index.html', context)
