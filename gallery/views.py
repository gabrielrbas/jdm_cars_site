from django.shortcuts import render
from .models import Pics


def index(request):
    pics = Pics.objects.all()
    return render(request, 'gallery/index.html', {
        'pics': pics
    })


def pic_view(request, pic_id):
    pic = Pics.objects.get(id=pic_id)
    return render(request, 'gallery/pic_view.html', {
        'pic': pic
    })
