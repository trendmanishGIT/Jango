from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    
    thumbnail.short_description = 'photo'

    list_display = ('id', 'first_name', 'designation', 'created_date', 'thumbnail')
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name','last_name')
    list_filter = ('designation',)
    # list_per_page = (2)


admin.site.register(Team, TeamAdmin)