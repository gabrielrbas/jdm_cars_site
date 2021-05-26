from django.shortcuts import render
from .models import Pics


def index(request):
    pic = Pics.objects.all()
    return render(request, 'gallery/index.html', {
        'pic': pic
    })
