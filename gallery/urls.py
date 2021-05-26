from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pic_id>', views.pic_view, name='pic_view'),
]
