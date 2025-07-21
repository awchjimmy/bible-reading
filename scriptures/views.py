from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    context['old_testament'] = [{
        'name': '創世記',
        'url': '#'
    },
    {
        'name': '出埃及記',
        'url': '#'
    },
    {
        'name': '利未記',
        'url': '#'
    },
    {
        'name': '民數記',
        'url': '#'
    },
    {
        'name': '申命記',
        'url': '#'
    }]

    context['new_testament'] = [{
        'name': '馬太福音',
        'url': '#'
    }]

    return render(request, 'scriptures/index.html', context)