from django.contrib import admin
from .models import Uploader,Photos,tags

# Register your models here.

class PhotosAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Uploader)
admin.site.register(Photos)
admin.site.register(tags)