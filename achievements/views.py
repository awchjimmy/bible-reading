from django.http import HttpResponse
from django.shortcuts import render

from .models import BibleCover

# Create your views here.
def index(request):
    context = {}
    book_covers = BibleCover.objects.all()
    progress = 6
    context['finished'] = book_covers[:progress]
    context['unfinished'] = book_covers[progress:]
    return render(request, 'achievements/index.html', context)
