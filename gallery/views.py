from django.shortcuts import render, get_object_or_404
from .models import Pics


def index(request):
    pics = Pics.objects.all()
    return render(request, 'gallery/index.html', {
        'pics': pics
    })


def pic_view(request, pic_id):
    pic = get_object_or_404(Pics, id=pic_id)
    return render(request, 'gallery/pic_view.html', {
        'pic': pic
    })
