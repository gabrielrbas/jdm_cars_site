from django.contrib import admin
from .models import Pics


class PicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Pics, PicsAdmin)
