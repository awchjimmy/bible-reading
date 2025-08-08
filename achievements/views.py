from django.http import HttpResponse
from django.shortcuts import render

from .models import BibleCover

# Create your views here.
def index(request):
    context = {}
    context['book_covers'] = BibleCover.objects.all()
    return render(request, 'achievements/index.html', context)
