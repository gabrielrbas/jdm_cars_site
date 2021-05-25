from django.db import models
from django.utils import timezone


class Photos(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(timezone.now)
    source = models.ImageField(upload_to='photos/%Y/%m/')
