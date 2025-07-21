from django.shortcuts import render

from .models import Book

# Create your views here.
def index(request):
    book_list = Book.objects.order_by("order")

    context = {}
    context['old_testament'] = book_list

    context['new_testament'] = [{
        'name': '馬太福音',
        'url': '#'
    }]

    return render(request, 'scriptures/index.html', context)