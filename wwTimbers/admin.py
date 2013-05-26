from django.contrib import admin
from models import (
    Image)

# Pimps out the admin page


class ImageAdmin(admin.ModelAdmin):
    list_display = ('path', 'title', 'group',)
    search_fields = ('title',)


admin.site.register(Image, ImageAdmin)
