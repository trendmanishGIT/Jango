from django.contrib import admin
from .models import Car
from django.utils.html import format_html 

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'car Image'
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style','fuel_type', 'is_featured')
    list_display_links = ('id','thumbnail')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title')
    list_filter = ('city', 'model','year')




admin.site.register(Car, CarAdmin)
